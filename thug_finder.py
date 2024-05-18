from PIL import Image
import os

im = Image.open("images.jpeg")

image_size = im.size
print(image_size)
txt_file = open("imagem.txt", "a")
for height in range(image_size[1]):
    for width in range(image_size[0]):
        r,g,b = im.getpixel((width, height))
        l = round((0.299*r) + (0.587*g) + (0.114*b))
        if l > 235:
            txt_file.write("#")
        elif l > 220:
            txt_file.write("X")
        elif l > 200:
            txt_file.write("%")
        elif l > 180:
            txt_file.write("&")
        elif l > 149:
            txt_file.write("*")
        elif l > 99:
            txt_file.write("+")
        elif l > 49:
            txt_file.write("/")
        elif l > 0:
            txt_file.write(",")
    txt_file.write("\n")
    #print("Searching Thugs..")
    

os.system("cls")
txt_file.close()
print("Thug Found!")

# print(im.format, im.size, im.mode)
# print(r,g,b)


#iterar pixel por pixel. (0,1) - (0,2) - (0,3)
#calcular a luminancia daquele pixel = (0.299*R + 0.587*G + 0.114*B)
#decidir qual caractere será utilizado para aquela luminancia.
#dar append no imagem.txt
#assim que o loop do width terminar, pular para uma nova linha no imagem.txt


#200 - 255 = @
#150 - 199 = #
#100 = 149 = X
#50 - 99 = I
#1 - 49 = ' 