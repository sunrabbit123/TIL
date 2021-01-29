import hashlib

for i in range(0, 1000000):
    if b"'='" in hashlib.md5(str(i).encode()).digest():
        print('Found : {i}')
        print(hashlib.md5(str(i).encode()).digest())
        