from rembg import remove
from PIL import Image
input_path = 'testLogo.jpg'
output_path = 'testLogo_removed.png'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)