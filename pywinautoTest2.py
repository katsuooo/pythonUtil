import random
import time
from pywinauto import application
from pywinauto.findwindows import WindowAmbiguousError, WindowNotFoundError

APPS_POOL = ['Chrome', 'GVIM', 'Notepad', 'Calculator', 'SourceTree', 'Outlook']


# Select random app from the pull of apps
def show_rand_app():
    # Init App object
    app = application.Application()

    random_app = random.choice(APPS_POOL)
    try:
        print('Select "%s"' % random_app)
        app.connect(title_re=".*%s.*" % random_app)

        # Access app's window object
        app_dialog = app.top_window_()

        app_dialog.Minimize()
        app_dialog.Restore()
        #app_dialog.SetFocus()
    except(WindowNotFoundError):
        print('"%s" not found' % random_app)
        pass
    except(WindowAmbiguousError):
        print('There are too many "%s" windows found' % random_app)
        pass

for i in range(15):
    show_rand_app()
    time.sleep(0.3)