# a Python program to calculate mortgage payments and mortgage costs
# tested with Python24 by      vegaseat      04jun2006

# give total loan
principal = 417000.0
# give annual percent interest
percent_interest = 3.75
# give length of mortgage
years = 15
# calculate total number of payments
payment_number = years * 12

# calculate monthly interest rate
monthly_interest = percent_interest/(100 * 12)
monthly_payment = principal * ( monthly_interest / (1 - (1 + monthly_interest) ** (- payment_number)))

print "Total loan = $%0.2f" % principal
print "Interest   = %0.2f%s" % (percent_interest, "%")
print "Years      = %0.f" % years
print "Number of payments = %0.f" % payment_number
print "Monthly Payment amount = $%0.2f" % monthly_payment

print "-"*60

print "Total cost     = $%0.2f" % (payment_number * monthly_payment)
print "Total interest = $%0.2f" % (payment_number * monthly_payment - principal)

print "-"*60

# give payments made
payments = 100

rem_principal = principal * (1 - ((1 + monthly_interest) ** payments - 1) / ((1 + monthly_interest) ** payment_number - 1))

print "The outstanding principal after %d payments is $%0.2f" % (payments, rem_principal)
print "At this point you have paid a total of $%0.2f" % (monthly_payment * payments)

#Amortization table
print "Amortization table"
print "payment_number\tpaid interest\tpaid principal\tremaining principal" 
prepayment = 500
print "Monthly Payment amount with $500 prepayment = $%0.2f" % (monthly_payment+prepayment)
remaining_principal = principal
total_interest = 0
for i in range(1,payment_number+1):    
    pi = remaining_principal * monthly_interest
    pp = monthly_payment - pi + prepayment    
    remaining_principal -= pp        
    if remaining_principal < 0:
        pi = (remaining_principal+pp) * monthly_interest
        total_interest+=pi
        pp = remaining_principal+pp - pi
        print "%d\t%0.2f\t%0.2f\t%0.2f" % (i, pi, pp, 0)        
        break    
    print "%d\t%0.2f\t%0.2f\t%0.2f" % (i, pi, pp, remaining_principal)
    total_interest+=pi

print "Monthly prepayment $%0.2f, Monthly total payment $%0.2f" % (prepayment, monthly_payment + prepayment)   
print "Total interest paid $%0.2f" % (total_interest)
y = i/12
print "Payoff the loan in %d years %d months" % (y, i-12*y)

#effective rate
import scipy.optimize
def monthlypayment(x, mp, n):
    return mp - x/(1-(1+x)**(-n))
 
actual_payment_number = i
actaul_monthly_payment = monthly_payment + prepayment
effective_rate = scipy.optimize.brentq(monthlypayment, 0.00001, 5, args=(actaul_monthly_payment/principal,actual_payment_number))

#print principal * effective_rate/(1-(1+effective_rate)**(-actual_payment_number)), actaul_monthly_payment
print "Effective rate is: %0.4f" % (effective_rate*12*100) 

 