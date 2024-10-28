from datetime import datetime


def get_days_from_today(date):
    current_date = datetime.today().date()
    start_date = datetime.strptime(date, "%Y-%m-%d").date()
    delta = (current_date - start_date).days
    return delta

resolt = get_days_from_today("2020-10-09")
print(f"{resolt} days")


