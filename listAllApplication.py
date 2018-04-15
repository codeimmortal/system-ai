for app in '/usr/share/applications/*.desktop':
   print(app) 
import os
import subprocess
os.system("ls /usr/share/applications/")
# os.startfile('/usr/share/applications/vlc.desktop')
subprocess.call('/usr/share/applications/vlc.desktop')