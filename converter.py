from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from datetime import datetime

cr = CurrencyRates()
cd = CurrencyCodes()

history = []


def converter(currency1, currency2, money):
    return cr.convert(currency1, currency2, money)


def converter_with_data(currency1, currency2, money, date_obj):
    return cr.convert(currency1, currency2, money, date_obj)


def get_history(history):
    if history == []:
        print('История операций пуста')
        print()
    else:
        for line in history:
            print(line)
        print()


while True:
    print('Если Вы хотите поменять валюту, нажмите Enter')
    print('Если Вы хотите получить историю своих операций, введите "get_history"')
    print('Если Вы хотите завершить программу, введите "quit"')

    read = str(input())
    if read == "get_history":
        get_history(history)

    elif read == "quit":
        print("Программа завершила работу")
        break

    else:
        print('Какую валюту Вы хотели бы поменять?')
        currency_from = str(input())
        while currency_from not in cr.get_rates('USD'):
            print('Кажется, Вы ошиблись. Введите валюту еще раз:')
            currency_from = str(input())

        print('Какую валюту Вы хотели бы получить?')
        currency_to = str(input())
        while currency_to not in cr.get_rates('USD'):
            print('Кажется, Вы ошиблись. Введите валюту еще раз:')
            currency_to = str(input())

        print('Сколько денег (' + cd.get_currency_name(currency_from) + ') Вы хотите поменять?')
        amount_of_money = float(input())

        print('Хотели бы Вы обменять валюту в ретроспективе?')
        print('Введите "да" или "нет":')

        yes_or_no = str(input())
        while yes_or_no != "да" and yes_or_no != "нет":
            print('Кажется, Вы ошиблись. Введите ответ еще раз:')
            yes_or_no = str(input())

        if yes_or_no == "нет":
            print('Вы получите:')
            final_sum = str(converter(currency_from, currency_to, amount_of_money)) + " " + str(cd.get_symbol(currency_to))
            print(final_sum)
            print()
            print()

        elif yes_or_no == "да":
            print('Введите дату:')
            print('Год:')
            year = int(input())
            print('Месяц:')
            month = int(input())
            print('День:')
            day = int(input())
            date = datetime(year, month, day)
            print('Вы получите:')
            final_sum = str(converter_with_data(currency_from, currency_to, amount_of_money, date)) + " " + str(cd.get_symbol(currency_to))
            print(final_sum)
            print()
            print()

        history += ["Конвертировал " + str(amount_of_money) + " " + str(currency_from) + " в " + str(currency_to)
                    + " по курсу " + str(cr.get_rate(currency_from, currency_to)) + " и получил " + final_sum]

