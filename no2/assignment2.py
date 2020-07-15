"""
4) Write a program that takes a list of ten prices and ten products,
 applies an 11% discount to
each of the prices displays the output like below, right-justified and nicely formatted.
Apples # 2.45
Oranges # 18.02
...
Pears #120.03

"""
prices = []
products = []

for i in range(3):
    product = input("please input product : ") 
    price = eval(input("please input price : "))
    calculating_discount = ((11/100)*(price/1))
    discount = (price)- (calculating_discount)
    add_price = prices.append(discount)
    add_product = products.append(product)

for p in prices:
    print()
    for x in products:
        print()