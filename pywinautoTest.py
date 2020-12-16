'''
win appの制御
https://stackoverflow.com/questions/39021888/using-pywinauto-to-control-a-currently-running-application

'HwndElementInfo join - Google Search - Google Chrome'

'''
#from pywinauto import application
import pywinauto
from pywinauto.application import Application

x = pywinauto.findwindows.find_elements()
#print(x)
#xx = ('\n').join(x)
with open('app.txt', 'w', encoding='utf-8') as f:
    for item in x:
        f.write(str(item) + '\n')

#app.window()

app = Application().connect(title='python app acrive controle - Google Search - Google Chrome')
print(app)


'''
https://stackoverflow.com/questions/28316597/pywinauto-wait-and-focus
OpenDialog = pwa_app.window(best_match=u'Open', class_name='#32770').wait('visible', timeout=20, retry_interval=0.5)
OpenDialog.set_focus()

pwa_app.OpenDialog.wait('visible', timeout=20)
pwa_app.OpenDialog.set_focus()
'''

#app.OpenDialog.wait('visible', timeout=20)
#app.OpenDialog.set_focus()

f = pywinauto.controls.hwndwrapper.HwndWrapper.has_focus(app)
print(f)  #false帰ってくる
# set_focusはない。dialogとらないとできない？
# windowをactiveにしたいだけなのだが
f = pywinauto.controls.hwndwrapper.HwndWrapper.set_focus(app)



