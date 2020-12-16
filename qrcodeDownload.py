
#import urllib.request as request
import requests

x = requests.get('https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl=%E5%8B%9D%E6%B5%A6%E9%AB%98%E4%B9%8B&choe=Shift_JIS')

#print(x)

with open('pic1.png', 'wb') as f:
    f.write(x)
'''
        response = requests.get(pic_url, stream=True)

        if not response.ok:
            print response

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
'''