

def format_number(number):
    num_str = str(number)
    length = len(num_str)
    if length <= 3:
        return num_str
    else:
        new_str = ''
        for i in range(length):
            new_str += num_str[i]
            if (length-i-1) % 3 == 0 and (length-i-1) != 0:
                new_str += ','
        return new_str