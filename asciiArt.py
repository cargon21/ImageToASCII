from PIL import Image
import sys 

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
    
def resize(image, new_width = 200):
    width, height = image.size
    print(height, width)
    ratio = height / width
    new_height = int(new_width * ratio / 3)
    print(new_height, new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

def main():
    path = input("Enter the path to the image fiel : \n")
    try:
        image = Image.open(path)
    except:
        print(path, "Unable to find image ")
        sys.exit()
    #resize image
    image = resize(image);
    #convert image to greyscale image
    greyscale_image = to_greyscale(image)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""

    #Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    #save the string to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img);
        
    print(ascii_img)

main()
