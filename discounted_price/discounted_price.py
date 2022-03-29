# 할인가 계산하기

def discount(price, percent):
    percent = percent/100
    return price*(1 - percent)

price = float(input('가격?? '))
percent = float(input('할인율 '))

print(discount(price, percent))