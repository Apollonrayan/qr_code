import time
import qrcode
from PIL import Image
import os
user = os.environ.get('USERNAME')
# récupère l'user

path_img = '\\\ined.fr\\Partages\\Sce_info\\03 - COMMUNICATION_interne_SSI\\img\\'
path_save = 'C:\\Users\\'+ user +'\\Pictures\\qr\\'
if not os.path.exists(path_save):
   os.makedirs(path_save)
#faire le chemin si il n'existe pas

ined= Image.open(path_img+'ined.png')
#Chemin vers le logo ined

qr_big = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    version = 1,
    box_size = 10,
    border = 4,
)
#taille du qr code + correction 30%
url = input("Entrez l'url : \n")

file = input("Entrez le nom de fichier : \n")
file_extension = file+".jpg"

bgColor=input("Couleur de background, en anglais ou un HEX (si hex il faut mettre le #) : \n")
qrColor =input("Entrez la couleur du qrcode : \n")
# info attendu

qr_big.add_data(url)
img_qr_big = qr_big.make_image(fill_color=qrColor, back_color=bgColor)
# entre les données dans le qr code
pos = ((img_qr_big.size[0] - ined.size[0]) // 2, (img_qr_big.size[1] - ined.size[1]) // 2)
img_qr_big.paste(ined, pos)
#copie le logo ined au centre de la map
img_qr_big.save(path_save+file_extension)
#enregistre le qrcode.

print("L'image a été enregistrer dans : "+path_save+file_extension+" \nLe QRCODE s'ouvrira dans 3secondes....")

time.sleep(3)
os.startfile(path_save+file_extension)

a = input('Appuyez sur une touche pour quitter.')
if a:
    exit(0)
#leave le script
