'''
https://www.hackerrank.com/challenges/symmetric-difference/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
'''


if __name__ == "__main__":
    m = int(input().strip())
    set_m = set(map(int, input().strip().split()))
    
    n = int(input().strip())
    set_n = set(map(int, input().strip().split()))
    
    sym_diff = set_m.symmetric_difference(set_n)
    
    for value in sorted(sym_diff):
        print(value)
