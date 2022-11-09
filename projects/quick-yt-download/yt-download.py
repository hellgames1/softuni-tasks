"""
Quick multiple Youtube music downloader by hellgames1
Works only on Windows!
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
8. You can keep adding songs while the program is working
9. When you're finished, press the Exit button

The songs will be found in the "converted" directory
"""

import win32clipboard, pytube.exceptions
from pytube import YouTube
import requests
import pygame

from os import system, getcwd, path, makedirs, listdir
from time import sleep
from sys import exit
from io import BytesIO
from shutil import rmtree
import threading

def pre_exit():
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
    trash = pygame.image.load(data_directory + "trash.png")
    progress_icon = [pygame.image.load(data_directory + "progress_1.png"), pygame.image.load(data_directory + "progress_2.png"), pygame.image.load(data_directory + "progress_3.png")]
    positive_sound = pygame.mixer.Sound(data_directory + "positive.wav")
    negative_sound = pygame.mixer.Sound(data_directory + "negative.wav")
    icon = pygame.image.load(data_directory + 'icon.png')
except FileNotFoundError as error:
    display_error("Error: File '" + str(error).replace(f"No such file or directory: '{getcwd()}\\data\\", "").replace("'.","") + "' was not found in 'data' directory!")

if not path.isfile("ffmpeg.exe"):
    display_error("Error: File 'ffmpeg.exe' was not found in the program directory!")

pygame.display.set_icon(icon)
pygame.mixer.Sound.set_volume(positive_sound,0.4)
pygame.mixer.Sound.set_volume(negative_sound,0.4)
rect_startbutton = pygame.Rect(800 - 128, 600 - 32, 128, 32)
rect_cancelbutton = pygame.Rect(0, 600 - 32, 128, 32)

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


def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    rotated_offset = offset_center_to_pivot.rotate(-angle)

    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    surf.blit(rotated_image, rotated_image_rect)

def draw_display():
    global anim_angle
    global scroller_offset
    global anim_helper
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
    states = ["downloading", "downloaded", "converting", "finished"]
    screen.fill((0, 0, 0))
    if not to_download:
        screen.blit(label,(width/2 - 400, height/2 - 300))
    for index, item in enumerate(to_download):
        screen.blit(item.thumbnail,(0,40 * index + scrolled))
        screen.blit(label_text.render(item.title, True, (255, 255, 255)),(72, 40 * index + 5 + scrolled))

        if item.progress > 0:
            pygame.draw.rect(screen,(255,255,255),(0, 40 * index + 26  + scrolled, 64, 10))
            screen.blit(small_text.render(states[item.progress - 1], True, (0,0,0)),(3, 40 * index + 25  + scrolled))

            pygame.draw.rect(screen,(0,0,0),(width - 40 - scroller_offset, 40 * index + scrolled, 40, 40))
            if item.progress == 1:
                blitRotate(screen,progress_icon[0],(width - 20 - scroller_offset, 40 * index + scrolled + 20), (20,20), anim_angle[0])
            elif item.progress == 2:
                blitRotate(screen,progress_icon[1],(width - 20 - scroller_offset, 40 * index + scrolled + 20), (20,20), 0)
            elif item.progress == 3:
                blitRotate(screen,progress_icon[1],(width - 20 - scroller_offset, 40 * index + scrolled + 20), (20,20), anim_angle[1])
            elif item.progress == 4:
                blitRotate(screen,progress_icon[2],(width - 20 - scroller_offset, 40 * index + scrolled + 20), (20,20), 0)

        else:
            screen.blit(trash, (width - 40 - scroller_offset, 40 * index + scrolled))



    pygame.draw.rect(screen, (0, 0, 0), (0, height - 32, width, 32))

    if phase == 0 and to_download:
        pygame.draw.rect(screen, (0, 128, 0), rect_startbutton)
        screen.blit(my_font.render("Start", True, (255, 255, 255)), (width - 92, height - 30))
    elif phase == 1:
        pygame.draw.rect(screen, (0, 0, 128), rect_startbutton)
        screen.blit(my_font.render("Pause", True, (255, 255, 255)), (width - 92, height - 30))


    pygame.draw.rect(screen, (128, 0, 0), rect_cancelbutton)
    screen.blit(my_font.render("Exit", True, (255, 255, 255)), (40, height - 30))


    if message_timer:
        message_render = my_font.render(message_text, True, (255,255,255,0.5))
        alpha = 255
        if message_timer <= 10:
            alpha = message_timer * 25
        message_render.set_alpha(alpha)
        screen.blit(message_render,(width/2 - message_render.get_width() / 2, height-32))


    if len(to_download) > (height-40)/40:
        scroller_offset = 20
        pygame.draw.rect(screen,(200,200,200), (width-20,0,20,(height - 38)))
        pygame.draw.rect(screen,(120,120,120), (width-18,(height - 40) * (-scrolled / len(to_download*40)),16,(height - 40)* ((height - 40) / len(to_download*40))))
    else:
        scroller_offset = 0

    pygame.display.flip()

thread = threading.Thread(target=print)

class Tvid:
    def __init__(self):
        self.progress = 0
        self.valid = True
        self.title = "This is a test video"
        self.thumbnail = pygame.Surface((120,68))
        self.thumbnail.blit(pygame.image.load("test.jpg"),(0,-11))
        self.thumbnail = pygame.transform.scale(self.thumbnail,(64,36))

class Video:
    def __init__(self, address):
        global message_text
        global message_timer
        self.address = address
        self.progress = 0
        self.valid = True
        try:
            self.yt_instance = YouTube(address)
        except pytube.exceptions.RegexMatchError:
            self.valid = False
            message_timer = 100
            message_text = "Video address is invalid!"
        if self.valid:
            try:
                self.title = self.yt_instance.title
            except pytube.exceptions.VideoUnavailable:
                self.valid = False
                message_timer = 100
                message_text = "Video can't be found!"
        if self.valid:
            self.thumbnail = pygame.Surface((120,68))
            self.thumbnail.blit(pygame.image.load(BytesIO(requests.get(self.yt_instance.thumbnail_url.replace("sddefault", "default").replace("hqdefault", "default"), timeout=3).content)),(0,-11))
            self.thumbnail = pygame.transform.scale(self.thumbnail,(64,36))
    def download(self):
        self.progress = 1
        self.audio_stream = self.yt_instance.streams.filter(type="audio", abr="128kbps")[0]
        self.file_name = self.audio_stream.default_filename
        self.audio_stream.download("raw\\")
        self.progress = 2
    def convert(self):
        self.progress = 3
        system('ffmpeg.exe -loglevel fatal -i "raw\\' + self.file_name + '" -c:a libmp3lame -b:a 128k -ac 2 -ar 44100 "converted\\' + self.file_name[:-4] + '.mp3"')
        system('del "raw\\' + self.file_name + '"')
        self.progress = 4
    def run(self,which):
        global thread
        if which == 0:
            thread = threading.Thread(target=self.download)
        elif which == 1:
            thread = threading.Thread(target=self.convert)
        thread.start()



to_download = []
#for i in range(13):
#    to_download.append(Tvid())
links = []
phase = 0
job_index = 0
sleep(0.05)
last_clipboard = "start"
scrolled = 0
message_timer = 0
message_text = "error"
scroller_offset = 0
anim_angle = [0,0]
anim_helper = 0

win32clipboard.OpenClipboard()
try:
    win32clipboard.SetClipboardText("start", win32clipboard.CF_UNICODETEXT)
finally:
    win32clipboard.CloseClipboard()


if not path.exists("converted"):
    makedirs("converted")
if not path.exists("raw"):
    makedirs("raw")

def adjust_screen():
    global rect_startbutton
    global rect_cancelbutton
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
    if height - scrolled - 40 > len(to_download)*40:
        if len(to_download) > (height-40)/40:
            print("Outside")
            scrolled = - (len(to_download)*40 - height + 40)
        else:
            print("Scroll to top")
            scrolled = 0
    #print(f"{scrolled} | {height} | {len(to_download)*40}")

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
                        system(f'explorer "{getcwd()}\\converted"')
                    pre_exit()
                elif rect_startbutton.collidepoint(event.pos) and to_download:
                    phase = 1 - phase
                else:
                    for index, item in enumerate(to_download):
                        if pygame.Rect(width - 40 - scroller_offset, 40 * index + scrolled, 40, 40).collidepoint(event.pos) and item.progress == 0:
                            links.remove(item.address)
                            to_download.remove(item)
                            adjust_screen()
                            break
            #elif event.button == 3:
            #    to_download.append(Tvid())
        elif event.type == pygame.VIDEORESIZE:
            adjust_screen()


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
                message_timer = 100
                message_text = "Video is already added!"
                negative_sound.play()
        else:
            message_timer = 100
            message_text = "Not a YouTube video link!"
            negative_sound.play()
        last_clipboard = data

    if phase == 1:
        if not thread.is_alive():
            try:
                to_download[job_index // 2].run(job_index % 2)
                job_index += 1
            except IndexError:
                pass

    if message_timer > 0:
        message_timer -= 1

    sleep(0.05)
