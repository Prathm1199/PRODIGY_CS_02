from PIL import Image

def encrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ 123, g ^ 123, b ^ 123)  # simple XOR

    img.save(output_path)

encrypt_image("cat.jpg", "encrypted.jpg")
