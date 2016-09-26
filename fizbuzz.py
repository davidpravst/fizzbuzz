# -*- coding: utf-8 -*-

"""
Smartninja Web Development 1 / Pogoji in zanke
Domača naloga 8.2: FizzBuzz
Uporabnik naj vnese število med 1 in 100
Program naj začne šteti do te izbrane številke (in izpiše vsako številko v terminalu).
V primeru da je številka deljiva s 3, naj namesto številke v terminalu izpiše "fizz".
V primeru da je številka deljiva s 5, naj namesto številke v terminalu izpiše "buzz".
V primeru da je številka deljiva tako s 3, kot s 5, naj namesto številke v terminalu izpiše "fizzbuzz".
"""

stevilo = int(raw_input("Vnesi število med 1 in 100: "))

stevec = 1

while stevec <= stevilo:
    if stevec%3==0 and stevec%5==0:
        print "fizzbuzz"
    elif stevec%3 == 0:
        print "fizz"
    elif stevec%5 == 0:
        print "buzz"
    else:
        print stevec
    stevec = stevec + 1
