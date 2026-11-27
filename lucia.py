import requests

url = "https://dog.ceo/api/breeds/list/all"
resp = requests.get(url)
data = resp.json()

razas = []

print("- Lista de razas disponibles -")
for raza, subraza in data["message"].items():
    razas.append(raza)
for raza in razas:
    print(raza)
print("---------------")
perro = input("Introduce la raza para contar sus imágenes: ")
if perro not in razas:
    print("No existe esa raza")
else:
    url_img = f"https://dog.ceo/api/breed/{perro}/images"
    imgs = requests.get(url_img)
    data_img = imgs.json()
    cantidad = len(data_img["message"])
    print(f"{perro} - {cantidad} fotos")

print("---------------")

perro = input("Introuduce la raza para ver las subrazas: ")
subrazas = data["message"][perro]

if perro not in razas:
    print("No existe esa raza")
else:
    if subrazas:
        for subraza in subrazas:
            print(f"{subraza}")
    else:
        print(f"No existen subrazas para {perro}")

print("---------------")

perro = input("Introduce la raza para ver una imagen: ")

if perro not in razas:
    print("No existe esa raza")
else:
    url_img = f"https://dog.ceo/api/breed/{perro}/images/random"
    imgs = requests.get(url_img)
    data_img = imgs.json()

    print(data_img["message"])
