from rembg import remove
from PIL import Image
input_path= 'cl.jpg'
output_path= 'output.png'
input_image= Image.open(input_path)
output= remove(input_image)
output.save(output_path)
