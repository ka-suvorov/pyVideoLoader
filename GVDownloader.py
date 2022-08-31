from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import win32clipboard
from tkinter import ttk
import yt_dlp
import subprocess as sp

# DEFS


def exit_application():
	msg_box = messagebox.askquestion('Exit Application', 'Хотите выйти из программы?', icon='warning')
	if msg_box == 'yes':
		root.destroy()
	else:
		messagebox.showinfo('Return', 'You will now return to the application screen')


def about_program():
	global version
	messagebox.showinfo('information', f'Notepad, version {version}')


def get_url():
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	url_video.insert(0, data)
	return data


def get_folder():
	path_dir = filedialog.askdirectory()
	get_path.delete(0, END)
	get_path.insert(0, path_dir)


def video_load():
	
	_path = get_path.get()
	_path += '\\%(title)s.%(ext)s'
	_url = url_video.get()
	ydl_opts = {
		'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/'
		'mp4+best[height>=1440]/(bv*[vcodec~=\'^((he|a)vc|h26[45])\']+ba) / (bv*+ba/b)',
		'playlist': 'yes',
		'ignore-errors': True,
		'live-from-start': True,
		'outtmpl': _path,
		'limit-rate': '1000M',
		'force-overwrites': True,
		'continue_dl': True,
		'skip-unavailable-fragments': True,
	}
	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		ydl.download([_url])
		statusbar.delete(0, 'end')
		statusbar.insert(0, 'Job is done!')
		print("download complete")


def open_video_source():
	programname = "notepad.exe"
	filename = "videoservice_txt"
	sp.Popen([programname, filename])


# Vars
column = ['Progress info']
version = '0.1.0'
url_link = ''
forder = ''
url = ''
root = Tk()

# window dimensions
WIDTH = 720
HEIGHT = 420

# Calculating window coordinates
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

# Setting the width and height of the window
root.geometry(F'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

# main setup
root.title(f'GVDownloader. written by K.A. Suvorov, версия программы: {version}')
root.resizable(False, False)
root.config(bg='#AFEEEE')

labels_frame = ttk.LabelFrame(root)
labels_frame.pack(fill=BOTH, expand=1)

gvd_label = ttk.Label(labels_frame, text='GVDownloader -version 0.1.0!')
gvd_label.pack(pady=1, fill=X, side=TOP)
info_label = ttk.Label(labels_frame, text='Download videos, playlist, streams from many resources!')
info_label.pack(pady=1, fill=X, side=TOP)

path_frame = ttk.LabelFrame(root)
path_frame.pack(fill=BOTH, expand=1)

get_path = ttk.Entry(path_frame, width=48)
get_path.pack(pady=1, side=LEFT)

path_button = ttk.Button(path_frame, text="выбрать каталог для загрузки", width=32, command=get_folder)
path_button.pack(pady=1, side=LEFT)

urls_frame = ttk.LabelFrame(root)
urls_frame.pack(fill=BOTH, expand=1)

url_video = ttk.Entry(urls_frame, width=48)
url_video.pack(pady=1, side=LEFT)

url_button = ttk.Button(urls_frame, text='Вставьте ссылку из буфера обмена', width=32, command=get_url)
url_button.pack(pady=1, side=LEFT)

videoservice_frame = ttk.LabelFrame(root)
videoservice_frame.pack(fill=BOTH, expand=1)

videoservice_button = ttk.Button(videoservice_frame, text='Посмотреть список видеосервисов', command=open_video_source)
videoservice_button.pack(pady=2, fill=X, side=BOTTOM)

download_frame = ttk.LabelFrame(root)
download_frame.pack(fill=BOTH, expand=1)

download_button = ttk.Button(download_frame, text='Скачать видео. плейлист или живой стрим', command=video_load)
download_button.pack(pady=2, fill=X, side=BOTTOM)

footer_frame = ttk.LabelFrame(root)
footer_frame.pack(fill=BOTH, expand=1)

exit_button = ttk.Button(footer_frame, text='Выйти из программы', command=exit_application)
exit_button.pack(pady=2, fill=X, side=TOP)


statusbar = ttk.Entry(footer_frame)
statusbar.pack(side=BOTTOM, fill=X)

tl = ttk.Style()
tl.configure('TLabel', font=('Arial', 14, 'bold'), padding=2, foreground='#A52A2A')
e = ttk.Style()
e.configure('TEntry', font=('Arial', 14, 'bold'), padding=4)
b = ttk.Style()
b.configure('TButton', font=('Arial', 14, 'bold'), padding=2, relief='curve', background='#E0FFFF', foreground='#4682B4')
f = ttk.Style()
f.configure('TLabelFrame', background='#696969')

# Main loop
try:
	if __name__ == '__main__':
		root.mainloop()
except EXCEPTION:
	messagebox.showerror('Ошибка!', 'Не корректный запуск программы!')
