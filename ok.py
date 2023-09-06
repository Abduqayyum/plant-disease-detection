import requests

url = "http://127.0.0.1:5000/upload/"

with open("/Users/abduqayumrasulmuhamedov/Desktop/license recognition/stb_leaf_schorch.jpeg", "rb") as file:
    files = {"file": file}

    response = requests.post(url, files=files)

if response.status_code == 200:
    print("done")
else:
    print("bad request")