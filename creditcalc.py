import math
import argparse
import sys
parser = argparse.ArgumentParser(description='Calculate credit details')
parser.add_argument('--type', type=str, help='Determines type of payments')
parser.add_argument('--principal', type=int, help='Principal of credit')
parser.add_argument('--payment', type=int, help='Value of payment')
parser.add_argument('--interest', type=float, help='Credit interest')
parser.add_argument('--periods', type=int, help='Number of periods')
args = parser.parse_args()
argm = sys.argv

def diff_month_payment(type, principal, periods,interest):
    i  = args.interest / 1200
    ind = 1
    overpayment = 0
    while ind <= args.periods:
        D = args.principal / args.periods + i * (args.principal - (args.principal * (ind - 1) / args.periods))
        print('Month ' + str(ind) + ': paid out ' + str(math.ceil(D)))
        ind = ind + 1
        overpayment += math.ceil(D)
    statement = ("\nOverpayment = " + str(overpayment - principal))
    return statement

def annuity_payment(type, pricnipal, periods, interest):
    i = args.interest / 1200
    ann_payment = (args.principal * i * (1 + i)**args.periods) /((1 + i)**args.periods - 1)
    overpayment_2 = math.ceil(ann_payment) * args.periods - args.principal
    print("Yout annuity payment = " + str(math.ceil(ann_payment)) + "!")
    statement_2 = ("Overpayment = " + str(overpayment_2))
    return statement_2
def principal_calc(type, payment, periods, interest):
    i = args.interest / 1200
    credit_principal = args.payment / ((i * (1 + i)**args.periods)/((1 + i)**args.periods-1))
    print("Your credit principal = " + str(math.floor(credit_principal)) +"!")
    overpayment_3 = ("Overpayment = " + str(args.payment * args.periods - math.floor(credit_principal)))
    return overpayment_3

def how_many_months(type, principal, payment, interest):
    i = args.interest / 1200
    number_of_months = math.log((args.payment)/(args.payment - i * args.principal), (1 + i))
    months_rounded = math.ceil(number_of_months)
    if months_rounded % 12 == 0:
        x = months_rounded / 12
        print("You need ", int(x), "years to repay this credit!")
    elif months_rounded < 12:
        print("You need ", months_rounded, "months to repay this credit!")
    else:
        years = months_rounded // 12
        months = months_rounded % 12
        print("You need ", years, "years and ", months, "months to repay this credit!")
    return("Overpayment = " + str(math.ceil(months_rounded * args.payment - args.principal)))


if len(sys.argv) != 5:
    print("Incorrect parameters")
elif args.type == "diff" and not args.payment:
    print(diff_month_payment(args.type, args.principal, args.periods, args.interest))
elif args.type == "annuity" and not args.payment:
    print(annuity_payment(args.type, args.principal, args. periods, args.principal))
elif args.type == "annuity" and not args.principal:
    print(principal_calc(args.type, args.payment, args.periods, args.interest))
elif args.type == "annuity" and not args.periods:
    print(how_many_months(args.type, args.principal, args.payment, args.interest))
else:
    print("Incorrect parameters")
