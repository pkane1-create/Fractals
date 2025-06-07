from PIL import Image, ImageDraw
from functions import iterate


fixed_points = {(615,115),(38,307),(769,461),(692,576),(346,192),(115,423),(423,38),(423,461),(38,423),(538,192),(192,538)}

start = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

for r in [0.95]:

    iter = list(iterate(4,r,fixed_points))

    width, height = 1001,1001
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    draw.point(iter,fill = 'green')
    image.save(f'PatrickKane_ChloeKAllen_Green{r}.jpeg')

for r in [0.95]:

    iter = list(iterate(4,r,fixed_points))

    width, height = 1001,1001
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    draw.point(iter,fill = 'pink')
    image.save(f'PatrickKane_ChloeKAllen_Pink{r}.jpeg')
