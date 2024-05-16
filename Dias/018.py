'''
https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
'''
def average(array):
    unique_elements = set(array)
    avg = sum(unique_elements) / len(unique_elements)
    return avg