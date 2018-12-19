import config
import urllib.request
nomearquivo=config.nomearquivo
arquivo = open(nomearquivo,"w")

estados = config.estados
partidos = config.partidos
link = config.link
file = config.file
def baixatudo():
    for partido in partidos:
        for estado in estados:
            newfile = file+partido + "_" + estado + ".zip"
            arquivo.write(newfile+"\n")
            print("baixando "+ link+newfile)
            #urllib.request.urlretrieve(link+newfile, newfile)

    arquivo.close()

baixatudo()