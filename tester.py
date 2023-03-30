import requests as r

base = "http://d300-34-87-118-14.ngrok.io"

url = base + "/createv4"

data = r.get(url, headers={"prompt": "Welcome to the internet."})

print(str(base + data.text))

