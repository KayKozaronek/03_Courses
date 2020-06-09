from PIL import Image, ImageFilter

img = Image.open("Pokedex\Pikachu.jpg")

print(img)
print(img.format)
print(img.size)
print(img.mode)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur", "png")
filtered_img.show()