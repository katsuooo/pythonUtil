''' chrome start '''
'''
import webbrowser
url = 'http://docs.python.org/'
# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# Linux
# chrome_path = '/usr/bin/google-chrome %s'
webbrowser.get(chrome_path).open(url)

can i get os kind by python command???
'''
'''
problem
before no chrome window, cannot access to python server.
cause unknown 
'''

import webbrowser
import platform

class chromeStart:
    url = 'http://kdesignhp.web.fc2.com'
    def __init__(self):
        osName = platform.system()
        print('running os is...', osName)
        if osName == 'Windows':
            chrome_path = 'c:/program files (x86)/Google/CHrome/Application/chrome.exe %s'
        elif osName == 'Darwin':
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
        elif osName == 'Linux':
            chrome_path = '/usr/bin/google-chrome %s'
        else:
            print('OS_DETECTION_ERR!!!')
            return
        webbrowser.get(chrome_path).open(self.url)
        

if __name__ == '__main__':
    chromeStart()