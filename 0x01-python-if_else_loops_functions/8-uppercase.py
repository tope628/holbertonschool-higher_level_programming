#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
<<<<<<< HEAD
            upper = ord(i) - 32
        else:
            upper = ord(i)
        print("{:s}".format(chr(upper)), end="")
    print('')
=======
            i -= 32
        print("{:s}".format(chr(ord(i)), end='')
  print("")
>>>>>>> f69560c7eecc527b8adac345b876935f1a90c092
