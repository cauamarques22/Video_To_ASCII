#VIDEO TO ASCII V2
import cv2 as cv
import time
from numba import njit

print("Você deseja renderizar um vídeo, ou ler um video já renderizado?")
choice = input("1 - Renderizar video\n2 - Ler video renderizado\n")

if choice == "2":
    while True:
        try:
            archive = input("Informe o nome do arquivo .txt (não escreva .txt): ")
            txt_file = open(f"{archive}.txt", "r")
            break
        except:
            print("Arquivo não encontrado!")
            continue
      
    lines = txt_file.readlines()
    if len(lines) == 0:
        print("O arquivo está vazio!!")
        raise SystemExit
    
    total_frames = len(lines)//60
    archive_prep = []
    init = 0
    end = 60
    for x in range(0,len(lines),60):
        archive_prep.append(lines[init:end])
        init+=60
        end+=60

    displayable_frame = []
    for y in range(len(archive_prep)):
        concatenation = ""
        for x in range(60):
            concatenation += archive_prep[y][x]

        displayable_frame.append(concatenation)
        ultimo_item = list(concatenation)
        ultimo_item.pop()
        concatenation = str(ultimo_item)
    for x in displayable_frame:
        print(x)
        time.sleep(0.0333)

    raise SystemExit

while True:
    video_file_name = input("\nPor favor digite APENAS o NOME DO ARQUIVO que você deseja renderizar: ")
    try:
        open(f"{video_file_name}.mp4")
        break
    except (FileNotFoundError):
        print("Não foi encontrado o arquivo informado! Certifique-se de que seu Arquivo é do tipo MP4")

cap = cv.VideoCapture(f"{video_file_name}.mp4") 

print("Renderizando...")

@njit
def processar_pixels(frame_array):
    frame_processado = []
    for height in range(60):
        linha_de_pixels = []
        for width in range(212):
            b,g,r = frame_array[height][width]
            luminance = round((0.299*r) + (0.587*g) + (0.114*b))
            if luminance > 250:
                linha_de_pixels.append("$")
            elif luminance > 224:
                linha_de_pixels.append("&")
            elif luminance > 199:
                linha_de_pixels.append("@")
            elif luminance > 174:
                linha_de_pixels.append("%")
            elif luminance > 149:
                linha_de_pixels.append("#")
            elif luminance > 99:
                linha_de_pixels.append("/")
            elif luminance > 74:
                linha_de_pixels.append("+")
            elif luminance > 49:
                linha_de_pixels.append(";")
            elif luminance > 24:
                linha_de_pixels.append(",")
            elif luminance >= 0:
                linha_de_pixels.append(".")
        frame_processado.append(linha_de_pixels)
    return frame_processado

#t1 = time.time() #APENAS PARA DEBUG
video_ascii = []
for frame_idx in range(int(cap.get(cv.CAP_PROP_FRAME_COUNT))):
    ret, frame = cap.read()
    resized_frames = cv.resize(frame, (212,60)) 
    video_ascii.append(processar_pixels(resized_frames))
#t2 = time.time() #APENAS PARA DEBUG
#print(f"processar_pixels {t2-t1} segundos para processar a tarefa com NUMBA NJIT") #APENAS PARA DEBUG

def text_frame_builder():
    rendered_frames = []
    for frame_do_video_ascii in video_ascii:
        frame_renderizado = ""
        for altura in range(60):
            for pixel in range(212):
                frame_renderizado += frame_do_video_ascii[altura][pixel]
            frame_renderizado+="\n"
        rendered_frames.append(frame_renderizado) 
    return rendered_frames

txt_file = open(f"{video_file_name}.txt", "w")
returned_frame_builder = text_frame_builder() #FAZER O LOOP EM CIMA DO RETORNO DA FUNÇÃO PIORA A EFICIÊNCIA, ESTA É A MELHOR FORMA
#t1 = time.time() #APENAS PARA DEBUG
for frame in returned_frame_builder:
    txt_file.write(frame)
txt_file.close()
#t2 = time.time() #APENAS PARA DEBUG
#print(f"text_frame_builder levou {t2-t1} segundos para processar a tarefa") #APENAS PARA DEBUG

print("Deseja exibir o video?")
choice = input("\n1 - Sim\n2 - Não\n")
if choice == "2":
    print("O arquivo estará renderizado para que você possa executá-lo")
    raise SystemExit

for frame in returned_frame_builder:
    print(frame)
    time.sleep(0.0333)
