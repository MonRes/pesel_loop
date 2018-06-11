"""Module for validation and for retrieving data from pesel"""

def validate(pesel):

    """Validation of the pesel number
    (if the cahracters are digits,
    number of digits, cheksum,
    correctness of the date of birth
    Args:
        pesel: pesel number
    Return:
        information about correctness of the pesel number"""


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

    if pesel.isdigit() and len(pesel) == 11:
        multip = 9 * (int(pesel[0]) + int(pesel[4]) + int(pesel[8])) + 7 * (int(pesel[1]) + int(pesel[5]) +
                        int(pesel[9])) + 3 * (int(pesel[6]) + int(pesel[2])) + int(pesel[3]) + int(pesel[7])

        month_table = ['02', '82', '22', '42', '62']
        if multip %10 == int(pesel[10]):
            if month not in month_table:
                if int(day) <= MONTH_LENGTH[int(month)-1]:
                    return True
                elif (int(new_year) %4 == 0 and int(new_year) %100 != 0) or int(new_year) %400 == 0:
                    if int(day) <= 29:
                        return True
                    return False
                else:
                    if int(day) <= 28:
                        return True
                    return False
                return False
            return False
        return False
    return False


def extract_personal_data(pesel):
    """Extract personal data from pesel number
    (birth date and sex)
    Args:
        pesel: pesel number
    Returns:
        date_birth, sex"""


    if validate(pesel) == False:
        raise ValueError ('Podany PESEL jest nieprawidłowy')

    year = pesel[0:2]
    month = pesel[2:4]
    day = pesel[4:6]
    new_year = ''

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

    all_data = '{} / {} / {}'.format(day, new_month, new_year)


    sex = ['woman', 'man']
    if int(pesel[9]) %2 == 0:
        sex_ = sex[0]
    else:
        sex_ = sex[1]

    pesel_info = {}

    pesel_info['Bitrh Date: '] = all_data
    pesel_info['Sex: '] = sex_

    return pesel_info

