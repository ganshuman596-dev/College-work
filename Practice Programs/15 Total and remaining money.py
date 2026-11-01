'''Problem Statement: A student has a certain amount of money and wants to buy notebooks.
                      Each notebook cost ₹35. Given the amount of money available 
                      calculate-
                      1)Max number of notebooks that can be purchased
                      2)Remaining money'''

balance = int(input("Enter the money you have: "))
nb_price = 35

nb = balance//35
remain = balance%35

print(f'The max number notebooks that can be purchased: {nb}')
print(f'Remaining money: ₹{remain}')