import pesel_tools


pesel = str(input('Witaj. Podaj Twój numer PESEL: '))

if pesel_tools.validate(pesel) is True:
    print(pesel_tools.extract_personal_data(pesel))
else:
    while pesel_tools.validate(pesel) == False:
        pesel = str(input('PESEL niepoprawny. Sprawdź i spróbuj jeszcze raz: '))
        if pesel_tools.validate(pesel) is True:
            print(pesel_tools.extract_personal_data(pesel))


