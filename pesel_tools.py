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

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numb_01 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    numb_02 = ['0', '1', '2']

    m_31 = ['01', '03', '05', '07', '08', '10', '12', '81', '83', '85', '87', '88', '90', '92', '21', '23',
            '25', '27', '28', '30', '32', '41', '43', '45', '47', '48', '50', '52', '61', '63', '65', '67',
            '68', '70', '72']
    m_30 = ['04', '06', '09', '11', '84', '86', '89', '91', '24', '26', '29', '31', '44', '46', '49', '51',
            '64', '66', '69', '71']
    m_28 = ['02', '82', '22', '42', '62']

    day_30 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
              '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
              '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    day_31 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
              '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
              '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    day_28 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
              '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
              '21', '22', '23', '24', '25', '26', '27', '28', '29']




    for indx, char in enumerate(pesel):
        if char in numbers and len(pesel) == 11: #sprawdzamy czy podane znaki są cyframi i czy jest ich 11

            multip = 9 * int(pesel[0]) + 7 * int(pesel[1]) + 3 * int(pesel[2]) + int(pesel[3]) + 9 * int(pesel[4]) + \
                     7 * int(pesel[5]) + 3 * int(pesel[6]) + int(pesel[7]) + 9 * int(pesel[8]) + 7 * int(pesel[9]) #liczenie sumy kontrolnej

            if multip % 10 == int(pesel[10]):
                if pesel[2] == '0' or pesel[2] == '8' or pesel[2] == '2' or pesel[2] == '4' or pesel[2] == '6':
                    if pesel[3] in numb_01:
                        if pesel[2:4] in m_31:
                            if pesel[4:6] in day_31:
                                return True
                        elif pesel[2:4] in m_30:
                            if pesel[4:6] in day_30:
                                return True
                        elif pesel[2:4] in m_28:
                            if pesel[4:6] in day_28:
                                return True
                        else:
                            return False
                elif pesel[2] == '1' or pesel[2] == '3' or pesel[2] == '5' or pesel[2] == '7' or pesel[2] == '9':
                    if pesel[3] in numb_02:
                        if pesel[2:4] in m_31:
                            if pesel[4:6] in day_31:
                                return True
                        elif pesel[2:4] in m_30:
                            if pesel[4:6] in day_30:
                                return True
                        elif pesel[2:4] in m_28:
                            if pesel[4:6] in day_28:
                                return True
                        else:
                            return False
                else:
                    return False
            return True
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

    rr = pesel[0:2]
    d = pesel[4:6]


    if pesel[2] == '0' or pesel[2] == '1': #funkcja do drukowania odpowiedniego roku według stulecia
        print("Rok urodzenia: 19", rr)
    elif pesel[2] == '8' or pesel[2] == '9':
        print("Rok urodzenia: 18", rr)
    elif pesel[2] == '2' or pesel[2] == '3':
        print("Rok urodzenia: 20", rr)
    elif pesel[2] == '4' or pesel[2] == '5':
        print("Rok urodzenia: 21", rr)
    elif pesel[2] == '6' or pesel[2] == '7':
        print('Rok urodzenia: 22', rr)
    else:
        print('Nieoczekiwany błąd')

    month_start = ['0', '8', '2', '4', '6']
    month_end = ['1', '9', '3', '5', '7']

    if pesel[2] in month_start: #drukowanie miesięcy z uwzględnieniem stuleci
        if pesel[3] == '1':
            print('Miesiąc: Styczeń')
        elif pesel[3] == '2':
            print('Miesiąc: Luty')
        elif pesel[3] == '3':
            print('Miesiąc: Marzec')
        elif pesel[3] == '4':
            print('Miesiąc: Kwiecień')
        elif pesel[3] == '5':
            print('Miesiąc: Maj')
        elif pesel[3] == '6':
            print('Miesiąc: Czerwiec')
        elif pesel[3] == '7':
            print('Miesiąc: Lipiec')
        elif pesel[3] == '8':
            print('Miesiąc: Sierpień')
        elif pesel[3] == '9':
            print('Miesiąc: Wrzesień')
        else:
            print('Nieoczekiwany błąd')
    elif pesel[2] in month_end:
        if pesel[3] == '0':
            print('Miesiąc: Październik')
        elif pesel[3] == '1':
            print('Miesiąc: Listopad')
        elif pesel[3] == '2':
            print('Miesiąc: Grudzień')
        else:
            print('Nieoczekiwany błąd')
    else:
        print('Nieoczekiwany błąd')

    print('Dzień: ', d) #drukowanie dni

    if int(pesel[9]) % 2 == 0: #drukowanie płci
        print('Płeć: Kobieta')
    else:
        print('Płeć: Mężczyzna')


