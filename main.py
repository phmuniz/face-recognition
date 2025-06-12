import json
from face_rec import make_face_recognition

faces_file = input("Identifique um arquivo json na pasta raiz que contenha os nomes e as faces a serem reconhecidas: ")

with open(faces_file) as file:
    faces = json.load(file)

option = 0

video_file = ''

while(True):
    print('\nSelecione uma opção: \n')
    print('1 - WebCam\n')
    print('2 - Arquivo de vídeo\n')
    option = int(input('Digite aqui sua escolha: '))

    if option != 1 and option != 2:
        print("Selecione uma opção válida!\n")
    else:
        break

if option == 2:
    video_file = input("Informe o nome do arquivo de vídeo: ")

make_face_recognition(faces, option, video_file)