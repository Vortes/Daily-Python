def find_factors(num):
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
    return factors

def merge_the_tools(string, k):
    # bad naming due to consistency for hackerranks problem
    n = len(string)
    k = max(find_factors(n))
    equal_parts = int(n/k)
    ti = []
    ui = []

    for t in range(0, n, equal_parts):
        ti.append(string[t:t + equal_parts])
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)