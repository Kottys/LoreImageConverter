from PIL import Image

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

size = 32, 15

image = Image.open("image.jpg") #change path to image, cannot be a png

image = image.resize(size)
pixel_values = list(image.getdata())
print(pixel_values)

loreLine = ""

for i in range(0, len(pixel_values)):
    value = pixel_values[i]
    loreLine += "<"+rgb2hex(value[0], value[1], value[2])+">█"
    if((i+1)%32 == 0 and i != len(pixel_values)):
        loreLine += "\n"

loreLine = str(loreLine).replace(" ", '')
print(loreLine)

with open("Output.txt", "w", encoding="utf-8") as text_file: #outputs the Loreline in Output.exe
    text_file.write(loreLine)