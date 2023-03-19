import string
from random import choice, shuffle

def sifre():
    l = list(string.ascii_lowercase)
    u = list(string.ascii_uppercase)
    d = list(string.digits)
    g = list(string.ascii_letters)
    f = list(string.hexdigits)
    all = l + u + d + g + f
    shuffle(all)

    lenght = int(input("Ne kadar uzun şifre istersin?"))
    password = ''
    for i in range(lenght):
        password += choice(all)
    print(password)

sifre()