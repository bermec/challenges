def deficient(num):
    divisors_sum = sum(find_divisors(num))
    deficiency = (2 * num) - divisors_sum
    if deficiency < 0:
        return '{0} abundant by {1}'.format(num, abs(deficiency))
    elif deficiency > 0:
        return '{0} deficient'.format(num)
    else:
        return 'neither'



def find_divisors(num):
    return [x for x in range(1, num + 1) if num % x == 0]

if __name__ =='__main__':

    ans = deficient(18)
    print(ans)