# write function that receives a picture and finds the secret message

from PIL import Image

PATH = 'code.png'

message = ''
with Image.open(PATH) as img:
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img.getpixel((i, j)) == 1:
                message += chr(j)

print(message)