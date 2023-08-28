# from decimal import Decimal
#
# def convert_binary_to_Decimal(binary_string:str):
#     binary_string = binary_string.lstrip('0')
#     binary_string = list(binary_string[::-1])
#
#     indices = []
#     for index, value in enumerate(binary_string):
#         if value == '1':
#             indices.append(index)
#
#     sum = Decimal(0)
#     for n in indices:
#         sum = sum + Decimal(2)**n
#
#
#     print(sum)
#
# convert_binary_to_Decimal('11001')

import base64

def base64_encoding(binary_string):
    padding = (6 - len(binary_string) % 6) % 6
    adjusted_binary = '0' * padding + binary_string
    binary_bytes = bytes(int(adjusted_binary[i:i + 6], 2) for i in range(0, len(adjusted_binary), 6))
    base64_encoded = base64.b64encode(binary_bytes).decode()

    return base64_encoded

print(base64_encoding('11'))