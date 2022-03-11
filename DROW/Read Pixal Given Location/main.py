from PIL import Image
import PIL
red_image = PIL.Image.open("WWE.png")
red_image_rgb = red_image.convert("RGBA")

rgb_pixel_value = red_image_rgb.getpixel((0,0))
print(type(rgb_pixel_value[0]))
