def look_and_say_numeric(start_variable):
    start_variable = int(input("Enter Start variable: "))
    # first to count the number from right them print the number from right

    digit_list = [int(digit) for digit in str(start_variable)]

    print(digit_list)
    digit_list.append(-1)
    new_number = []

    count = 0

    for x in range(len(digit_list)):
        if digit_list[x] == digit_list[x+1 if x+1 < len(digit_list) else -1]:
            count= count+1
            continue
        else:
            print(digit_list[x])
            new_number.append(count+1)
            new_number.append(digit_list[x])
            count=0


    print(new_number)



# 22111311
# 22311321
