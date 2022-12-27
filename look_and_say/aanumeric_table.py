def look_and_say_numeric(start_variable):
    start_variable = int(input("Enter Start variable: "))

    digit_list = [int(digit) for digit in str(start_variable)]

    print(digit_list)
    digit_list.append(-1)    # to handle the index out of bound case in the for loop
    new_number = []

    count = 0
 # first counting the number from left them print the number from right most of the same set till different number occurs next
    for x in range(len(digit_list)):
        if digit_list[x] == digit_list[x+1 if x+1 < len(digit_list) else -1]:
            count= count+1
            continue
        else:
            print(digit_list[x])
            new_number.append(count+1)
            new_number.append(digit_list[x])
            count=0

    string_number1 = ""
    string_number = [string_number1+str(x) for x in new_number]
    print(new_number)



# 22111311
# 22311321
