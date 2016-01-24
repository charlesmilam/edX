balance = 9900
annualInterestRate = 0.12
monthly_interest_rate = annualInterestRate / 12.0
fixed_pay = 10

def test_fixed_pay(payment, bal):
    for month in range(1, 13):
        monthly_upaid_bal = bal - payment
        bal = monthly_upaid_bal + (monthly_interest_rate * monthly_upaid_bal)

    return bal

while True:
    if test_fixed_pay(fixed_pay, balance) <= 0:
        print 'Lowest Payment: ' + str(fixed_pay)
        break
    else:
        fixed_pay += 10
        test_fixed_pay(fixed_pay, balance)
