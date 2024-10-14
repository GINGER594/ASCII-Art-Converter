from PIL import Image
import os, urllib.request

#list of ascii chars
chars = ["@", "#", "$", "%", "&", "8", "*", "o", "0", "+", "=", "-", ":", ";", ",", ".", " "]

def getImg():
    #giving the user the choice of using a downloaded file or an img url
    choice = input("1 - File\n2 - Img address (url)\n")
    if choice == "1":
        img = Image.open(input("Enter file name: "))
    elif choice == "2":
        urllib.request.urlretrieve(input("Enter image address: "), "img.png")
        img = Image.open("img.png")
    return img, choice

def factorImg(img):
    height = int(input("Enter height: "))
    #scaling img based on height
    width = int(img.width * (height / img.height) * 1.25) #width is scaled based on height & multiplied by n as new lines are taller than each char is wide
    img = img.resize((width, height))
    return img

def Convert(img):
    asciilist = []
    #looping through each pixel
    for y in range(img.height):
        row = ["|"]
        for x in range(img.width):
            #getting an avg rgb value and inverting it (dark mode/personal preference)
            brightness = 255 - (img.getpixel((x, y))[0] + img.getpixel((x, y))[1] + img.getpixel((x, y))[2]) // 3
            #giving it an ascii value based on how bright it is & adding it to asciilist
            index = int((brightness / 255) * (len(chars) - 1))
            row.append(chars[index])
        row.append("|")
        asciilist.append(row)
    return asciilist

def writeImg(asciilist):
    #adding borders, width & height captions to the ascii img
    data = "-" * (len(asciilist[0]) * 2 - 1)
    for row in asciilist:
        data += "\n" + " ".join(row)
    data += "\n" + "-" * (len(asciilist[0]) * 2 - 1) + f"\nWidth: {len(asciilist[0])} Height: {len(asciilist)}"

    #writing ascii art to the .txt file
    with open("image.txt", "w") as file:
        file.write(data)

def main():
    os.system("cls")
    #getting img from user input
    img, choice = getImg()
    #greyscaling, adjusting contrast based on user input & resizing based on user input
    img = factorImg(img)
    #adding ascii character conversion to list
    asciilist = Convert(img)
    #deleting the created file if the user used an img url
    if choice == "2":
        os.remove("img.png")
    #writing list to .txt file
    writeImg(asciilist)
main()