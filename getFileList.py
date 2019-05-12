'''get file list in folder'''

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

if __name__ == '__main__':
    gf = getFileList()
    #print(gf.getFileNamesFromFolder('d:\work'))
    print(gf.getFileNamesFromFolderExdir('d:\work'))