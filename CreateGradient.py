from PIL import Image, ImageDraw

def create_gradient(width, height):
    image = Image.new("RGB", (width, height), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)

    for x in range(width):
        r = 0
        g = int((x / width) * 255)
        b = 255 - int((x / width) * 255)

        for y in range(height):
            draw.point((x, y), fill=(r, g, b))

    return image

width = 255
height = 255

gradient_image = create_gradient(width, height)

# Save the image as non-compressed png
#gradient_image.save("gradient.png")  # Save the image to a file

# Save the image as a compressed JPEG with quality level (0-100)
compression_quality = 100  # Adjust as needed
gradient_image.save("Gradient.jpg", "JPEG", quality=compression_quality)