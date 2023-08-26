# word = "100110011110111010110111001011011110101"
# word1 = "1001100111101110"
# decimal = int(word,2)
# hexa = hex(decimal)[2:]
#
# # hex_to_binary = bin(hexa)
# print(decimal)
# print(len(bin(int(hexa,16))[2:]))
# print(len(hexa))
# # print(hex_to_binary)

import base64

binary_string = "100110011110111010110111001011011110101000"

# Add padding if needed
padding = (3 - len(binary_string) % 3) % 3
binary_string += '0' * padding

binary_bytes = bytes(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))

base64_encoded = base64.b64encode(binary_bytes).decode()

base64_back = base64.b64decode(base64_encoded)
binary_back = ''.join(bin(byte)[2:].rjust(8, '0') for byte in base64_back)[:len(binary_string)]  # Adjust length

print("Original Binary String:", binary_string)
print("Base64 Encoded:", base64_encoded)
print("Decoded Binary String:", binary_back)

print("Is binary_string same as decoded binary_back?", binary_string == binary_back)




# def base64_encoding(binary_string):
#     binary_bytes = bytes(int(binary_string[i:i + 8], 2) for i in range(0, len(binary_string), 8))
#     base64_encoded = base64.b64encode(binary_bytes).decode()
#
#     return  base64_encoded
#
#
# print(base64_encoding("1001100111101110101101110010110101110101"))



