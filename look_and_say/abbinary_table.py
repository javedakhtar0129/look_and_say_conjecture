# This is where we'll build our binary look and say algo
import pandas as pd


def look_and_say_numeric(start_variable):
    digit_list = [int(digit) for digit in start_variable]

    digit_list.append(-1)  # to handle the index out of bound case in the for loop
    new_number = []
    count = 0

    # first counting the number from left them print the number from right
    # most of the same set till different number occurs next
    for x in range(len(digit_list)):
        if digit_list[x] == digit_list[x + 1 if x + 1 < len(digit_list) else -1]:
            count = count + 1
            continue
        else:
            new_number.append(bin(count + 1)[2:])    # to convert counted number into Binary
            new_number.append(digit_list[x])
            count = 0

    string_list = [str(x) for x in new_number]
    string_number = ''.join(string_list)

    return string_number


def count_digits(number):
    digit_count = {
        "Number": number
    }

    for i in number:
        if i in digit_count:
            digit_count[i] += 1
        else:
            digit_count[i] = 1
    return digit_count


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

    # Create an empty list to store the dictionaries for each number
    data = []

    # Iterate over the list of numbers
    for n in new_numbers:
        digit_count = count_digits(n)
        data.append(digit_count)

    df = pd.DataFrame(data)

    print(df)
    df.to_csv('output_binary.csv')

# 22111311
# 22311321