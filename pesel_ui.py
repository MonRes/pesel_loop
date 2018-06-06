import pesel_tools


pesel = str(input('Witaj. Podaj Twój numer PESEL: '))

isValidate = False
while isValidate == False:
    try:
        isValidate = pesel_tools.validate(pesel)
        isValidate = str(input(pesel))
    except ValueError:
        print('Błędny PESEL. Spróbuj jeszcze raz: ')

print(pesel_tools.extract_personal_data(pesel))