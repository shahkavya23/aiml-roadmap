import sys
import os
from PIL import Image , ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3 : 
    sys.exit("Too many command-line arguments")

 
if not sys.argv[1].lower().endswith((".jpg" , ".jpeg" , ".png"))  or not  sys.argv[2].lower().endswith((".jpg" , ".jpeg" , ".png")) :
    sys.exit("Invalid output")

# //os.path.splitext(file) - used as as it only splits by last dot

name1 , ext1 = os.path.splitext(sys.argv[1])
name2 , ext2 = os.path.splitext(sys.argv[2])


if ext1.lower() != ext2.lower():
    sys.exit("Input and output have different extensions")

try:

    
    photo = Image.open(sys.argv[1])

        
    shirt = Image.open("shirt.png")
    size = shirt.size

    photo = ImageOps.fit(photo,size)

    photo.paste(shirt,shirt)

    photo.save(sys.argv[2])
    
except FileNotFoundError:
    sys.exit("Input does not exist")


