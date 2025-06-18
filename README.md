# face-recognition
Neste repositório é implementado um reconhecedor de faces cadastradas, seja por um vídeo externo, ou pela webcam. Para realizar este trabalho foram utilizadas as bibliotecas face_recognition e opencv, do Python.

## Como funciona?
Para rodar o código, basta digitar no terminal:
```bash
python3 main.py
```
Será solicitado o nome e o caminho a partir da pasta raiz de um arquivo json que contenhas as informações das faces a serem cadastradas, assim como no arquivo faces.json no exemplo. Após isso, será preciso selecionar uma opção de captura de vídeo: 0, para webcam e 1, para um vídeo externo. Caso opte pelo vídeo, será solicitado o nome e o caminho a partir da pasta raiz do vídeo, como no exemplo. Com isso, as faces cadastradas serão identificadas pelo nome no vídeo ou na webcam.

## Referências
- <a href="https://github.com/ageitgey/face_recognition">Repositório no github do face-recognition</a>
