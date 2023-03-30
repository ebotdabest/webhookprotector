import requests as r
import webbrowser

url = input("Url>>  ")
prompt = input("Prompt>> ")
steps = input("Steps>>  ")


urlxdxd = url[::-1].replace("/"[::-1], ""[::-1], 1)[::-1]

base = urlxdxd + "/createv4"

data = r.get(base, headers={
    "prompt": prompt,
    "steps": str(steps)
}).text

full = urlxdxd + data.replace(".", "", 1)

webbrowser.open(full)