"""Case-study #3 Investment report
Developer: Kosilov I.

"""


def make_table(data):
    table = "+-----------------------+-----------------------------------+" \
             "-----------------------------------+-----------------------+\n"
    table += "|\t" + '\t\t\t\t|\t'.join(["Месяц", "Основа инвестиций", "Сумма % за месяц", "Капитал"]) + "\t\t\t\t|\n"
    table += "+-----------------------+-----------------------------------+" \
             "-----------------------------------+-----------------------+\n"
    for row in data:
        table += f"|\t{row[0]}{(4*4+4-len(row[0]))*' '}|" \
                 f"\t{row[1]} ${(4*4+14-len(row[1]))*' '}|" \
                 f"\t{row[2]} ${(4*4+14-len(row[2]))*' '}|" \
                 f"\t{row[3]} ${(4*4+2-len(row[3]))*' '}|\n"
    table += "+-----------------------+-----------------------------------+" \
             "-----------------------------------+-----------------------+\n"
    return table


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
        data = []
        for month in range(1, 13):
            data.append([str(month), float_format(capital), float_format(capital * interest_rate / 100),
                         float_format(capital * (1 + interest_rate / 100))])
            capital = capital * (1 + interest_rate / 100) + investments
        print(f"{year} год", make_table(data), sep="\n")


if __name__ == '__main__':
    main()
