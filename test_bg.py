import time
import qrcode
from PIL import Image
import os



### - qrcode maker underneath
user = os.environ.get('USERNAME')
# récupère l'user

path_img = '\\\ined.fr\\Partages\\Sce_info\\03 - COMMUNICATION_interne_SSI\\img\\ined.png'
path_save = 'C:\\Users\\'+ user +'\\Pictures\\qr\\'
if not os.path.exists(path_save):
   os.makedirs(path_save)
#faire le chemin si il n'existe pas

ined= Image.open(path_img)
#Chemin vers le logo ined

qr_big = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    version = 2,
    box_size = 10,
    border = 4,
)
#taille du qr code + correction 30%
url = input("Entrez l'url : \n")

file = input("Entrez le nom de fichier : \n")
extension=".jpg"
file_extension = file+".jpg"
bgColor=input("Couleur de background, en anglais ou un HEX (si hex il faut mettre le #) : \n")
qrColor =input("Entrez la couleur du qrcode : \n")
# info attendu

qr_big.add_data(url)
img_qr_big = qr_big.make_image(fill_color=qrColor, back_color=bgColor).convert('RGB')
# entre les données dans le qr code

print("Voulez-vous qu'il y ait le logo de l'ined sur le QRCODE ?\nAttention ! cela dégrade efficacité du QRCODE.\nTapez yes/y pour l'avoir. \nTapez no/n pour ne pas l'avoir.\nTapez 2, pour avoir les deux versions: ")
yes_choices=['yes','y','oui','o']
no_choices=['no','n','non']
both_choice='2'
while True:
    ined_logo=input()
    if ined_logo.lower() in yes_choices:
        pos = ((img_qr_big.size[0] - ined.size[0]) // 2, (img_qr_big.size[1] - ined.size[1]) // 2)
        #centre l'img
        img_qr_big.paste(ined, pos)
        # copie le logo ined au centre du QRCODE
        img_qr_big.save(path_save + file_extension)
        # enregistre le qrcode.
        break
    elif ined_logo.lower() in no_choices:
        img_qr_big.save(path_save + file_extension)
    # enregistre le qrcode.
        break
    elif ined_logo in both_choice:
        img_qr_big.save(path_save+file+'no_qr'+extension)
        #version sans ined
        pos = ((img_qr_big.size[0] - ined.size[0]) // 2, (img_qr_big.size[1] - ined.size[1]) // 2)
        #centre l'img
        img_qr_big.paste(ined, pos)
        # copie le logo ined au centre du QRCODE
        img_qr_big.save(path_save+file+'_qr'+extension)
        break
    else:
        print("Entrez une valeur correct.")
        continue

if ined_logo is both_choice:
    print("L'image a été enregistrer dans : "+path_save+" \n\nLes QRCODEs s'ouvriront dans 3secondes....")
    time.sleep(3)
    #attend 3 sec
    os.startfile(path_save+file+'no_qr'+extension)
    os.startfile(path_save+file+'_qr'+extension)
    #ouvre les 2  QRCODE
else:
    print("L'image a été enregistrer dans : " + path_save + file_extension + " \n\nLe QRCODE s'ouvrira dans 3secondes....")
    time.sleep(3)
    # attend 3secondes
    os.startfile(path_save + file_extension)
    #ouvre le QRCODE


leave_script = input('Appuyez sur une touche pour quitter.')
if leave_script:
    exit(0)
#leave le script
