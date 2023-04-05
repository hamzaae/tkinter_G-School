import hashlib


with open('New Text Document.txt','a') as f:
    f.write(hashlib.sha256('tkinterPassword123'.encode()).hexdigest())
