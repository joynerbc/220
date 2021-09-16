"""
Name: Brianna Joyner
interest.py

Problem: This program calculates the monthly interest charge for a given period.

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with tutors at the CSL.
"""

def main():
    annual_apr = eval(input("enter the annual interest rate: "))
    annual_apr /= 100
    billing_cycle = eval(input("enter the number of billing days: "))
    previous_balance = eval(input("enter the previous net balance: "))
    payment = eval(input("enter the payment amount: "))
    cycle_day = eval(input("enter the day of the billing cycle when the payment was made: "))
    step_one = previous_balance * billing_cycle
    days_before_end_cycle = billing_cycle - cycle_day
    step_two = payment * days_before_end_cycle
    step_three = step_one - step_two
    step_four = step_three / billing_cycle
    monthly_interest_rate = annual_apr / 12
    monthly_interest_charge = step_four * monthly_interest_rate
    print(round(monthly_interest_charge, 2))


if __name__ == '__main__':
    main()
