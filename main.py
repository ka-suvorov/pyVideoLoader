# usr/bin/python3

import os


# Main code
# Определение типа операционной системы (windows = nt, linux = posix))

try:
    switch = True
    if os.name == 'posix':
        os.system('python lin_pytube.py')
    elif os.name == 'nt':
        os.system('python win_pytube.py')
    else:
        print('This OS in not supported!')
        switch = False
except ImportError:
    print("Some modules not loaded, please check your source code!")


'''
try:
except ValueError:
print("You have some mistake of userinput Value!")
except TypeError:
print("You have some mistake of type Value!")
except SystemError:
print("This is system mistake! Please don't panic! Relax!")
except FileNotFoundError:
print("There isn't file here!")
except FileExistsError:
print("File or directory already exist!")
except ImportError:
print("Some modules not loaded, please check your source code!")
except IOError:
print('An error IO file!')

(bv*[vcodec~='^((he|a)vc|h26[45])']+ba) / (bv*+ba/b)
bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4+best[height<=1080]


'''