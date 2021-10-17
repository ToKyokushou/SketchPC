import base64

def convert(img_string):
    img_data = base64.b64decode(img_string)
    t = open('1.png','wb')
    t.write(img_data)
    t.close()

img_string = 'iVBORw0KGgoAAAANSUhEUgAABZYAAAIfCAYAAADjdomZAAAAAXNSR0IArs4c6QAAIABJREFUeF7s3Q/sbvd9F/b32VhIO5gdmkmMktj8mVoxBTtIXTbSzL5UHYUJ2Q5a61XV7DvaakMM24jGhk3NvSsBmxRir9q0P5F8M6ZORjSxGUilkxJ7eBuEqXFKJMqoGqdhBdHSxiokpUM60+c+5wnHT3+/3/Oc3+/5c/68jvLTje/vPN/z/b6+597n/t7P93y+TRwECBAgQIAAAQIECBAgQIAAAQIECBAgQGCAQDPgXKcSIECAAAECBAgQIECAAAECBAgQIECAAIEIlt0EBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAsD+JyMgECBAgQIECAAAECBAgQIECAAAECBAgIlt0DBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAsD+JyMgECBAgQIECAAAECBAgQIECAAAECBAgIlt0DBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAsD+JyMgECBAgQIECAAAECBAgQIECAAAECBAgIlt0DBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAsD+JyMgECBAgQIECAAAECBAgQIECAAAECBAgIlt0DBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAsD+JyMgECBAgQIECAAAECBAgQIECAAAECBAgIlt0DBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAsD+JyMgECBAgQIECAAAECBAgQIECAAAECBAgIlt0DBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAsD+JyMgECBAgQIECAAAECBAgQIECAAAECBAgIlt0DBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAsD+JyMgECBAgQIECAAAECBAgQIECAAAECBAgIlt0DBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAsD+JyMgECBAgQIECAAAECBAgQIECAAAECBAgIlt0DBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAsD+JyMgECBAgQIECAAAECBAgQIECAAAECBAgIlt0DBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAsD+JyMgECBAgQIECAAAECBAgQIECAAAECBAgIlt0DBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAsD+JyMgECBAgQIECAAAECBAgQIECAAAECBAgIlt0DBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAsD+JyMgECBAgQIECAAAECBAgQIECAAAECBAgIlt0DBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAsD+JyMgECBAgQIECAAAECBAgQIECAAAECBAgIlt0DBAgQIECAAAECBAgQIECAAAECBAgQIDBIQLA8iMvJBAgQIECAAAECBAgQIECAAAECBAgQICBYdg8QIECAAAECBAgQIECAAAECBAgQIECAwCABwfIgLicTIECAAAECBAgQIECAAAECBAgQIECAgGDZPUCAAAECBAgQIECAAAECBAgQIECAAAECgwQEy4O4nEyAAAECBAgQIECAAAECBAgQIECAAAECgmX3AAECBAgQIECAAAECBAgQIECAAAECBAgMEhAs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'

convert(img_string)