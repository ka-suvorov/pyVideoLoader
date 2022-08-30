import os
import sys
from colorama import init
from colorama import Fore, Back, Style
from time import sleep
init()

# Variables
switch = True


def error_input_message():
    global switch
    print(Fore.RED, Style.BRIGHT + '''
    Ошибка! Выбирите действие:'
    1 - меню программы
    2 - выйти из программы''')
    switch = int(input('Ваш выбор? '))
    if switch == 1:
        tube_menu()
    elif switch == 2:
        switch = False
        load_shutdown_animation()


# Function clear of screen
def clearscreen():
    if os.name == 'nt':
        sleep(2)
        os.system('cls')
    elif os.name == 'posix':
        sleep(2)
        os.system('clear')
    else:
        print(Fore.YELLOW, Back.RED + 'Другие операционные системы не поддерживаются!')
        clearscreen()
        load_shutdown_animation()


# Exit Function
def tube_exit():
    sleep(2)
    print(Fore.RED + 'До свидания!')
    load_shutdown_animation()
    sys.exit()


# Start animation
def load_start_animation():
    print(Fore.MAGENTA + 'Video Console Downloader... \n')
    sleep(0.1)
    start = ['З', 'а', 'г', 'р', 'у', 'ж', 'а', 'е ', 'м ', 'с', 'я']
    succsess = '\n Программа успешно загружена!'

    for s in range(0, len(start)):
        sleep(0.2)
        print(Fore.GREEN, Style.BRIGHT + " ", start[s], end="")
    print(succsess)


# Exit Animation
def load_shutdown_animation():
    global switch
    print(Fore.RED + 'Video Console Downloader... \n')
    sleep(0.1)
    start = ['В', 'ы', 'г', 'р', 'у', 'ж', 'а', 'е ', 'м ', 'с', 'я']
    succsess = '\n Программа успешно завершена!'

    for i in range(0, len(start)):
        sleep(0.2)
        print(Fore.RED, Style.BRIGHT + " ", start[i], end="")
    print(succsess)
    sleep(1)
    switch = False


# Function run program
def run():
    load_start_animation()
    tube_menu()


# Function Before_exit
def before_exit():
    global switch
    clearscreen()
    print(Fore.RED, Style.BRIGHT + '''
    Вы действительно хотите выйти из программы?
    Выбирете один из пунктов меню:''')
    print()
    switch = int(input('\n\t1 - Выйти в главное меню, \n\t2 - Выйти из программы, \n\t>>> '))
    if (switch < 1) or (switch > 2):
        error_input_message()
    elif switch == 2:
        tube_exit()
    elif switch == 2:
        tube_menu()


# Menu function
def tube_menu():
    import win_pytube
    import lin_pytube
    clearscreen()
    print(Fore.GREEN, Style.BRIGHT + '''
    Добро пожаловать в меню программы Video Console Downloader!.
    Выберете один из пунктов меню:''')
    print()
    global switch
    switch = int(input('''  
    1 - Скачать видео или плейлимт с хорошим качеством'
    2 - Получить краткую помощь'
    3 - Выйти из программы'
    >>> '''))
    if (switch < 1) or (switch > 3):
        error_input_message()
    elif switch == 3:
        tube_exit()
    elif switch == 2:
        _help()
    elif switch == 1:
        try:
            switch = True
            if os.name == 'posix':
                lin_pytube.download()
            elif os.name == 'nt':
                win_pytube.download()
            else:
                print('This OS in not supported!')
                switch = False
        except ImportError:
            print("Some modules not loaded, please check your source code!")


# Function short help
def _help():
    print(Fore.GREEN, Style.BRIGHT + '''
    Программа puVideo Downloader позволяет скачивать видео со множества популярных видеохостингов.
    Скачивать можно как одно видео, так и плейлист целиком.
    Программа организована в виде несложных меню выбора, которое позволяет комфортно Вам работать с ней.''')


def damper():
    print('Damper Function')
