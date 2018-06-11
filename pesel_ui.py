import pesel_tools

pesel = input('Please, give the PESEL number: ')

print(pesel_tools.extract_personal_data(pesel))