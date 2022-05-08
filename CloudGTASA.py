import hashlib
import shutil
import time
import os
from dotenv import load_dotenv

#pip install python-dotenv

ARCHIVE_1 = "\\gta_sa.set"
ARCHIVE_2 = "\\GTASAsf1.b"

def initParams():
  load_dotenv()

  global SRC_ARCHIVE 
  SRC_ARCHIVE = os.getenv('SRC_ARCHIVE')
  
  global DESTINY_ARCHIVE
  DESTINY_ARCHIVE = os.getenv('DESTINY_ARCHIVE')

  global STEAM_PATH
  STEAM_PATH = os.getenv('STEAM_PATH')

def getHashFile(filename):
   h = hashlib.sha1()

   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)
   return h.hexdigest()

def copyArchive(srcArchive, destinyArchive):
  shutil.copy2(srcArchive, destinyArchive)

def hasChanges(hashFileOld, hashFileNew, archiveType):
  if hashFileNew != hashFileOld:
    hashFileOld = hashFileNew
    copyArchive(SRC_ARCHIVE + archiveType,DESTINY_ARCHIVE)
    print ("Copia feita arquivo "+archiveType)

def watchChanges():
  hashFile1Old = getHashFile(SRC_ARCHIVE + ARCHIVE_1)
  hashFile2Old = getHashFile(SRC_ARCHIVE + ARCHIVE_2)

  while True:
    print ("Verificando ...")

    hashFile1New = getHashFile(SRC_ARCHIVE + ARCHIVE_1)
    hasChanges(hashFile1Old, hashFile1New, ARCHIVE_1)

    hashFile2New = getHashFile(SRC_ARCHIVE + ARCHIVE_2)
    hasChanges(hashFile2Old, hashFile2New, ARCHIVE_2)
      
    time.sleep(5)

if __name__ == '__main__':
  initParams()
  os.system(f" \"{STEAM_PATH}\" -applaunch 12120")
  watchChanges()