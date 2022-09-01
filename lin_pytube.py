import functions
import yt_dlp
from colorama import init
from colorama import Fore, Back, Style
init()

# Variables
folder = r'$HOME/Videos/%(title)s.%(ext)s'
link_url = ''
switch = True


# Functions


# Load High Resolution video(s)
def download():
    print(Fore.GREEN, Style.BRIGHT)
    global link_url
    link_url = input('Вставьте ссылку на видео, плейлист или стрим >>> ')
    link_url.strip()
    global folder
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4+best[height<=1440]/(bv*[vcodec~=\'^((he|a)vc|h26[45])\']+ba) / (bv*+ba/b)',
        'playlist': 'yes',
        'ignore-errors': True,
        'live-from-start': True,
        'outtmpl': folder,
        'limit-rate': '1000M',
        'force-overwrites': True,
        'continue_dl': True,
        'skip-unavailable-fragments': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link_url])
        functions.clearscreen()
        functions.before_exit()


if __name__ == "__main__":
    functions.run()
