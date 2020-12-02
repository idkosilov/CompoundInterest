from prettytable import PrettyTable


def enter_data():
    years = input("Срок размещения капитала (лет): ")
    while not years.isdigit():
        print("Неверное значение, введите целое значение.")
        years = input("Срок размещения капитала (лет): ")
    years = int(years)
    capital = input("Начальный капитал ($): ")
    while not capital.isdigit():
        print("Неверное значение, введите целое значение.")
        capital = input("Начальный капитал ($): ")
    capital = int(capital)
    interest_rate = input("Процентная ставка (%/мес.): ")
    while not interest_rate.isdigit():
        print("Неверное значение, введите целое значение.")
        interest_rate = input("Процентная ставка (%/мес.): ")
    interest_rate = int(interest_rate)
    investments = input("Инвестиционные вливания ($/мес.): ")
    while not investments.isdigit():
        print("Неверное значение, введите целое значение.")
        investments = input("Инвестиционные вливания ($/мес.): ")
    investments = int(investments)
    return years, capital, interest_rate, investments


def main():
    years, capital, interest_rate, investments = enter_data()
    for year in range(1, years + 1):
        table = PrettyTable()
        table.field_names = ["Месяц", "Основа инвестиций", "Сумма % за месяц", "Капитал"]
        for month in range(1, 13):
            table.add_row([month, capital, capital*interest_rate/100, capital*(1+interest_rate/100)])
            capital = capital * (1 + interest_rate / 100) + investments
        print(f"{year} год", table, sep="\n")


if __name__ == '__main__':
    main()
