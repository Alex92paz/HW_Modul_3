from datetime import datetime

def get_days_from_today(date):
    current_date = datetime.today().date()
    try:
        start_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("You entered an invalid date! Please try again.")
        try:
            date = input("Enter the date in the format YYYY-MM-DD: ")
            start_date = datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            print("You entered an invalid date again!")
            return None  # Return None if the second input is also invalid

    delta = (current_date - start_date).days
    return delta

result = get_days_from_today(input("Enter the date in the format YYYY-MM-DD: "))
if result is not None:
    print(f"{result} days")
