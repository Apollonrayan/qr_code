import time
import qrcode
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
import string

#variable
yes_choices=['yes','y','oui','o']
no_choices=['no','n','non']
both_choice='2'
# récupère l'user
user = os.environ.get('USERNAME')
path_img = '\\\ined.fr\\Partages\\Sce_info\\03 - COMMUNICATION_interne_SSI\\img\\ined.png'
path_save = 'C:\\Users\\'+ user +'\\Pictures\\qr\\'
ined= Image.open(path_img)
### - qrcode maker underneath
def cleanInput(x):
    x= x.lower()
    x = x.strip()
    return x
def alphanumTrier(file):
  for character in file:
    if not character.isalnum() and character != " " and character != "_" and character != "-":
      return False
  return True

#initialise tkinter et ferme la fenetre pour meilleur expérience utilisateur
root = tk.Tk()
root.withdraw()
print("Voulez-vous changer le fichier de destination ? Y/N\nPar défaut il sera enregistrer dans le dossier /Pictures/qr :")
while True:
    folder_choice= input()
    folder_choice = cleanInput(folder_choice)
    if folder_choice in yes_choices:
        #utilisation de tkinter pour le choix du folder pour enregistrer le fichier
        path_save = filedialog.askdirectory()
        break
    elif folder_choice in no_choices:
        if not os.path.exists(path_save):
             os.makedirs(path_save)
        break
        #faire le chemin si il n'existe pas
    else:
        print("Entrez une valeur correct.\n")
        continue
#taille du qr code + correction 30%
qr_big = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    version = 2,
    box_size = 10,
    border = 4,
)
print("Entrez le nom pour le fichier : \n")


while True:
    file=input()
    file = file.strip()
    if not alphanumTrier(file):
        print("Merci d'écrire le nom sans caractère spéciaux.")
        continue
    else:
        print("Le fichier s'appelera "+file+"\n")
        break


print("Choisissez l'extension: png / jpg / pdf \n")
# vérification si l'user rentre bien une extension attendue
while True:
    extension = input()
    extension = cleanInput(extension)
    if len(extension) >= 5 or (extension != "png" and extension != "jpg" and extension != "pdf" and extension != ".png" and extension != ".jpg" and extension != ".pdf"):
        print("Entrez une extension valide :")
        continue
    elif len(extension) == 3 :
        extension = "." + extension
        break
    else:
        break
print("Le fichier sera donc : "+file+extension+"\n")
url = input("Entrez l'url ou les données que vous voulez encoder: \n")
#crée le QRCode avec la data donnée par l'user
qr_big.add_data(url)

print("Couleur de background : \n")
bgColor = tk.colorchooser.askcolor()
#la roulette de couleur nous donnes comme sorties le rgb et le # , on choisit le # pour plus de simplicité donc [1]
print("La couleur du background sera :"+bgColor[1]+"\n")
print("Entrer la couleur du qrcode : \n")
qrColor = tk.colorchooser.askcolor()
print("La couleur du QR Code sera :"+qrColor[1]+"\n")
# Mettre les couleurs
img_qr_big = qr_big.make_image(fill_color=qrColor[1], back_color=bgColor[1]).convert('RGB')
print(
        "Voulez-vous qu'il y ait le logo de l'ined sur le QRCODE ?\nAttention ! cela dégrade efficacité du QRCODE.\n"
        "Tapez yes/y pour l'avoir. \nTapez no/n pour ne pas l'avoir.\n"
        "Tapez 2, pour avoir les deux versions: "
    )
while True:
    ined_logo = input()
    ined_logo = cleanInput(ined_logo)
    if ined_logo in yes_choices:
        pos = ((img_qr_big.size[0] - ined.size[0]) // 2, (img_qr_big.size[1] - ined.size[1]) // 2)
        # centre l'img
        img_qr_big.paste(ined, pos)
        # copie le logo ined au centre du QRCODE
        img_qr_big.save(path_save + file+extension)
        # enregistre le qrcode.
        break
    elif ined_logo in no_choices:
        img_qr_big.save(path_save + file+extension)
        # enregistre le qrcode.
        break
    elif ined_logo in both_choice:
        img_qr_big.save(path_save + file + 'no_qr' + extension)
        # version sans ined
        pos = ((img_qr_big.size[0] - ined.size[0]) // 2, (img_qr_big.size[1] - ined.size[1]) // 2)
        # centre l'img
        img_qr_big.paste(ined, pos)
        # copie le logo ined au centre du QRCODE
        img_qr_big.save(path_save + file + '_qr' + extension)
        break
    else:
        print("Entrez une valeur correct.")
        continue

if ined_logo is both_choice:
        print("Les images sont enregistrées dans : " + path_save + " \n\nLes QRCODEs s'ouvriront dans 3secondes....")
        time.sleep(3)
        # attend 3 sec
        os.startfile(path_save + file + 'no_qr' + extension)
        os.startfile(path_save + file + '_qr' + extension)
        # ouvre les 2  QRCODE
else:
    print(
        "L'image est enregistrée dans : " + path_save + file+extension + " \n\nLe QRCODE s'ouvrira dans 3secondes....")
    time.sleep(3)
    # attend 3secondes
    os.startfile(path_save + file+extension)
    # ouvre le QRCODE

leave_script = input('Appuyez sur une touche pour quitter.')
if leave_script:
    exit(0)
# leave le script

