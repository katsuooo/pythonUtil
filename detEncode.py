'''
encodeの取得

by chardet
'''
from getFileList import getFileList

gf = getFileList()
x = gf.getFullFileNamesFromFolder('detEncode')
print(x)
fname = 'detEncode/' + x[0]
with open(fname, 'rb') as f:
    t = f.read()
#print(t)
import chardet
det = chardet.detect(t)
print(det)
#{'encoding': 'SHIFT_JIS', 'confidence': 0.7121212121212122, 'language': 'Japanese'}
#
#confidence = 確度
#


