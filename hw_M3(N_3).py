import re
list_phone_number = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    " +38(050) 145 33- 00",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11 ",
]


def normalize_phone(list_phone_number):
    
    for num in list_phone_number:

        pattern = r"[\s\-()\n\+]"
        replacement = ""
        formatted_number = re.sub(pattern, replacement, num)

        pattern = r"^38"
        replacement = ""
        formatted_number = re.sub(pattern, replacement, formatted_number)

        pattern = r"^"
        replacement = "+38"
        formatted_number = re.sub(pattern, replacement, formatted_number)
        print(formatted_number)

normalize_phone(list_phone_number)


