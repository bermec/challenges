
input1 = ''' 0 0 20 20 20 20 20 20 20 20 20 20 30 30 30 30 30 30 30 30 30 30 40 40 40 40
 40 40 40 40 40 40 50 50 50 50 50 50 50 50 50 50 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0'''
#input2 = '''0 0 30 30 30 30 30 30 30 30 30 30 40 40 40 40 40 40 40 40 40 40 5050 50 50
#50 50 50 50 50 50 60 60 60 60 60 60 60 60 60 60 100 120 140 160 200 10 10 10 10 10 10
#10 10 10 10 10 10 10 10 10 10 10 10 10 10'''


def calc_loan(input2):
    input2, bal, income_repay, clawback_repay = map(int, input2.split()), 0, 0, 0
    royalty_rate = .2
    for i, j in enumerate(input2):
        if i + 18 == 65:
            royalty_rate = .4

        bal = bal * 1.02 + 15
        #print('bal ', bal)
        jay = j * royalty_rate
        print('inc * roy_rate ', jay)
        income_repay += min(jay, bal)
        #print('inc_repay ', income_repay)
        bal = max(bal - j * royalty_rate, 0)
        #print('bal ', bal)
        clawback_repay += min((15 * (bal > 100)) * royalty_rate, bal)
        #print('claw ', clawback_repay)
        bal = max(bal - (15 * (bal > 100)) * royalty_rate, 0)
        #print('bal after ', bal)
        print(i, j, clawback_repay, bal, jay)
        print()




calc_loan(input1)
#calc_loan(input2)

print('{:34s} ${:g}'.format('Overall loan taken:', 15 * len(input1)))
print ('{:34s} ${:g}'.format('Repayments from income:', income_repay))
print ('{:34s} ${:g}'.format('Repayments from benefit clawbacks:', clawback_repay))
print ('{:34s} ${:g}'.format('Ending balance with interest:', bal))
print('-' * 20)