loan = int(input("Input the cost of the item in $: "))
payment = 50.0 
month = 1
vaxtap = 0.02
debt = loan
total_interest = 0

if loan <= 1000:
    vaxtap = 0.015

while debt > 0.00:
    vextir = 0
    vextir = debt*vaxtap
    debt = (debt - (payment - vextir))
    
    print('Month:', month, 'Payment:', round(payment, 2), 'Interest paid:', round(vextir, 2), 'Remaining debt:', round(debt,2))

    month =  month + 1 
    total_interest += vextir

    if debt < payment:
        vextir = debt*vaxtap
        payment = debt + vextir
    
print("")    
print('Number of months:',(month-1))    
print('Total interest paid:',round(total_interest, 2))    


