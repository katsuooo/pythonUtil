'''some text

some more text
https://stackoverflow.com/questions/40265705/press-key-with-pywinauto/40266078

'''


# from pywinauto.SendKeysCtypes import SendKeys # old for pywinauto==0.5.x
from pywinauto.keyboard import send_keys

send_keys('some text{ENTER 2}some more textt{BACKSPACE}', with_spaces=True)


