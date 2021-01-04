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

def calcular_vec_usuario(juegos):
    perfil_usuario=[]
    for game in  juegos:
        game_favorite=Vector_Caracteristicas.objects.filter(juego=game.titulo)
        pass
    return perfil_usuario

