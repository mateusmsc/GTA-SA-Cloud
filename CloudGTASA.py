import hashlib
import shutil
import time

SRC_ARCHIVE_1 = "C:\\Users\\mat3u\\Documents\\GTA San Andreas User Files\\gta_sa.set"
SRC_ARCHIVE_2 = "C:\\Users\\mat3u\\Documents\\GTA San Andreas User Files\\GTASAsf1.b"

DESTINY_ARCHIVE = "G:\\Meu Drive\\Jogos-Infos\\GTA SA"

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

def watchChanges():
  hashFile1Old = getHashFile(SRC_ARCHIVE_1)
  hashFile2Old = getHashFile(SRC_ARCHIVE_2)

  while True:
    print ("Verificando ...")

    #hasChanges
    hashFile1New = getHashFile(SRC_ARCHIVE_1)

    if hashFile1New != hashFile1Old:
      hashFile1Old = hashFile1New
      copyArchive(SRC_ARCHIVE_1,DESTINY_ARCHIVE)
      print("Copiando 1 ...")
    
    hashFile2New = getHashFile(SRC_ARCHIVE_2)
    if hashFile2New != hashFile2Old:
      hashFile2Old = hashFile2New
      copyArchive(SRC_ARCHIVE_2,DESTINY_ARCHIVE)
      print("Copiando 2 ...")
      
    time.sleep(5)

if __name__ == '__main__':
  watchChanges()