CorrectSymbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a", "B", "b", "C", "c", "D", "d", "E", "e",
                  "F", "f"]
# Массив корректных символов, используемых в MAC адресе

correctOctetSeparatorCount = 5
# Количество разделителей в обычном MAC адресе

separatorSymbol = ":"
# Символ разделитель

def zeroState(Symbol):
    if Symbol in CorrectSymbols:
        return (True, 1)
    return (False, -1)


def FirstState(Symbol):
    if Symbol in CorrectSymbols:
        return (True, 2)
    return (False, -1)


def SecondState(Symbol, counter):
    if counter < correctOctetSeparatorCount and Symbol == separatorSymbol:
        counter += 1
        return (True, 0, counter)

    return (False, -1, -1)


def CheckMAC(MACadr):
    state = 0
    # Состояние конечного автомата:
    # 0 - ожидается символ
    # 1 - ожидается символ
    # 2 - ожидается ":"
    octetSeparatorCounter = 0
    # Счетчик кол-ва разделителей
    for Symbole in MACadr:
        if state == 0:
            Correct, state = zeroState(Symbole)
            if not Correct:
                return False
        elif state == 1:
            Correct, state = FirstState(Symbole)
            if not Correct:
                return False
        elif state == 2:
            Correct, state, octetSeparatorCounter = SecondState(Symbole, octetSeparatorCounter)
            if not Correct:
                return False
        else:
            return False
    if octetSeparatorCounter == correctOctetSeparatorCount:
        return True
    else:
        return False
