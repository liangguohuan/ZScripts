import sys

sys.path.append('/home/hanson/CodeHub/PYTHON/AutoKey')
from DictHub import DictTable, SentenceTable
import re 

wc = window.get_active_class()
if wc in ['webbrowser-app.webbrowser-app', 'FoxitReader.Foxit Reader', 'subl.Subl']:
    sys.exit()

try:
    text = clipboard.get_selection()
except:
    text = ''

if len(text.split(' ')) > 1:
    tbl = SentenceTable()
    text = re.sub(r'(\s+)|(\n)', ' ', text)
    text = text.capitalize()
    fields = {'sentence': text}
else:
    tbl = DictTable()
    text = re.sub(r'(^[^A-Za-z]+)|([^A-Za-z]+$)', '', text)
    text = text.lower()
    fields = {'name': text}

if text != '':
    tbl.insert(fields)
    
#cmd = 'DISPLAY=:0 notify-send -t %d -i gtk-dialog-info -u critical "Save Sentence Secessed!"' % \
#      (time.time() + 100, )
#system.exec_command(cmd)