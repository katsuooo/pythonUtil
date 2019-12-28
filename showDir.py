'''show sub directroy size
指定フォルダのフォルダ名とサイズを取得する
'''
print('start')
import os
class getFileList:
    def __init__(self):
        pass
    def getFileNamesFromFolder(self, dirName):
        '''ディレクトリ内のファイル名リストを返す'''
        '''include sub directory files'''
        labels = []
        for root, dirs, files in os.walk(dirName):  
            for f in files:
                labels.append(f.split('.')[0])
        return labels
    def getFileNamesFromFolderExdir(self, dirName):
        '''ディレクトリ内のファイル名リストを返す'''
        '''指定ディレクトリのファイルのみ'''
        fileNames = []
        for root, dirs, files in os.walk(dirName):  
            if root == dirName:
                for f in files:
                    fileNames.append(f)
        return fileNames
    def getDirNames(self, dirName):
        '''get dir name list'''
        dirNames = []
        for root, dirs, files in os.walk(dirName):  
            if root == dirName:
                for dir in dirs:
                    dirNames.append(dir)
        return dirNames
    def getDir(self, parent):
        '''指定dir内のディレクトリ名を返す
        '''
        for root, dirs, files in os.walk(parent):
            if root == parent:
                print(root, dirs)
    def getFileSize(self, parent):
        '''指定dir内のディレクトリ名:ファイルサイズを返す
        '''
        for root, dirs, files in os.walk(parent):
            if root == parent:
                for fn in files:
                    path = os.path.join(root, fn)
                    size = os.stat(path).st_size # in bytes
                    print(path, size)
    def getSize(self, parent):
        for root, dirs, files in os.walk(parent):
            for fn in files:
                path = os.path.join(root, fn)
                size = os.stat(path).st_size # in bytes
                print(path, size)
    def get_size(self, start_path = '.'):
        '''start_path以下のそうファイルサイズを加算する'''
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        return total_size
    def sizeFormat(self, num):
        '''数値を単位表記に'''
        pass
    def getDirSize(self, parent):
        '''指定dir内のディレクトリ名:ディレクトリサイズを返す
        '''
        d = []
        for root, dirs, files in os.walk(parent):
            if root == parent:
                for dir in dirs:
                    path = os.path.join(root, dir)
                    size = self.get_size(path)
                    d.append({'dir':path, 'size': size})
        return d

gf = getFileList()
dirName = 'c:/work/chou2-sche-div'

def printList(l):
    '''list format print'''
    maxLen = 0
    for ll in l:
        if len(ll['dir']) > maxLen:
            maxLen = len(ll['dir'])
    for ll in l:
        dir = ll['dir']
        dirLen = len(dir)
        blankSize = maxLen - dirLen
        dirName = dir + ' ' * blankSize
        print(dirName, '{:,}'.format(ll['size']))

l = gf.getDirSize(dirName)
printList(l)

