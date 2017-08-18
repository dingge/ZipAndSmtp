import os
from zipfile import *
import zipfile


def adddirfile():
       print 'ready to compress files.'
       f=zipfile.ZipFile('Udisk.zip','w',zipfile.ZIP_DEFLATED)
       startdir='./Udisk/'
       for root,dirs,files in os.walk(startdir):
              for filename in files:
                     f.write(os.path.join(root,filename))
       f.close()
       print 'compress success!'

