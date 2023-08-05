# https://github.com/Snakeinweb/T5_1_hw

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
