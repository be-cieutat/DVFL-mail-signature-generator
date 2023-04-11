# Ce script permet de récupérer les informations de l'utilisateur et de les stocker dans un fichier _temp.txt
# Ce fichier sera ensuite utilisé par le script de génération de signature
# Ce script appelle ensuite le script de génération de signature DVFLsignatureGenerator.py


import subprocess
import os

'''

def multi_choice_input(question, options):
    print(question)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    while True:
        choice = input("Entrer votre choix: ")
        if type(choice) == str and choice.upper() in options:
            return choice.upper()
        if type(choice) == str and choice == '':
            return ''
        try:
            choice = int(choice)
            if 1 <= choice <= len(options):
                return options[choice-1]
        except ValueError:
            pass            

def mail_input(question):
    print(question)
    while True:
        try:
            mail = input()
            if '@edu.devinci.fr' in mail:
                return mail
            if mail != '' and not mail.__contains__('@'):
                return mail+'@edu.devinci.fr'
            if mail == '':
                return ''
        except ValueError:
            pass

def user_input(previousValues):
    if previousValues == ['','','','','','','','']:
        print('\nVeuillez saisir les informations suivantes :')
    else:
        print('\nVeuillez corriger les informations entrées.')
        print('\nSi vous ne souhaitez pas modifier une information, appuyez sur [Entrée].') 
    prenom = input(f'\nEntrez votre prénom ({previousValues[0]}):') or previousValues[0]
    nom = input(f'\nEntrez votre nom ({previousValues[1]}):') or previousValues[1]
    ecole = multi_choice_input(f'\nChoisissez votre école ({previousValues[2]}):',ecoles) or previousValues[2]
    anneeEtude = multi_choice_input(f'\nChoisissez votre année d\'étude ({previousValues[3]}):',anneesEtude) or previousValues[3]
    fonction = input(f'\nEntrez votre fonction au sein du bureau ({previousValues[4]}):') or previousValues[4]
    genre = multi_choice_input(f'\nChoisissez à quel genre s\'accorde votre signature ({previousValues[5]}) :',genres) or previousValues[5]
    urlLinkedIn = input(f'\nEntrez l\'url de votre LinkedIn ({previousValues[6]}) :') or previousValues[6]
    mailEcole = mail_input(f'\nEntrez votre adresse mail devinci.fr ({previousValues[7]}) :') or previousValues[7]
    return [prenom,nom,ecole,anneeEtude,fonction,genre,urlLinkedIn,mailEcole]




# Récupération des informations de l'utilisateur depuis la console
ecoles = ['ESILV','EMLV','IIM','SupdeVinci']
association = 'DVFL'
entry = ['','','','','','','','']
anneesEtude = ['A1','A2','A3','A4','A5']
genres = ['MASCULIN','FEMININ','NEUTRE']

while True:
    entry=user_input(entry)
    print('\nVous avez entré les informations suivantes :')
    print(f'Prénom : {entry[0]}')
    print(f'Nom : {entry[1]}')
    print(f'Ecole : {entry[2]}')
    print(f'Année d\'étude : {entry[3]}')
    print(f'Fonction : {entry[4]}')
    print(f'Genre : {entry[5]}')
    print(f'LinkedIn : {entry[6]}')
    print(f'Mail Ecole : {entry[7]}')
    validation=input('\nCes informations sont-elles correctes ? (o/n)')
    if validation in ['o','O','oui','Oui','']:
        break
    print('\n_______________________________________________________________\n')
'''  
# Appel du script de génération de signature

association = 'DVFL'
entry = ['Boyan-Edouard', 'Cieutat', 'ESILV', 'A4', 'vice-président', 'MASCULIN', 'url', 'boyan-edouard.cieutat@edu.devinci.fr'] # DEBUG
os.chdir("C:/Users/boyan/Projects/Python Personnal Projects/Fablab/MailSignatureGenerator") # DEBUG

subprocess.run(["python", "test.py"])
subprocess.run(["python", "DVFLsignatureGenerator.py", entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7], association])

# OLD
'''
# Création du fichier temporaire contenant les informations de l'utilisateur
with open('_temp.txt','w') as f:
    string = f'{entry[0]};{entry[1]};{entry[2]};{entry[3]};{entry[4]};{entry[5]};{entry[6]};{entry[7]};{association}'
    f.write(string)
    
# Appel du script de génération de signature
subprocess.run(["python", "DVFLsignatureGenerator.py", "_temp.txt"])
'''