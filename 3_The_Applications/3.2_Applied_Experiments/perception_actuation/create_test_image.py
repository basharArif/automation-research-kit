from PIL import Image, ImageDraw

def create_test_image(file_path, size=(224, 224)):
    """Creates a simple test image with a red square on a white background."""
    img = Image.new('RGB', size, color = 'white')
    draw = ImageDraw.Draw(img)
    # Draw a red square in the center
    box_size = size[0] // 4
    x0 = (size[0] - box_size) // 2
    y0 = (size[1] - box_size) // 2
    x1 = x0 + box_size
    y1 = y0 + box_size
    draw.rectangle([x0, y0, x1, y1], fill='red')
    img.save(file_path)

if __name__ == "__main__":
    create_test_image("test_image.jpg")
