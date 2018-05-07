# coding: utf-8
#! /usr/bin/python3

''''Ejemplo de una aplciación que consume la API de Twitter.'''

import csv, twitter, json
from functools import reduce
CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET = "", "", "", ""


def accede_a_tw(fuente):
    '''Crea el objeto a partir del cual se consumirá la API de Twitter,
    leyendo las credenciales desde un archivo, definido en fuente.'''
    (CONSUMER_KEY,
     CONSUMER_SECRET,
     OAUTH_TOKEN,
     OAUTH_TOKEN_SECRET) = open(
            fuente, 'r').read().splitlines()
    auth = twitter.oauth.OAuth(OAUTH_TOKEN,
                           OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY,
                           CONSUMER_SECRET)
    return twitter.Twitter(auth=auth)

def busqueda_tw(tw, termino):
    '''Regresa los últimos 500 tuits en español de una búsqueda específica.'''
    return tw.search.tweets(q=termino, lang="es", count="500")["statuses"]


def guarda_tuits(tuits, archivo):
    '''Almacena los twits en formato JSON en el archivo especificado.'''
    with open(archivo, "w") as f:
        json.dump(tuits, f, indent=1)
        
def carga_tuits(archivo):
    '''En caso de que exista un archivo, lee los tuits almacenados en formato JSON.'''
    try:
        f = open(archivo, "r")
        resultado = json.load(f)
    except IOError:
        resultado = []
    else:
        f.close()
    return resultado

def mezcla_tuits(actuales, nuevos):
    '''Añade sólo los tuits que no existen aún en la lista.'''
    for tuit in nuevos: 
        if tuit["id"] not in [actual["id"] for actual in actuales]:
            actuales.append(tuit)
    return actuales

        
def main(archivo="tuits.json"):
    termino = input("Término de búsqueda: ")
    tw = accede_a_tw("credenciales.txt")
    tuits_previos = carga_tuits(archivo)
    tuits_recientes = busqueda_tw(tw, termino)
    tuits = mezcla_tuits(tuits_previos, tuits_recientes)
    guarda_tuits(tuits, archivo)
    
if __name__ == "__main__":
    main()