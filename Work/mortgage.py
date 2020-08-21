# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    months = months + 1 
    if principal - payment <= 0:
        principal = 0
        total_paid = total_paid + (payment - principal)
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
    
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal - extra_payment

    print(f'M: {months} T: {round(total_paid,2)} D: {round(principal, 2)}')
    

print(f'Total paid ${round(total_paid, 2)}')
print(f'Total months: {months}')