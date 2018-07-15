'''Unconditional Loan Income is a private or public (social) program that uses
"soft loans" whose only repayment obligation is a royalty on future income.

Special considerations for core/simple test are:

    An automatic clawback (to repay previous loans) of new social loans takes
    place when the total outstanding balance exceeds a threshold cap.
    A higher royalty rate applies when recipient's age is 65 or higher, and
    applies for both income and new ULI loans.

When repayments are made, the first loan in queue (first loan taken out) is
repaid with the payment. Special considerations for bonus are:

    once repayments for a loan exceed (or equal) the principal amount, interest
    stops accruing,
    there is a total repayment cap of 2x the principal for any loan (once cap
    is reached,
    there may be a social guarantor for the loans, which will repay up to the
    loan principal upon the borrower's death.

sample test

Given an interest rate, annual loan amount, starting age, royalty rate under
    age 65, clawback balance trigger, royalty rate over 65 and an annual
    (assumed) income stream, calculate total repayments and profit or loss:
sample input

interest rate: 2%
annual loan amount: $15000
start age: 18
clawback balance trigger: $100000
royalty rate (under 65): 20%
royalty rate (over 65): 40%
income stream: (in thousands)

 0 0 20 20 20 20 20 20 20 20 20 20 30 30 30 30 30 30 30 30 30 30 40 40 40 40
    40 40 40 40 40 40 50 50 50 50 50 50 50 50 50 50 0 0 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

sample output (in thousands)

Overall loans taken: $1080
Repayments from income: $280
Repayments from benefit clawbacks: $270
Ending balance with interest: $1169.09
input #2

interest rate: 2%
annual loan amount: $15000
start age: 18
clawback balance trigger: $100000
royalty rate (under 65): 20%
royalty rate (over 65): 40%
income stream: (in thousands)

 0 0 30 30 30 30 30 30 30 30 30 30 40 40 40 40 40 40 40 40 40 40 50 50 50 50
 50 50 50 50 50 50 60 60 60 60 60 60 60 60 60 60 100 120 140 160 200 10 10
 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10

output #2 (in thousands)

Overall loans taken: $1005
Repayments from income: $584
Repayments from benefit clawbacks: $237
Ending balance with interest: $509.487
'''

def ULI_calc(l):
    balance = 0
    annual_loan = 15
    clawback = 0
    int_rate = 0.02
    income_repayment = 0
    salary = list(enumerate(l, 18))

    for i, j in (salary):
        j = int(j)
        if 18 <= i <= 64:
            royalty_rate = 0.2
        else:
            66 <= i <= 100
            royalty_rate = 0.4
        balance = balance + ((balance) * int_rate)
        balance += annual_loan
        liable = j * royalty_rate
        income_repayment += min(balance, liable)
        balance = max(balance - j * royalty_rate, 0)
        clawback += min((15 * (balance > 100)) * royalty_rate, balance)
        balance = max(balance - (15 * (balance > 100)) * royalty_rate, 0)
    return (balance, income_repayment, clawback, annual_loan, royalty_rate)





if __name__ == '__main__':
    income = ''' 0 0 20 20 20 20 20 20 20 20 20 20 30 30 30 30 30 30 30 30 30 30 40 40 40 40
     40 40 40 40 40 40 50 50 50 50 50 50 50 50 50 50 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
     0 0 0 0 0 0 0 0 0 0'''
    # income2 = '''0 0 30 30 30 30 30 30 30 30 30 30 40 40 40 40 40 40 40 40 40 40 5050 50 50
    # 50 50 50 50 5050 60 60 60 60 60 60 60 60 60 60 100 120 140 160 200 10 10 10 10 10 10 10
    # 10 10 10 10 10 10 10 10 10 10 10 10 10'''
    income = income.split()
    ans = ULI_calc(income)
    #calc_loan(input2)

    print('{0}{1}'.format('Overall loan taken:', ans[3] * len(income)))
    print('{0}{1}'.format('Repayments from income:', ans[1]))
    print('{0}{1}'.format('Repayments from benefit clawbacks:', ans[2]))
    print('{0}{1}'.format('Ending balance with interest:', round(ans[0], 2)))
