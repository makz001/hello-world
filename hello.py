from time import sleep
from os import system
from random import choice

spaces = 0

system ('cls')

while 1:
    sleep (0.1)

    x = choice ([True, False])
    if x:
        spaces +=1
    elif spaces > 0:
        spaces -=1
    for i in range (spaces):
        print (' ', end='')

    print ('hi')
