import zipfile
import downloader

nomearquivo=downloader.nomearquivo
nomesarquivos=[]



def peganomesarquivos():
    arquivo = open(nomearquivo, "r")
    for line in arquivo:
        print(line[-1])

    arquivo.close()
    #return nomesarquivos


#with ZipFile('spam.zip') as myzip:
 #   with myzip.open('eggs.txt') as myfile:
  #      print(myfile.read())


peganomesarquivos()