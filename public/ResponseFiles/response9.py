

# This is a really complicated python script over 100 lines long

# imports
import math
import random

# global variables
num_list = []
max_num = 0

# function to generate a list of random numbers
def generate_random_numbers(length):
    global num_list
    for i in range(length):
        num_list.append(random.randint(1, 100))

# function to find the maximum number in the list
def find_max_num():
    global num_list
    global max_num
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num

# function to calculate the mean of the list
def calculate_mean():
    global num_list
    total = 0
    for num in num_list:
        total += num
    mean = total / len(num_list)
    return mean

# function to calculate the median of the list
def calculate_median():
    global num_list
    num_list.sort()
    if len(num_list) % 2 == 0:
        mid_index_1 = int(len(num_list) / 2) - 1
        mid_index_2 = mid_index_1 + 1
        median = (num_list[mid_index_1] + num_list[mid_index_2]) / 2
    else:
        mid_index = int(len(num_list) / 2)
        median = num_list[mid_index]
    return median

# function to calculate the standard deviation of the list
def calculate_std_dev():
    global num_list
    mean = calculate_mean()
    total_squared_diff = 0
    for num in num_list:
        diff = num - mean
        diff_squared = diff ** 2
        total_squared_diff += diff_squared
    variance = total_squared_diff / len(num_list)
    std_dev = math.sqrt(variance)
    return std_dev

# function to print the results
def print_results():
    global num_list
    global max_num
    mean = calculate_mean()
    median = calculate_median()
    std_dev = calculate_std_dev()
    print("The maximum number in the list is:", max_num)
    print("The mean of the list is:", mean)
    print("The median of the list is:", median)
    print("The standard deviation of the list is:", std_dev)

# main function
def main():
    length = int(input("Enter the length of the list: "))
    generate_random_numbers(length)
    find_max_num()
    print_results()

# call main
main()