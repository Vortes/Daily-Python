def find_factors(num):
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
    return factors


def remove_duplicates(input):
    final_list = []
    for i in input:
        if i not in final_list:
            final_list.append(i)
    return final_list


def merge_the_tools(string, k):
    # bad naming due to consistency for hackerranks problem
    n = len(string)
    k = max(find_factors(n))
    equal_parts = int(n/k)
    dummy_ti = []
    ti = []
    ui = []

    for t in range(0, n, equal_parts):
        dummy_ti.append(string[t:t + equal_parts])
    
    for t in range(len(dummy_ti)):
        ti.append(list(dummy_ti[t]))

    for i in range(len(ti)):
        ui.append(remove_duplicates(ti[i]))
    
    for i in range(len(ui)):
        if i == 0:
            pass
        else:
            print()
        for j in range(len(ui[i])):
            print(ui[i][j], end='')
    
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)