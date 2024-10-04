actualCost= float(input('Please enter the actual product price-'))

saleAmount=float(input('Please enter the sales amount'))

if saleAmount>actualCost:
    amount=saleAmount-actualCost
    print('Total profit=', amount)
else: 
    print("No profit")

 


