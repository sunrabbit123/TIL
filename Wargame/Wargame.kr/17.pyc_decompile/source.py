import time
from sys import exit
from hashlib import sha512





if __name__ == '__main__':
    time_minus = 240#local time - server time
    now = time.localtime(time.time() + {time_minus})
    seed = time.strftime('%m/%d/HJEJSH', time.localtime()).encode('utf-8')
    hs = sha512(seed).hexdigest()
    start = now.tm_hour % 3 + 1
    end = start * (now.tm_min % 30 + 10)
    ok = hs[start:end]
    print(ok)

# okay decompiling bughela.pyc
    