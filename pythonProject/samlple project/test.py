'''
Assume you want to build two functions for discounting products on
a website. Function number 1 is for student discount which discounts
the current price to 10%. Function number 2 is for additional discount
for regular buyers which discounts an additional 5% on the current
student discounted price. Depending on the situation, we want to be
able to apply both the discounts on the products. Design the above
two mentioned functions and apply them both simultaneously on 
the price.
'''
def student_discount(price):
    discount_price=0.1
    return price *(1-discount_price)

def regularbuyers_discount(price):
    discount_price=0.05
    return price *(1-discount_price)


actual_price=100
print('student discount=',student_discount(actual_price))
print('regular discount=',regularbuyers_discount(actual_price))
