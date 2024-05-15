import requests
from wikipedia import wikipedia

# Assuming other parts of your code remain unchanged
query = "Python (programming language)"
page = wikipedia.page(query)
image_link = page.images[1]

print(page.images[0])
print(page.images[1])
print(page.images[2])

# Use the obtained User-Agent string
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

req = requests.get(image_link, headers=headers)

print("Image Link:", image_link)
print("Status Code:", req.status_code)
print("Content Length:", len(req.content))

# Save the image content to a file
#print(req.content)
#print(req._content)

with open('files/image.jpg', 'wb') as f:
    f.write(req.content)