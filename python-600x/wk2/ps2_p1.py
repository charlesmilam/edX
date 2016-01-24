balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthly_interest_rate = annualInterestRate / 12.0
total_paid = 0

for month in range(1, 13):
    min_payment = balance * monthlyPaymentRate
    monthly_upaid_bal = balance - min_payment
    balance = monthly_upaid_bal + (monthly_interest_rate * monthly_upaid_bal)
    total_paid += min_payment

    print 'Month: ' + str(month)
    print 'Minimum monthly payment: ' + str(round(min_payment, 2))
    print 'Remaining balance: ' + str(round(balance, 2))

print 'Total paid: ' + str(round(total_paid, 2))
print 'Remaining balance: ' + str(round(balance, 2))
