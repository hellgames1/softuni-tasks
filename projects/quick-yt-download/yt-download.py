"""
Quick multiple Youtube music downloader by hellgames1
Works only on Windows!
Downloads, converts and parses videos at the same time (in parallel)
Auto-fixes repeating links or links with extra arguments (playlist, start time, etc)
To use the program
1. Install the packages pywin32, pytube, requests and pygame
2. Download the image and sound files and place them in a directory called "data"
3. Download and unpack ffmpeg.exe from https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z
* you only need ffmpeg.exe, place it in the same directory as the script
4. Run the code
5. Open Youtube and start copying the links to every song/track that you want to download
6. When you copy a link, the video will appear in the program and you will hear a sound
* if the link is invalid or already in the list, you will hear a different sound and see an error message
7. Press the Start button to start downloading and converting the songs to mp3
* you can keep adding new songs while the program is processing
8. When you're finished, press the Exit button

The songs will be found in the "converted" directory
You can also add a playlist, and the program will start parsing all videos under 30 minutes in the playlist
Age-restricted videos are not supported!
"""

import win32clipboard, pytube.exceptions
from pytube import YouTube, Playlist
import requests
import pygame

from re import findall
from os import getcwd, path, makedirs, listdir
from time import sleep
from sys import exit
from io import BytesIO
from shutil import rmtree
import subprocess
import threading

def pre_exit():
    global thread_playlist_terminate
    thread_playlist_terminate = True
    rmtree("raw")
    exit()

data_directory = getcwd()+"\\data\\"
pygame.init()
pygame.display.set_caption("Quick&Easy Youtube MP3 downloader")
width, height = 800, 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
my_font = pygame.font.SysFont('Calibri', 30)
label_text = pygame.font.SysFont('Calibri', 24)
small_text = pygame.font.SysFont('Calibri', 12)

def display_error(text):
    global width, height
    while True:
        screen.fill((0, 0, 0))
        message_render = my_font.render(text, True, (255,255,255))
        screen.blit(message_render,(width / 2 - message_render.get_width() / 2, height / 2 - message_render.get_height()))

        ok = pygame.Rect(width / 2 - 128, height / 2 + message_render.get_height() / 2 + 32, 256, 64)
        pygame.draw.rect(screen, (128,128,128), ok)
        message_render = my_font.render("OK", True, (255,255,255))
        screen.blit(message_render,(width / 2 - message_render.get_width() / 2, height / 2 + message_render.get_height() / 2 + 48))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if ok.collidepoint(event.pos):
                        exit()
            elif event.type == pygame.VIDEORESIZE:
                width, height = screen.get_size()
        sleep(0.05)

try:
    label = pygame.image.load(data_directory + "label.png")
    sprites = pygame.image.load(data_directory + "sprites.png")
    positive_sound = pygame.mixer.Sound(data_directory + "positive.wav")
    negative_sound = pygame.mixer.Sound(data_directory + "negative.wav")
    delete_sound = pygame.mixer.Sound(data_directory + "delete.wav")
    icon = pygame.image.load(data_directory + 'icon.png')
except FileNotFoundError as error:
    display_error("Error: File '" + str(error).replace(f"No such file or directory: '{getcwd()}\\data\\", "").replace("'.","") + "' was not found in 'data' directory!")

if not path.isfile("ffmpeg.exe"):
    display_error("Error: File 'ffmpeg.exe' was not found in the program directory!")

trash = pygame.Surface((40,40))
trash.blit(sprites,(0,0))
info_icon = pygame.Surface((40,40))
info_icon.blit(sprites,(-40,0))
progress_icon = []
for i in range(6):
    progress_icon.append(pygame.Surface((40,40)))
    progress_icon[i].blit(sprites,(-80 - (i * 40), 0))



pygame.display.set_icon(icon)
pygame.mixer.Sound.set_volume(positive_sound,0.4)
pygame.mixer.Sound.set_volume(negative_sound,0.4)
pygame.mixer.Sound.set_volume(delete_sound,0.2)
rect_startbutton = pygame.Rect(800 - 128, 600 - 32, 128, 32)
rect_cancelbutton = pygame.Rect(0, 600 - 32, 128, 32)
rect_cancelparsebutton = pygame.Rect(width / 2 - 80, 600 - 68, 160, 32)
scrollbar = pygame.Rect(0,0,1,1)
temp_thumbnail = pygame.Surface((64,36))
temp_thumbnail.fill((0,0,0))

def get_progress_conv(size):
    try:
        with open("progress-log.txt", "r") as f:
            txt = f.read().replace("\n", "nlln")
        results = ['0']
        results.extend(findall(r"(?<=nllnout_time_ms=)(\d+)", txt))
        #print(results)
        percents = int(int(results[len(results) - 1]) // 1000000 / size * 100)
        return percents
    except:
        return 0

def clip(default):
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except TypeError:
        return "file"
    except:
        return default
    if data:
        return data
    else:
        return default


def blitRotate(surf, image, pos, angle, percent=100):
    if percent >= 100:
        percent = 100
    else:
        percent *= 0.7
        percent += 15
    image_rect = image.get_rect()
    offset_center_to_pivot = pygame.math.Vector2(20) - image_rect.center

    rotated_offset = offset_center_to_pivot.rotate(-angle)

    rotated_image_center = (20 - rotated_offset.x, 20 - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
    cropped = pygame.Surface((40 * (percent / 100),40))

    cropped.blit(rotated_image, rotated_image_rect)

    surf.blit(cropped, pos)

def draw_display():
    global anim_angle
    global scroller_offset
    global anim_helper
    global scrollbar
    global progress_conv, progress_conv_waiter
    if anim_helper == 1:
        if anim_angle[0] <= 30:
            anim_angle[0] = 360
        else:
            anim_angle[0] -= 30
        anim_helper = 0
    else:
        anim_helper = 1
    if anim_angle[1] <= 8:
        anim_angle[1] = 360
    else:
        anim_angle[1] -= 8
    states = ["downloading", "downloaded", "converting", "finished", "failed"]
    screen.fill((0, 0, 0))
    if not to_download:
        screen.blit(label,(width/2 - 400, height/2 - 300))
    for index, item in enumerate(to_download):
        if (40 * index + scrolled) < 0 or (40 * index + scrolled) > height - 40:
            continue
        screen.blit(item.thumbnail,(0,40 * index + scrolled))
        screen.blit(label_text.render(item.title, True, (255, 255, 255)),(72, 40 * index + 5 + scrolled))
        if item.progress == 0:
            timestamp = small_text.render(item.verbose_time, True, (255, 255, 255))
            pygame.draw.rect(screen,(0,0,0),(64-timestamp.get_width() - 2, 40 * index + 26  + scrolled, timestamp.get_width() + 2, 10))
            screen.blit(timestamp, (64-timestamp.get_width()-1, 40 * index + 27 + scrolled))
        if item.progress > 0:
            pygame.draw.rect(screen,(255,255,255),(0, 40 * index + 26  + scrolled, 64, 10))
            screen.blit(small_text.render(states[item.progress - 1], True, (0,0,0)),(3, 40 * index + 25  + scrolled))

            pygame.draw.rect(screen,(0,0,0),(width - 40 - scroller_offset, 40 * index + scrolled, 40, 40))
            if item.progress == 1:
                blitRotate(screen,progress_icon[0],(width - 40 - scroller_offset, 40 * index + scrolled), anim_angle[0])
            elif item.progress == 2:
                blitRotate(screen,progress_icon[1],(width - 40 - scroller_offset, 40 * index + scrolled), 0)
            elif item.progress == 3:
                blitRotate(screen,progress_icon[5],(width - 40 - scroller_offset, 40 * index + scrolled), anim_angle[1])
                if progress_conv_waiter == 0:
                    progress_conv = get_progress_conv(item.length)
                blitRotate(screen,progress_icon[2],(width - 40 - scroller_offset, 40 * index + scrolled), anim_angle[1], progress_conv)
            elif item.progress == 4:
                blitRotate(screen,progress_icon[3],(width - 40 - scroller_offset, 40 * index + scrolled), 0)
            elif item.progress == 5:
                blitRotate(screen,progress_icon[4],(width - 40 - scroller_offset, 40 * index + scrolled), 0)

            if item.info:
                screen.blit(info_icon, (width - 80 - scroller_offset, 40 * index + scrolled))

        else:
            screen.blit(trash, (width - 40 - scroller_offset, 40 * index + scrolled))
    for index, item in enumerate(to_download):
        if item.info == "" or (40 * index + scrolled) < 0 or (40 * index + scrolled) > height - 40:
            continue
        if pygame.Rect(width - 80 - scroller_offset, 40 * index + scrolled, 40, 40).collidepoint(pygame.mouse.get_pos()):
            info_message = label_text.render(item.info,True,(0,0,0))
            info_w, info_h = info_message.get_size()
            pygame.draw.rect(screen, (255, 255, 255),(pygame.mouse.get_pos()[0] - info_w, pygame.mouse.get_pos()[1], info_w, info_h))
            screen.blit(info_message,(pygame.mouse.get_pos()[0] - info_w, pygame.mouse.get_pos()[1]))



    pygame.draw.rect(screen, (0, 0, 0), (0, height - 32, width, 32))

    if phase == 0 and to_download:
        pygame.draw.rect(screen, (0, 128, 0), rect_startbutton)
        screen.blit(my_font.render("Start", True, (255, 255, 255)), (width - 92, height - 30))
    elif phase == 1:
        pygame.draw.rect(screen, (0, 0, 128), rect_startbutton)
        screen.blit(my_font.render("Pause", True, (255, 255, 255)), (width - 92, height - 30))


    pygame.draw.rect(screen, (128, 0, 0), rect_cancelbutton)
    screen.blit(my_font.render("Exit", True, (255, 255, 255)), (40, height - 30))

    if thread_playlist.is_alive():
        pygame.draw.rect(screen, (128, 0, 0), rect_cancelparsebutton)
        screen.blit(my_font.render("Stop parsing", True, (255, 255, 255)), (width/2 - 74, height - 66))
        blitRotate(screen, progress_icon[0], (width/2 - 20, height - 108), anim_angle[0])

    if message_timer:
        message_render = my_font.render(message_text, True, (255,255,255,0.5))
        alpha = 255
        if message_timer <= 10:
            alpha = message_timer * 25
        message_render.set_alpha(alpha)
        screen.blit(message_render,(width/2 - message_render.get_width() / 2, height-32))


    if len(to_download) > (height-40)/40:
        scroller_offset = 20
        scrollbar = pygame.Rect(width-18,(height - 40) * (-scrolled / len(to_download*40)),16,(height - 40)* ((height - 40) / len(to_download*40)))
        pygame.draw.rect(screen,(200,200,200), (width-20,0,20,(height - 38)))
        pygame.draw.rect(screen,(120,120,120), scrollbar)
    else:
        scroller_offset = 0

    pygame.display.flip()

thread_down = threading.Thread(target=print)
thread_conv = threading.Thread(target=print)
thread_playlist = threading.Thread(target=print)
thread_thumbs = threading.Thread(target=print)

class Tvid:
    def __init__(self):
        self.progress = 3
        self.info = "Video is age restricted!"
        self.valid = True
        self.title = "This is a test video"
        self.thumbnail = temp_thumbnail
        self.length = 2770
        self.verbose_time = "test"
    def run(self,to):
        pass

class Video:
    def __init__(self, address):
        global message_text
        global message_timer
        self.address = address
        self.progress = 0
        self.info = ""
        self.valid = True
        try:
            self.yt_instance = YouTube(address)
        except pytube.exceptions.RegexMatchError:
            self.valid = False
            message_timer = 50
            message_text = "Video address is invalid!"
        if self.valid:
            try:
                self.title = self.yt_instance.title
            except pytube.exceptions.VideoUnavailable:
                self.valid = False
                message_timer = 50
                message_text = "Video can't be found!"
        if self.valid:
            self.thumbnail = temp_thumbnail
            self.length = self.yt_instance.length
            self.temp_length = self.length
            self.verbose_time = ""
            if self.temp_length // 3600 > 0:
                self.verbose_time = f"{(self.length // 3600):02d}:"
                self.temp_length -= 3600 * (self.length // 3600)
            if self.temp_length // 60 > 0:
                self.verbose_time += f"{(self.temp_length // 60):02d}:"
                self.temp_length -= 60 * (self.temp_length // 60)
            self.verbose_time += f"{self.temp_length:02d}"



    def hatch_thumb(self):
        self.temp_thumbnail = pygame.Surface((120, 68))
        self.temp_thumbnail.blit(pygame.image.load(BytesIO(requests.get(self.yt_instance.thumbnail_url.replace("sddefault", "default").replace("hqdefault", "default"),timeout=3).content)), (0, -11))
        self.thumbnail = pygame.transform.scale(self.temp_thumbnail, (64, 36))

    def download(self):
        global job_index_down
        global job_index_conv
        global job_index_thumb
        global message_text
        global message_timer
        if path.isfile(getcwd() + "\\converted\\" + self.title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"','').replace('<','').replace('>','').replace('|','').replace("'", '').replace(",","") + ".mp3"):
            self.progress = 4
            message_timer = 50
            message_text = "File already exists!"
            self.info = message_text
        else:
            self.progress = 1
            try:
                self.audio_stream = self.yt_instance.streams.filter(type="audio", abr="128kbps")[0]
            except (pytube.exceptions.AgeRestrictedError, KeyError):
                self.progress = 5
                message_timer = 50
                message_text = "Video is age restricted!"
                self.info = message_text
            else:
                self.file_name = self.audio_stream.default_filename
                if path.isfile(f"{getcwd()}\\converted\\{self.file_name.replace('.mp4','.mp3')}"):
                    self.progress = 4
                    message_timer = 50
                    message_text = "File already exists!"
                    self.info = message_text
                else:
                    self.audio_stream.download("raw\\")
                    self.progress = 2
    def convert(self):
        global progress_conv_waiter, progress_conv
        self.progress = 3
        progress_conv_waiter = 1
        progress_conv = 0
        subprocess.run('ffmpeg.exe -loglevel fatal -progress progress-log.txt -y -i "raw\\' + self.file_name + '" -c:a libmp3lame -b:a 128k -ac 2 -ar 44100 "converted\\' + self.file_name[:-4] + '.mp3"', shell=True)
        subprocess.run('del "raw\\' + self.file_name + '"', shell=True)
        self.progress = 4

    def run(self,which):
        global thread_down, thread_conv, thread_thumbs
        if which == 0:
            thread_down = threading.Thread(target=self.download)
            thread_down.start()
        elif which == 1:
            thread_conv = threading.Thread(target=self.convert)
            thread_conv.start()
        elif which == 2:
            thread_thumbs = threading.Thread(target=self.hatch_thumb)
            thread_thumbs.start()

class Playlistt:
    def __init__(self,address):
        self.playlist = Playlist(address).video_urls
    def parse(self):
        global to_download
        global links
        global scrolled
        global height
        global thread_playlist_terminate
        for url in self.playlist:
            if url not in links:
                to_download.append(Video(url))
                links.append(url)
                if not to_download[-1].valid:
                    to_download.pop()
                else:
                    if to_download[-1].length > 1800:
                        to_download.pop()
                        links.pop()
                    else:
                        if len(to_download) > (height - 40) / 40 and scrolled == - (len(to_download) * 40 - height):
                            scrolled = - (len(to_download) * 40 - height + 40)
            if thread_playlist_terminate:
                thread_playlist_terminate = False
                break
    def run(self):
        global thread_playlist
        thread_playlist = threading.Thread(target=self.parse)
        thread_playlist.start()

to_download = []
#for i in range(16):
#    to_download.append(Tvid())
links = []
phase = 0
job_index_down = 0
job_index_conv = 0
job_index_thumb = 0
sleep(0.05)
last_clipboard = "start"
scrolled = 0
message_timer = 0
message_text = "error"
scroller_offset = 0
anim_angle = [0,0]
anim_helper = 0
thread_playlist_terminate = False
scrolling_mouse = False
scrolling_mouse_offset = (0,0)
progress_conv = 0
progress_conv_waiter = 0

win32clipboard.OpenClipboard()
try:
    win32clipboard.SetClipboardText("start", win32clipboard.CF_UNICODETEXT)
finally:
    win32clipboard.CloseClipboard()


if not path.exists("converted\\"):
    makedirs("converted")
if not path.exists("raw\\"):
    makedirs("raw")

def adjust_screen():
    global rect_startbutton
    global rect_cancelbutton
    global rect_cancelparsebutton
    global width
    global height
    global scrolled
    width, height = screen.get_size()
    rem = height % 40
    if rem != 0:
        if rem <= 20:
            height -= rem
        else:
            height += 40 - rem
        pygame.display.set_mode((width, height), pygame.RESIZABLE)
    rect_startbutton = pygame.Rect(width- 128, height - 32, 128, 32)
    rect_cancelbutton = pygame.Rect(0, height - 32, 128, 32)
    rect_cancelparsebutton = pygame.Rect(width / 2 - 80, height - 68, 160, 32)
    if height - scrolled - 40 > len(to_download)*40:
        if len(to_download) > (height-40)/40:
            scrolled = - (len(to_download)*40 - height + 40)
        else:
            scrolled = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pre_exit()
        elif event.type == pygame.MOUSEWHEEL:
            scrolled += event.y * 40
            if scrolled < (height - 40) - len(to_download)*40:
                scrolled -= event.y * 40
            if scrolled > 0:
                scrolled = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rect_cancelbutton.collidepoint(event.pos):
                    if len(listdir("converted")) > 0:
                        subprocess.run(f'explorer "{getcwd()}\\converted"', shell=True)
                    pre_exit()
                elif rect_startbutton.collidepoint(event.pos) and to_download:
                    phase = 1 - phase
                elif rect_cancelparsebutton.collidepoint(event.pos) and thread_playlist.is_alive() and thread_playlist_terminate == False:
                    thread_playlist_terminate = True
                elif len(to_download) > (height-40)/40 and scrollbar.collidepoint(event.pos) and scrolling_mouse == False:
                    scrolling_mouse_offset = (scrolled, pygame.mouse.get_pos()[1])
                    scrolling_mouse = True
                else:
                    for index, item in enumerate(to_download):
                        if pygame.Rect(width - 40 - scroller_offset, 40 * index + scrolled, 40, 40).collidepoint(event.pos) and item.progress == 0:
                            links.remove(item.address)
                            to_download.remove(item)
                            delete_sound.play()
                            adjust_screen()
                            break
            #elif event.button == 3:
            #    to_download.append(Tvid())
        elif event.type == pygame.MOUSEBUTTONUP and scrolling_mouse:
            scrolling_mouse = False
        elif event.type == pygame.VIDEORESIZE:
            adjust_screen()

    if scrolling_mouse:
        scrolled = scrolling_mouse_offset[0] + (scrolling_mouse_offset[1] - pygame.mouse.get_pos()[1]) / ((height - 40) / len(to_download*40))
        rem = scrolled % 40
        if rem != 0:
            if rem <= 20:
                scrolled -= rem
            else:
                scrolled += 40 - rem
        if height - scrolled - 40 > len(to_download) * 40:
            if len(to_download) > (height - 40) / 40:
                scrolled = - (len(to_download) * 40 - height + 40)
        elif scrolled > 0:
            scrolled = 0
    draw_display()
    data = clip(last_clipboard)

    if data != last_clipboard:
        if data[:32] == "https://www.youtube.com/watch?v=":
            if data.split("&")[0] not in links:
                to_download.append(Video(data.split("&")[0]))
                links.append(data.split("&")[0])
                if not to_download[-1].valid:
                    to_download.pop()
                    negative_sound.play()
                else:
                    positive_sound.play()
                    if len(to_download) > (height - 40) / 40:
                        scrolled = - (len(to_download) * 40 - height + 40)
            else:
                message_timer = 50
                message_text = "Video is already added!"
                negative_sound.play()
        elif data[:38] == "https://www.youtube.com/playlist?list=":
            if thread_playlist.is_alive():
                message_timer = 50
                message_text = "Already parsing playlist!"
                negative_sound.play()
            else:
                pl_temp = Playlistt(data)
                pl_temp.run()
                positive_sound.play()
        else:
            message_timer = 50
            message_text = "Not a YouTube video link!"
            negative_sound.play()
        last_clipboard = data

    if not thread_thumbs.is_alive():
        try:
            to_download[job_index_thumb].run(2)
            job_index_thumb += 1
        except IndexError:
            pass

    if phase == 1:
        if not thread_down.is_alive():
            try:
                to_download[job_index_down].run(0)
                job_index_down += 1
            except IndexError:
                pass
        if not thread_conv.is_alive():
            try:
                if to_download[job_index_conv].progress == 2:
                    to_download[job_index_conv].run(1)
                    job_index_conv += 1
                elif to_download[job_index_conv].progress == 4 or to_download[job_index_conv].progress == 5:
                    job_index_conv += 1
            except IndexError:
                pass

    if message_timer > 0:
        message_timer -= 1

    if progress_conv_waiter < 7:
        progress_conv_waiter += 1
    else:
        progress_conv_waiter = 0

    sleep(0.05)
