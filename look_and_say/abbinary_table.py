# # This is where we'll build our binary look and say algo
import os
import base64
from save_csv import  save_to_csv,create_csv
from decimal import Decimal


def look_and_say_numeric(start_variable):
    digit_list = [int(digit) for digit in start_variable]

    digit_list.append(-1)  # to handle the index out of bound case in the for loop
    new_number = []
    count = 0

    # first counting the number from left then print the number from right
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


def base64_encoding(binary_string):
    padding = (6 - len(binary_string) % 6) % 6
    adjusted_binary = '0' * padding + binary_string
    binary_bytes = bytes(int(adjusted_binary[i:i + 6], 2) for i in range(0, len(adjusted_binary), 6))
    base64_encoded = base64.b64encode(binary_bytes).decode()

    return base64_encoded


def base64_decoding(base64_encoded):
    decoded_bytes = base64.b64decode(base64_encoded)
    binary_back = ''.join(format(byte, '06b') for byte in decoded_bytes).lstrip('0')

    return binary_back


def convert_binary_to_Decimal(binary_string: str):
    binary_string = binary_string.lstrip('0')
    binary_string = list(binary_string[::-1])

    indices = []
    for index, value in enumerate(binary_string):
        if value == '1':
            indices.append(index)

    sum = Decimal(0)
    for n in indices:
        sum = sum + Decimal(2) ** n

    return sum


if __name__ == "__main__":

    start_variable = input("Enter Start variable: ")
    gen_count = int(input("Enter number of times: "))

    new_numbers = open('new_numbers_temoprary.txt','w')
    x = start_variable
    for i in range(gen_count):
        new_numbers.write("%s\n"%x)
        x = look_and_say_numeric(x)

    new_numbers.close()
    file =  open('new_numbers_temoprary.txt','r')

    save_csv_file_path = create_csv()

    print(save_csv_file_path)

    # Iterate over the list of numbers
    for n in file:

        number = {
            # 'binary': [n.strip()],
            'base64_number': [base64_encoding(n.strip())],
            'decimal_number':[convert_binary_to_Decimal(n.strip())],
            'binary_length':[len(n.strip())],
            '1 count':[n.count("1")],
            '0 count':[n.count("0")],
            'Ratio 1/0':  [compute_ratio(n.count("1"),n.count("0"))]
        }

        # print(number)
        save_to_csv(number,save_csv_file_path)

    file.close()
    os.remove(new_numbers.name)

    #     data.append(number)
    # save_to_csv(data)

# 22111311
# 22311321

