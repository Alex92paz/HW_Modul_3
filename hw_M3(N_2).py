from random import randint

def get_numbers_ticket(min, max, quantity):

    result_array = set()
    while len(result_array) != quantity:
        result_array.add(randint(min, max))

    return (sorted(list(result_array)))

lottery_numbers = get_numbers_ticket ( 1 , 49, 6)
print(f"Ваши лотерейные числа:, {lottery_numbers}")