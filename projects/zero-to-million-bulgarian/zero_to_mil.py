def dali_da_ima_i(desetici, edinici, number, is_hilqdi):
    if is_hilqdi == True:
        stotici = nameri(number, 100)
    if not (desetici == 0 and edinici == 0):
        print(" ", end="")
        if is_hilqdi == False:
            if (desetici == 0 or edinici == 0) or number < 20:
                print("и ", end="")
        else:
            if stotici == 0:
                print("и ", end="")
    else:
        if is_hilqdi == True:
            print(" и ", end="")
def nameri(number, kakvo):
    stotici = number // 100
    edinici = (number - stotici * 100) % 10
    desetici = (number - stotici * 100) // 10
    if kakvo == 100:
        return stotici
    elif kakvo == 10:
        return desetici
    elif kakvo == 1:
        return edinici

def print_tricifreno(number):
    stotici = nameri(number, 100)
    edinici = nameri(number, 1)
    desetici = nameri(number, 10)
    texts = ["", "едно", "две", "три", "четири", "пет", "шест", "седем", "осем", "девет", "десет", "единадесет",
             "дванадесет", "тринадесет", "четиринадесет", "петнадесет", "шестнадесет", "седемнадесет", "осемнадесет",
             "деветнадесет"]
    texts_desetici = ["", "", "двадесет", "тридесет", "четиридесет", "петдесет", "шестдесет", "седемдесет", "осемдесет",
                      "деветдесет"]
    if number >= 100:
        if stotici == 1:
            print("сто", end="")
        elif stotici < 4:
            print(texts[stotici] + "ста", end="")
        else:
            print(texts[stotici] + "стотин", end="")
        number -= stotici * 100
        dali_da_ima_i(desetici, edinici, number, False)

    if number == 0 and stotici == 0:
        print("нула", end="")
    elif number < 20:
        print(texts[number], end="")
    elif number < 100:
        if edinici == 0:
            print(texts_desetici[desetici], end="")
        else:
            print(texts_desetici[desetici] + " и " + texts[edinici], end="")

while True:
    chislo = int(input())
    if chislo < 0:
        if chislo >= -1000000:
            print("минус ", end="")
        chislo = abs(chislo)
    if chislo == 1000000:
        print("милион")
    elif chislo > 1000000:
        print("извън диапазона")
    elif chislo >= 1000:
        hilqdi = int(str(chislo)[:-3])
        ostatuk = chislo - hilqdi * 1000
        if hilqdi != 1:
            print_tricifreno(hilqdi)
            print(" хиляди", end="")
        else:
            print("хиляда", end="")
        if ostatuk != 0:
            dali_da_ima_i(nameri(ostatuk, 10), nameri(ostatuk, 1), ostatuk, True)
            print_tricifreno(ostatuk)
    else:
        print_tricifreno(chislo)
    print("\n",end="")
