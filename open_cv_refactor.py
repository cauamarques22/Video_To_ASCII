import cv2 as cv
import time

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
#a largura do meu terminal é 237 caracteres.
#a altura é 60 caracteres
print("Renderizando...")
video_ascii = []
for frame_idx in range(int(cap.get(cv.CAP_PROP_FRAME_COUNT))):

    ret, frame = cap.read()
    resized_frames = cv.resize(frame, (212,60)) 
    frame_processado = []
    for height in range(60):

        linha_de_pixels = []
        for width in range(212):
            
            b,g,r = resized_frames[height][width]
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
    video_ascii.append(frame_processado)

lista_de_frames = []
for frame_do_video_ascii in video_ascii:
    
    frame_renderizado = ""
    for altura in range(60):
        for pixel in range(212):
            frame_renderizado += frame_do_video_ascii[altura][pixel]
        frame_renderizado+="\n"
    lista_de_frames.append(frame_renderizado)

txt_file = open(f"{video_file_name}.txt", "w")

for frame in lista_de_frames:
    txt_file.write(frame)
txt_file.close()

print("Deseja exibir o video?")
choice = input("\n1 - Sim\n2 - Não\n")
if choice == "2":
    print("O arquivo estará renderizado para que você possa executá-lo")
    SystemExit

for frame in lista_de_frames:
    print(frame)
    time.sleep(0.0333)


# for frame in range(np.shape(luminance_matrix)[0]):
#     print(frame)
#     for height in range(np.shape(luminance_matrix)[1]):


    # # Define dimensions
    # Nx, Ny, Nz = 848, 480, 3
    # X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), -np.arange(Nz))

    # kw = {
    #     'vmin': frame.min(),
    #     'vmax': frame.max(),
    #     'levels': np.linspace(frame.min(), frame.max(), 10),
    # }

    # # Create a figure with 3D ax
    # fig = plt.figure(figsize=(5, 4))
    # ax = fig.add_subplot(111, projection='3d')

    # # Plot contour surfaces
    # _ = ax.contourf(
    #     X[:, :, 0], Y[:, :, 0], frame[:, :, 0],
    #     zdir='z', offset=0, **kw
    # )
    # _ = ax.contourf(
    #     X[0, :, :], frame[0, :, :], Z[0, :, :],
    #     zdir='y', offset=0, **kw
    # )
    # C = ax.contourf(
    #     frame[:, -1, :], Y[:, -1, :], Z[:, -1, :],
    #     zdir='x', offset=X.max(), **kw
    # )
    # # --


    # # # Set limits of the plot from coord limits
    # # xmin, xmax = X.min(), X.max()
    # ymin, ymax = Y.min(), Y.max()
    # zmin, zmax = Z.min(), Z.max()
    # ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax], zlim=[zmin, zmax])

    # # Plot edges
    # edges_kw = dict(color='0.4', linewidth=1, zorder=1e3)
    # ax.plot([xmax, xmax], [ymin, ymax], 0, **edges_kw)
    # ax.plot([xmin, xmax], [ymin, ymin], 0, **edges_kw)
    # ax.plot([xmax, xmax], [ymin, ymin], [zmin, zmax], **edges_kw)

    # # Set labels and zticks
    # ax.set(
    #     xlabel='X',
    #     ylabel='Y',
    #     zlabel='Z',
    #     zticks=[0, 1, 2 , 3 , 4 ,5],
    # )

    # # Set zoom and angle view
    # ax.view_init(40, -30, 0)
    # ax.set_box_aspect(None, zoom=0.9)

    # # Colorbar
    # fig.colorbar(C, ax=ax, fraction=0.02, pad=0.1, label='Name [units]')

    # # Show Figure
    # plt.show()