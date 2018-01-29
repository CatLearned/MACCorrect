CorrectSymbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "a", "B", "b", "C", "c", "D", "d", "E", "e",
                  "F", "f"]
# Массив корректных символов, используемых в MAC адресе
state = 0
# Состояние конечного автомата:
# 0 - ожидается символ
# 1 - ожидается символ
# 2 - ожидается ":"
octetSeparatorCounter = 0
# Счетчик кол-ва разделителей
correctOctetSeparatorCount = 5


# Количество разделителей в обычном MAC адресе

def zeroState(Symbol):
    return


def FirstState(Symbol):
    return


def SecondState(Symbol):
    return


def CheckMAC(MACadr):
    return
