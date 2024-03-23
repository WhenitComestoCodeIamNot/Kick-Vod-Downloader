A Python scirpt that takes a .m3u8 url from kick, extracts the dates downloads it via yt-dlp

** required yt-dlp.exe to work **


Setup**
change line 43 text to what ever you want the title to be in the filename
change line 65 to the output directoy you want
chance line 76 to the directory of yt-dlp.exe

run script with python
A popup opens to input the .m3u8 url then a popup to confirm the title you want. Click ok and yt-dlp will open a cmd window and start to dl the file. Once complete, it will let you know. 

Future plans**
more automation in grabbing file. (Need access to kick api for this)
handle duplicate file names better
handle mutliple url's at once

