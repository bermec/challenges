import sys

def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


if __name__ == '__main__':
    ans = read_series('output.txt')
    print(ans)

