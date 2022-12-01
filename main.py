
import os
import openai

from rembg import remove

openai.organization = "org-7GHrzPrQec6Q9QGVWpfDG3yC"
openai.api_key = "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"
openai.Model.list()

response = openai.Image.create(
    prompt="3D representation of a AIDS virus with a stickman body, 8-bit style red palette",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)