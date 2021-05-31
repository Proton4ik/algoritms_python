def rotate(num):
    return str(num) if num < 10 else str(num % 10) + rotate(num // 10)


number = 1230
print (rotate(number))
