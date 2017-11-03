
''' A module for demonstrating exceptions'''
import sys

def convert(s):
    '''Convert to an integer'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print('Conversion error: {}'
            .format(str(e)),
            file=sys.stderr)
        raise


if __name__ == '__main__':
    ans = convert('["rt"]')
    print(ans)
    ans = convert('9')
    print(ans)

    

