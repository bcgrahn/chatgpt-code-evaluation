

import itertools

def permutations(string): 
    return list(itertools.permutations(string)) 

def get_permutations(string): 
    if len(string) == 0: 
        return [] 
    if len(string) == 1: 
        return [string] 
    permutation_list = [] 
    for permutation in permutations(string): 
        permutation_list.append(''.join(permutation)) 
    return permutation_list 

if __name__ == "__main__": 
    string = input("Enter a string: ") 
    print(get_permutations(string))