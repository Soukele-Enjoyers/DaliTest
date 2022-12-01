
import os
import urllib.request

import rembg
import openai

import urllib3.request

openai.organization = "org-7GHrzPrQec6Q9QGVWpfDG3yC"
openai.api_key = "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"
openai.Model.list()

nbIteration = 4
folderPath = "C:/Users/crhon/Desktop/buffer";

response = openai.Image.create(
    prompt="3D representation of a AIDS virus with a stickman body, 8-bit style red palette",
    n=nbIteration,
    size="256x256"
)
for i in range(nbIteration):
    fileInput = folderPath + "/image" + str(i) + ".png"
    fileOutput = folderPath + "/image" + str(i) + str(nbIteration) + ".png"
    url = (response['data'][i]['url'])
    urllib.request.urlretrieve(url, fileInput)
    open(fileOutput, 'wb').write(rembg.remove(open(fileInput, 'rb').read()))