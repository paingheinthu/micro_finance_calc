#!/usr/bin/python
import sys
import argparse

def calculate_loan_interest(month, loan_amt, interest_rate):
    per_m_i = 0
    old_m_i = 0
    total_m_i = 0
    
    mnt_paid_amt = round(loan_amt / float(month))
    min_interest = round(mnt_paid_amt * (interest_rate/100))
    
    for i in range(1, month + 1):
        per_m_i = (min_interest * float(i))
        old_m_i =  total_m_i
        total_m_i += per_m_i
        msg = "({0:5} x {1:3}) = {2:10} + {3:10} = {4:10}".format(min_interest, i, per_m_i, old_m_i, total_m_i)
        print msg
        
    print "\n"
    print "One Month Paid = %i" % mnt_paid_amt
    print "TOTAL interest = %i" % total_m_i
    print "One Month paid interest = %i" % (total_m_i / month)
    print "Total paid per one month = %i" % ( (total_m_i/month) + mnt_paid_amt )
    
def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--month", help="payment month", required=True, type=int)
    parser.add_argument("-l", "--loan", help="loan amount", required=True, type=int)
    parser.add_argument("-i", "--interest", help="interest persent", required=True, type=float)
    args = parser.parse_args()
    return (parser, args)
 

if __name__=="__main__":
    (parser, args) = setup_args()

    mnt = args.month
    loan_amt = args.loan
    interest_rate = args.interest
    
    calculate_loan_interest(mnt, loan_amt, interest_rate)


