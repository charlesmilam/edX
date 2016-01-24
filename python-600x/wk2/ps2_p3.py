balance = 999999
annualInterestRate = 0.18
monthly_interest_rate = annualInterestRate / 12
lower_bound = balance / 12
upper_bound = balance * (1 + monthly_interest_rate)**12 / 12.0
diff = .01

def test_fixed_pay(payment, bal):
    for month in range(1, 13):
        monthly_upaid_bal = bal - payment
        bal = monthly_upaid_bal + (monthly_interest_rate * monthly_upaid_bal)

    return bal

while True:
    fixed_pay = (lower_bound + upper_bound) / 2

    if abs(test_fixed_pay(fixed_pay, balance)) <= diff:
        print 'Lowest Payment: ' + str(round(fixed_pay, 2))
        break
    elif test_fixed_pay(fixed_pay, balance) > diff:
        lower_bound = fixed_pay

    elif test_fixed_pay(fixed_pay, balance) < diff:
        upper_bound = fixed_pay
