import requests
import os
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

path = 'Activities/Classroom/webscraping'
path_csv = 'Activities/Classroom/webscraping/pokemon'

def create_pokemon():
# USER AGENT PARA PROTEGERNOS DE BANEOS
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
    }
    
    os.makedirs(path, exist_ok=True)

    url = 'https://pokemondb.net/pokedex/all'
    pag = requests.get(url, headers=headers)
    soup = BeautifulSoup(pag.content, "html.parser")

    table = soup.find("table", class_="data-table sticky-header block-wide")
    row = table.find_all("tr")
    row = table.find("tbody").find_all("tr")

    position = []
    name = []
    hp = []
    attack = []
    defense = []

    for x in row:
        position.append(x.find_all("td")[0].get_text().replace("\n\n\n", ""))
        name.append(x.find_all("td")[1].get_text().replace("\n\n\n", ""))
        hp.append(x.find_all("td")[4].get_text().replace("\n\n\n", ""))
        attack.append(x.find_all("td")[5].get_text().replace("\n\n\n", ""))
        defense.append(x.find_all("td")[6].get_text().replace("\n\n\n", ""))
        
    dictionary_pokemon = pd.DataFrame({
        '#': position,
        'name': name,
        'hp': hp,
        'attack': attack,
        'defense': defense,
    })

    dictionary_pokemon.to_csv(path_csv)

def menu():
    print('''
Bienvenido al menu, por favor selecciona una opcion:
          
        1- Mostrar lista ordenada por 'HP'
        2- Mostrar lista ordenada por 'Ataque'
        3- Mostrar lista ordenada por 'Defensa'
        4- Salir
        ''')  
    
    while True:
        try:
            opcion = int(input('Selecciona una opcion: -> '))   
            break
        except ValueError:
            print('Caracter no valido \n')
    
    return opcion


def order_by_hp(file_p):
    return file_p.sort_values(by='hp')
    
def order_by_attack(file_p):
    return file_p.sort_values(by='attack')
    
def order_by_defense(file_p):
    return file_p.sort_values(by='defense')
    
    
options = {
    1: order_by_hp,
    2: order_by_attack,
    3: order_by_defense,
    4: exit
}


def read_action():
    file_pokemon = pd.read_csv(path_csv)

    while True:
        option = menu()
        print('-------------------------------------')

        if option == 4:
            break
        
        if option in options:
            file_pokemon = options[option](file_pokemon)
            print(file_pokemon)
        else:
            print('Opcion invalida')

# SEPERATION BETWEEN CODE AND MENU ^

if os.path.exists(path_csv): 
    read_action()
else:
    create_pokemon()
    read_action()