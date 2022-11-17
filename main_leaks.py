from git import Repo 
import json
import re 
import sys

# primero he clonado el repositorio a la carpeta correspondiente 


REPO_URL = 'https://github.com/skalenetwork/skale-manager'
REPO_PATH = 'skale__manager_a_rellenar'


def clonar(REPO_URL):
    # clonar aqui la url (si se ejecuta ahora con un archivo lleno no funcionara ya que el archio 'skale__manager_a_rellenar' ya existiría y no esta vacia
    # si se quiere ejecutar perfecto, ejecutar con este nombre y se guardara el cloning a la carpeta vacia
    repo = Repo.clone_from(url=REPO_URL, to_path='skale__manager_a_rellenar')
    return 

def salida_controlada():
    print("\nEnd program")
    sys.exit()

# ETL- cargar los commits a un json (bloque 1 y 3) 
def extract(REPO_PATH):
    repo = Repo(REPO_PATH)
    #nos creamos la lista de commits 
    commits = list(repo.iter_commits('develop'))
    
    return commits

def transform(commits,palabras):
    diccionario = {}
    for i in commits:
        for j in palabras:
            if re.search( j, i.message, re.IGNORECASE):
                #guardamos el par clave:valor en el diccionario
                data_1 = i.message
                keys  = i.hexsha
                #insercion en el diccionario
                diccionario[keys] = data_1

    return diccionario

def load(diccionario):
    #abrimos especificando el nombre del archivo, por eso no se lo pasamos a la funcion 
    archivo=open('commits_to.json', 'w')  
    #cargamos los commits al json 
    json.dump(diccionario, archivo, indent=3)


def main():
    
    palabras = ['credentials', 'password', 'key', 'username']
    
    clonar(REPO_URL)
    
    commits = extract(REPO_PATH)
    
    diccionario = transform(commits,palabras)
    
    load(diccionario)
    
    salida_controlada()
    

if __name__  == '__main__' :
    main()
    
