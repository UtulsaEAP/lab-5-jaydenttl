''' 
Name: Jayden Ly
Lab Time: thurs 12:09 PM

def fibonacci(n):
    if n > 0:
        term = 0
        newterm = 1
        for _ in (0, n + 1):
            term, newterm = newterm, term + newterm
            return newterm
        
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    else:
          return -1
'''
def fibonacci(n):
    if n > 1:
        old, new = 0, 1
        for _ in range(2, n + 1):
            old, new = new, old + new
        return new
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return -1


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')