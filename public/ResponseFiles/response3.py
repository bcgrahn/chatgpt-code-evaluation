

# This code takes a list of integers and returns a list of all the prime numbers in the original list

def get_prime_numbers(nums):
    prime_nums = []
    for num in nums:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_nums.append(num)
    return prime_nums