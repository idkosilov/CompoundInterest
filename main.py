"""Case-study #3 Investment report
Developer: Kosilov I.

"""

from prettytable import PrettyTable


def float_format(number):
    return f"{number:.{2}f}"


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def enter_data():
    years = input("Срок размещения капитала (лет): ")
    while not is_number(years):
        print("Неверное значение, введите целое значение.")
        years = input("Срок размещения капитала (лет): ")
    years = int(years)

    capital = input("Начальный капитал ($): ")
    while not is_number(capital):
        print("Неверное значение, введите число.")
        capital = input("Начальный капитал ($): ")
    capital = float(capital)

    interest_rate = input("Процентная ставка (%/мес.): ")
    while not is_number(interest_rate):
        print("Неверное значение, введите число.")
        interest_rate = input("Процентная ставка (%/мес.): ")
    interest_rate = float(interest_rate)

    investments = input("Инвестиционные вливания ($/мес.): ")
    while not is_number(investments):
        print("Неверное значение, введите число.")
        investments = input("Инвестиционные вливания ($/мес.): ")
    investments = float(investments)

    return years, capital, interest_rate, investments


def main():
    years, capital, interest_rate, investments = enter_data()
    for year in range(1, years + 1):
        table = PrettyTable()
        table.field_names = ["Месяц", "Основа инвестиций", "Сумма % за месяц", "Капитал"]
        for month in range(1, 13):
            table.add_row([month, float_format(capital), float_format(capital * interest_rate / 100),
                           float_format(capital * (1 + interest_rate / 100))])
            capital = capital * (1 + interest_rate / 100) + investments
        print(f"{year} год", table, sep="\n")


if __name__ == '__main__':
    main()
