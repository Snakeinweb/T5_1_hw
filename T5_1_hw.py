﻿

x = int(input("Введите любое число: "))
if x > 0 and x % 2 == 0:
    print ("положительное четное число")  
elif x > 0 and x % 2 != 0:
    print ("положительное нечетное число")
elif x < 0 and x % 2 != 0:
    print ("отрицательное нечетное число")
elif x < 0 and x % 2 == 0:
    print ("отрицательное четное число")
else:
    print ("нулевое число")
