#https://medium.com/@wenxuan0923/feature-extraction-from-text-using-countvectorizer-tfidfvectorizer-9f74f38f86cc
import nltk
import random
from gamehouse.sjug.models import Juego

def calcular_cpus(juegos):
    """ Esta funcion recibe la lista de ids de los juegos """
    seccion = len(juegos) // 5
    cpus = []
    terminos = {
            0:4, #Obtener los tres primeros terminos de la primera seccion
            1:3, #Obtener los dos siguients terminos de la segunda seccion
            2:2, #Obtener los dos siguients terminos de la tercera seccion
            3:1,
            4:1,
            5:0
    }
    #Caso donde hay resto:
    if  len(juegos) % 5: # Si hay resto hacer lista con juegos restantes
        terminos = {
            0:3, #Obtener los tres primeros terminos de la primera seccion
            1:2, #Obtener los dos siguients terminos de la segunda seccion
            2:2, #Obtener los dos siguients terminos de la tercera seccion
            3:1,
            4:1,
            5:1
        }
    i = 0
    while i < 5: #Obtener listas de juegos por secciones
        inicio = i * seccion
        chunk = juegos[inicio:inicio+seccion]
        escogido = random.randint(0, seccion-1) #Escoger un indice aleatorio entre 0 y el tamanio de la lista
        juego = Juego.objects.get( id_juego = chunk[escogido] )
        tokens = nltk.word_tokenize(juego.descripcion_limpia,"spanish")
        tokens_dist = nltk.FreqDist(tokens)
        for word, frequency in tokens_dist.most_common(terminos[i]):
            cpus.append(word)
            print('%s;%d' % (word, frequency))
        i = i + 1
    if len(juegos) % 5: #Si hay resto hacer para una ultima lista
        inicio = i * seccion ## Obtener una lista con el sobrante
        resto = juegos[inicio:]
        escogido = random.randint(0, seccion-1) #Escoger un indice aleatorio entre 0 y el tamanio de la lista
        juego = Juego.objects.get( id_juego = resto[escogido] )
        tokens = nltk.word_tokenize(juego.descripcion_limpia,"spanish")
        tokens_dist = nltk.FreqDist(tokens)
        for word, frequency in tokens_dist.most_common(terminos[i]):
            cpus.append(word)
            print('%s;%d' % (word, frequency))
    return cpus

def calcular_caracteristicas(caracteristicas,frecuencia):
    cpus=""
    listtemp=[]
    print("Número caracteristicas")
    print(len(caracteristicas))
    for cde in caracteristicas:
        listtemp.append(frecuencia[cde])
    cpus=','.join(str(x) for x in listtemp)
    return cpus

import numpy as np
def calcular_vec_usuario(juegos,gamer):
    perfil_usuario=[]
    listgeneros=[]
    listplataformas=[]
    listcpu=[]
    listcdes=[]
    i=0
    for game in  juegos:
        vector=Vector_Caracteristicas.objects.get(jugador=gamer,juego=game.titulo)
        Gen_Pla=ListGeneros.objects.get(jugador=gamer, juego=game.titulo)
        #Get elements from every game of user
        cpus=vector.cpus
        cdes=vector.cdes
        genes=Gen_Pla.listgenero
        platas=Gen_Pla.listplataforma
        #Get a list of elements
        cpus=cpus.split(',')
        cdes=cdes.split(',')
        platas=platas.split(',')
        genes=genes.split(',')
        #append in one list
        listgeneros.append(genes)
        listplataformas.append(platas)
        listcpu.append(cpus)
        listcdes.append(cdes)
    #Change type to Array
    gen = np.array(listgeneros)
    pla = np.array(listplataformas)
    ccpu = np.array(listcpu)
    ccde = np.array(listcdes)
    #Calculate de Mean
    #Sort   Genero,Plataforma,CPU,CDE
    perfil_usuario.append(np.average(gen, axis=0))
    perfil_usuario.append(np.average(pla, axis=0))
    perfil_usuario.append(np.average(ccpu, axis=0))
    perfil_usuario.append(np.average(ccde, axis=0))

        
        pass
    #perfil_usuario=/i
    return perfil_usuario


def CountGen(generos):
  genes=['Acción','Arcade','Aventura','Bélico','Carreras','Deporte','Disparo',
  'Educacional','Estrategia','Juegos de mesa','Música','Peleas','Plataforma',
  'Rol (RPG)','Rompecabezas','Simulación','Survival horror','Trivia']
  generos.sort()
  genes.sort()
  listgeneros=[]
  cero=0
  uno=1
  for i in range(18): 
    if genes[i] not in generos:
      listgeneros.append(cero)
    else:
      listgeneros.append(uno)
  #print("Esta son los generos",listgeneros)
  return listgeneros

def CountPlat(plataformas):
  platas=['Android','Arcade','Dreamcast','Gameboy',
  'Gameboy Advance','Gameboy Color','J2ME','Linux',
  'NES','Neo Geo','Nintendo 3DS','Nintendo 64','Nintendo DS',
  'Nintendo GameCube','Nintendo Switch','PS Vita','PSP',
  'PlayStation 1','PlayStation 2','PlayStation 3','PlayStation 4',
  'SNES','Wii','Wii U','Windows',
  'Xbox','Xbox 360','Xbox One','iOS']
  platas.sort()
  plataformas.sort()
  listplataformas=[]
  cero=0
  uno=1
  for i in range(29): 
    if platas[i] not in plataformas:
      listplataformas.append(cero)
    else:
      listplataformas.append(uno)
  return listplataformas

