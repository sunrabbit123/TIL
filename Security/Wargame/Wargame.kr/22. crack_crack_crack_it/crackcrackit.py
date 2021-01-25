import itertools
from passlib.hash import md5_crypt
import time

passwd_section = 'G4HeulB'
salt = 'mka3d3YY'
hashed_passwd = 'dkjywXQf7qq6FDue5H2ho1'

alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
success_flag = 0

for I in range(1, 10):
    to_attempt = itertools.product(alpha, repeat= I)
    now = time.strftime("[%H:%M:%S]")
    print(now, "try ... length :", len(passwd_section) + I)

    for attempt in to_attempt:
        val = ''.join(attempt)

        passwd = passwd_section + val
        shadow_passwd = md5_crypt.using(salt = salt).hash(passwd)
        crypted_passwd = shadow_passwd.split("$")[3]

        if crypted_passwd == hashed_passwd :
            now = time.strftime("[%H%M%S]")
            print("-" * 20)
            print(now, "password cracking succes!")
            print("cracked password :", passwd)
            print(f"hash : {crypted_passwd}")
            print("-" * 20)
            success_flag = 1
            break
    if success_flag == 1:
        break

