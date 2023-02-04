# This is where we'll build our binary look and say algo
from save_csv import save_to_csv


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

def compute_ratio(ones: int, zeros: int) -> float | None:
    if zeros == 0:
        return None
    else:
        return ones/zeros


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
        number = {
            'number': n,
            'lenght':len(n),
            '1 count':n.count("1"),
            '0 count':n.count("0"),
            'Ratio 1/0':  compute_ratio(n.count("1"),n.count("0"))
        }

        data.append(number)


    save_to_csv(data)

# 22111311
# 22311321