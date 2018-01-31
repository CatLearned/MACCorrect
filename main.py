# Place for main Function
import sys
from MACCorrect import MACCorrectAuto as MC
from MACCorrect import MACCorrectReg as MCReg

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        Mac = "1F:FF:FF:FF:FF:FA"
    else:
        Mac = sys.argv[1]
    print(Mac + " is " + str(MC.CheckMAC(Mac)))
    print(Mac + " is (Reg) " + str(MCReg.CheckMacReg((Mac))))
