
import sys
import urllib.request

import PIL.Image
import rembg
import openai

import PIL.Image as PImg

import urllib3.request

folderPath = "C:/Users/crhon/Desktop/buffer"

arguments = sys.argv

def getAverage(imageOpen:PIL.Image.Image, area, cellSize):
    avg = (0,0,0)
    for x in range(cellSize[0]):
        for y in range(cellSize[1]):
            avg2 = imageOpen.getpixel((area[0]+x, area[1] + y))
            avg = (avg[0] + avg2[0], avg[1] + avg2[1], avg[2] + avg2[2])
    totalPxl = cellSize[0]+cellSize[1]
    return (int(avg[0]/totalPxl), int(avg[1]/totalPxl), int(avg[2]/totalPxl))
def traitementImage(path, resolution, fileOutput):
    image = PImg.open(path)
    #image2 = open(folderPath + "/imagePixel.png", "wb")
    proportions = (int(image.width/resolution[0]), int(image.height/resolution[1]))

    imgPxl = PImg.new('RGBA', resolution, (0, 0, 0))
    pxl = imgPxl.load()
    for x in range(resolution[0]):
        for y in range(resolution[1]):
            pxl[x,y] = getAverage(image, (proportions[0]*x,proportions[1]*y), proportions)

    imgPxl.save(fileOutput);


openai.organization = "org-7GHrzPrQec6Q9QGVWpfDG3yC"
openai.api_key = "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"
openai.Model.list()


def createMonster(type):
    nbIteration = 8

    response = openai.Image.create(
        prompt=type + " virus as an 8-bit monster from a fantasy world, done using a red color palette",
        n=nbIteration,
        size="256x256"
    )
    for i in range(nbIteration):
        fileInput = folderPath + "/monster/" + type + "0-" + str(i) + ".png"
        fileOutput = folderPath + "/monster/" + type + "1-" + str(i) + ".png"

        url = (response['data'][i]['url'])
        urllib.request.urlretrieve(url, fileInput)
        open(fileOutput, 'wb').write(rembg.remove(open(fileInput, 'rb').read()))

def createBackground(type):
    nbIteration = 4

    response = openai.Image.create(
        prompt=type + " landscape in a fantasy world",
        n=nbIteration,
        size="1024x1024"
    )
    for i in range(nbIteration):
        fileInput = folderPath + "/background/" + type + "0-" + str(i) + ".png"

        url = (response['data'][i]['url'])
        urllib.request.urlretrieve(url, fileInput)
def createSprite():
    nbIteration = 4

    response = openai.Image.create(
        prompt="AIDS virus as an 8-bit monster from a fantasy world, done using a red color palette",
        n=nbIteration,
        size="256x256"
    )
    for i in range(nbIteration):
        fileInput = folderPath + "/image0-" + str(i) + ".png"
        fileOutput = folderPath + "/image1-" + str(i) + ".png"
        fileOutput2 = folderPath + "/image2-" + str(i) + ".png"

        url = (response['data'][i]['url'])
        urllib.request.urlretrieve(url, fileInput)
        #traitementImage(fileInput, (32, 32), fileOutput)
        open(fileOutput, 'wb').write(rembg.remove(open(fileInput, 'rb').read()))
        #open(fileOutput, 'wb').write(rembg.remove(open(fileInput, 'rb').read()))


def traitementTexte():
    txt = open(folderPath + "/t.txt", 'r', encoding="utf-8")
    buffer = txt.read()

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="summerize this:" +buffer
    )
    print(response['data'])

if len(arguments)>1:
    if arguments[1] == 'background':
        createBackground(arguments[2])
    else:
        createMonster(arguments[2])
else:
    createMonster('VIH')