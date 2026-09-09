sales=[100000,120000,50000,110000,115000,1000000]

march_month_sales=sales[2]    #display march month sales

print(march_month_sales)

#update may month sales as 10500
sales[4]=10500
print(sales)


print("display all sales using index")
for i in range(0,len(sales)):

    print(sales[i])


print("display sales>100000")
for amount in sales:

    if amount>100000:

        print(amount)
