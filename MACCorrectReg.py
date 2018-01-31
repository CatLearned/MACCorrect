import re


def CheckMacReg(InputMAC):
    InputMAC = str(InputMAC)
    resaut = re.findall(r'^[0123456789AaBbCcDdEeFf][0123456789AaBbCcDdEeFf]:'
                        r'[0123456789AaBbCcDdEeFf][0123456789AaBbCcDdEeFf]:'
                        r'[0123456789AaBbCcDdEeFf][0123456789AaBbCcDdEeFf]:'
                        r'[0123456789AaBbCcDdEeFf][0123456789AaBbCcDdEeFf]:'
                        r'[0123456789AaBbCcDdEeFf][0123456789AaBbCcDdEeFf]:'
                        r'[0123456789AaBbCcDdEeFf][0123456789AaBbCcDdEeFf]$', InputMAC)
    if resaut != []:
        return True
    else:
        return False
