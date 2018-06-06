""" Module for validation and for retrieving data from pesel number"""

def validate(pesel):

    """ Validation of the pesel number
        (if the characters are digits,
        number of digits, checksum, correctness of the date of birth)
        Args:
            pesel: pesel number
        Return:
            information about corectness of pesel number
        """

    MONTH_LENGTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    year = pesel[0:2]
    month = pesel[2:4]
    day = pesel[4:6]

    if pesel[2] == '0' or pesel[2] == '1':
        new_year = '19' + year
    elif pesel[2] == '2' or pesel[2] == '3':
        new_year = '20' + year
    elif pesel[2] == '4' or pesel[2] == '5':
        new_year = '21' + year
    elif pesel[2] == '6' or pesel[2] == '7':
        new_year = '22' + year
    elif pesel[2] == '8' or pesel[2] == '9':
        new_year = '18' + year


    if pesel.isdigit() and len(pesel) == 11: #sprawdzamy czy podane znaki są cyframi i czy jest ich 11

        multip = 9 * int(pesel[0]) + 7 * int(pesel[1]) + 3 * int(pesel[2]) + int(pesel[3]) + 9 * int(pesel[4]) + \
                 7 * int(pesel[5]) + 3 * int(pesel[6]) + int(pesel[7]) + 9 * int(pesel[8]) + 7 * int(pesel[9]) #liczenie sumy kontrolnej

        if multip % 10 == int(pesel[10]):
            if month != '02' and month != '82' and month != '22' and month != '42' and month !='62':
                if int(day) <= MONTH_LENGTH[int(month)-1]:
                    return True
            elif (int(new_year) % 4 == 0 and int(new_year) % 100 != 0) or int(new_year) % 400 == 0:
                if int(day) <= 29:
                    return True
                else:
                    return False
            else:
                if int(day) <= 28:
                    return True
                else:
                    return False
            return False
        return False
    return False

def extract_personal_data(pesel):

    """ Extract personal data from pesel number
        (birth date and sex )
        Args:
            pesel: pesel number
        Return:
            date_birth, sex
        """

    year = pesel[0:2]
    month = pesel[2:4]
    day = pesel[4:6]

    if pesel[2] == '0' or pesel[2] == '1':
        new_year = '19' + year
    elif pesel[2] == '2' or pesel[2] == '3':
        new_year = '20' + year
    elif pesel[2] == '4' or pesel[2] == '5':
        new_year = '21' + year
    elif pesel[2] == '6' or pesel[2] == '7':
        new_year = '22' + year
    elif pesel[2] == '8' or pesel[2] == '9':
        new_year = '18' + year

    if pesel[2] == '8' or pesel[2] == '2' or pesel[2] == '4' or pesel[2] == '6':
        new_month = '0' + pesel[3]
    elif pesel[2] == '9' or pesel[2] == '3' or pesel[2] == '5' or pesel[2] == '7':
        new_month = '1' + pesel[3]
    else:
        new_month = month

    print('Data urodzenia: ', new_year, '/', new_month, '/', day)

    sex = ['kobieta', 'mężczyzna']
    if int(pesel[9]) % 2 == 0: #drukowanie płci
        print('Płeć: ', sex[0])
    else:
        print('Płeć: ', sex[1])


