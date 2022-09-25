# writer.py

import random
import time
from PIL import Image, ImageDraw, ImageFont

def startScreen():
    print(
        '██████╗  ██████╗  ██████╗██╗  ██╗███╗   ██╗████████╗████████╗    ██╗    ██╗██████╗ ██╗████████╗███████╗██████╗     ██╗   ██╗     ██╗    ██████╗')
    print(
        '██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝████╗  ██║╚══██╔══╝╚══██╔══╝    ██║    ██║██╔══██╗██║╚══██╔══╝██╔════╝██╔══██╗    ██║   ██║    ███║   ██╔═████╗')
    print(
        '██████╔╝██║   ██║██║     █████╔╝ ██╔██╗ ██║   ██║      ██║       ██║ █╗ ██║██████╔╝██║   ██║   █████╗  ██████╔╝    ██║   ██║    ╚██║   ██║██╔██║')
    print(
        '██╔══██╗██║   ██║██║     ██╔═██╗ ██║╚██╗██║   ██║      ██║       ██║███╗██║██╔══██╗██║   ██║   ██╔══╝  ██╔══██╗    ╚██╗ ██╔╝     ██║   ████╔╝██║')
    print(
        '██║  ██║╚██████╔╝╚██████╗██║  ██╗██║ ╚████║   ██║      ██║       ╚███╔███╔╝██║  ██║██║   ██║   ███████╗██║  ██║     ╚████╔╝      ██║██╗╚██████╔╝')
    print(
        '╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝      ╚═╝        ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝      ╚═══╝       ╚═╝╚═╝ ╚═════╝')
    for i in range(2):
        print('')

def isfont():
    is_font = False
    selected_font = ''
    fonts = ['1', '2', '3', '4']
    while is_font == False:
        selected_font = str(input('Выберите шрифт (1/2/3/4) //P.S лучший шрифт - третий//: '))
        if selected_font in fonts:
            is_font = True
            print('')
            print(f'Выбранный шрифт: {selected_font}')
        else:
            print('Не понял. Ответ не является номером шрифта')
    return selected_font

def typeInstruction():
    print('')
    time.sleep(2)
    print('Максимальное количество строк - 19.')
    time.sleep(2)
    print('Максимальное количество символов в строке - 25 (все лишнее автоматически будет обрезано)')
    time.sleep(2)
    print('Лимиты обусловлены размерами листка. ')
    time.sleep(2)
    print('Если хотите закончить печатать - напишите "КОНЕЦ" в поле для строки.')
    print('')
    return 0

startScreen()

im = Image.open('paper.jpg')
IsRunning = True
x = 340
y = 70
lines_done = 1
draw_text = ImageDraw.Draw(im)
isHeader = False
l_text = ''

font = isfont()

header_font = ImageFont.truetype(f'Fonts/{font}.ttf', size=150) # Шрифты
line_font = ImageFont.truetype(f'Fonts/{font}.ttf', size=90)

while IsRunning == True:
    typeInstruction()
    while lines_done < 21:
        l_text = str(input(f'Печатаю строку #{lines_done}, введите её текст.\n'
                           f'Если хотите, чтобы это был заголовок, перед текстом введите "[з]" без лишних пробелов.\n'
                           f'Пример: [з]Параграф 1.\nВведите в окно текста "КОНЕЦ", чтобы закончить печатать.\n'
                           f'Текст:'))
        print('')
        marker = l_text[:3]
        if marker.lower() == '[з]':
            draw_text.text(
                (x, y),
                l_text[3:],
                font=header_font,
                fill='#000F55')
            y += random.randint(98, 139)
        elif l_text == 'КОНЕЦ':
            break
        else:
            draw_text.text(
                (x, y),
                l_text,
                font=line_font,
                fill='#000F55')
            y += random.randint(120, 140)
        lines_done += 1
        l_text = ''
        x += random.randint(-20, 20)
    IsRunning = False
    resized_image = im.resize((720, 922))
    resized_image.show()