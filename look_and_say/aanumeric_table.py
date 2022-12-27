def look_and_say_numeric(start_variable):

    digit_list = [int(digit) for digit in start_variable]
 
    digit_list.append(-1)    # to handle the index out of bound case in the for loop
    new_number = []
    count = 0

    # first counting the number from left them print the number from right
    # most of the same set till different number occurs next
    for x in range(len(digit_list)):
        if digit_list[x] == digit_list[x +1 if x + 1 < len(digit_list) else -1]:
            count = count + 1
            continue
        else:
            new_number.append(count + 1)
            new_number.append(digit_list[x])
            count = 0
 
    string_list = [str(x) for x in new_number]
    string_number = ''.join(string_list)
 
    return string_number
 
if __name__ == "__main__":
    start_variable = input("Enter Start variable: ")
    gen_count = int(input("Enter number of times: "))
 
    # Define the list of numbers
    new_numbers = []
 
    x = start_variable
    for i in range(gen_count):
        new_numbers.append(x)
        x = look_and_say_numeric(x)
 
    print(new_numbers)
  
# 22111311
# 22311321