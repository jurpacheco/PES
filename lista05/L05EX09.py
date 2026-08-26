print(f'==================================== lista de exercício 05 ====================================')
print(f'------------------------------------------- Questão 9 -------------------------------------------\n')
print("Construa uma função que receba uma data no formato DD/MM/AAAA (string) e\ndevolva uma string com a data por extenso, por exemplo: “doze de agosto de dois mil e\nvinte e quatro”. Seu algoritmo deve ser capaz de converter datas entre os anos de 2000 e\n2100.\n")
print(f'------------------------------------------------------------------------------------------------\n')

def format_date_to_text(date_str):

    days = {
        1: "primeiro", 2: "dois", 3: "três", 4: "quatro", 5: "cinco",
        6: "seis", 7: "sete", 8: "oito", 9: "nove", 10: "dez",
        11: "onze", 12: "doze", 13: "treze", 14: "catorze", 15: "quinze",
        16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove", 20: "vinte",
        21: "vinte e um", 22: "vinte e dois", 23: "vinte e três", 24: "vinte e quatro",
        25: "vinte e cinco", 26: "vinte e seis", 27: "vinte e sete", 28: "vinte e oito",
        29: "vinte e nove", 30: "trinta", 31: "trinta e um"
    }

    months = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
        5: "maio", 6: "junho", 7: "julho", 8: "agosto",
        9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }

    units = {
        0: "", 1: "um", 2: "dois", 3: "três", 4: "quatro",
        5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove"
    }

    tens = {
        10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "catorze",
        15: "quinze", 16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove",
        20: "vinte", 30: "trinta", 40: "quarenta", 50: "cinquenta",
        60: "sessenta", 70: "setenta", 80: "oitenta", 90: "noventa"
    }

    day_str, month_str, year_str = date_str.split("/")
    day = int(day_str)
    month = int(month_str)
    year = int(year_str)

    day_text = days[day]
    month_text = months[month]

    if year == 2000:
        year_text = "dois mil"
    elif year == 2100:
        year_text = "dois mil e cem"
    else:

        last_two_digits = year % 100
        
        if last_two_digits in tens:
            year_text = f"dois mil e {tens[last_two_digits]}"
        else:
            ten_part = (last_two_digits // 10) * 10
            unit_part = last_two_digits % 10
            year_text = f"dois mil e {tens[ten_part]} e {units[unit_part]}"

    return f"{day_text} de {month_text} de {year_text}"


date=input("Coloque q data no formato dd/mm/aaaa para receber por extenso: ")
print (format_date_to_text(date))