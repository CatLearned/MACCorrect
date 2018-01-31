# Place for main Function
import sys
from MACCorrect import MACCorrectAuto as MC
from MACCorrect import MACCorrectReg as MCReg

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        Mac = "FF:FF:FF:FF:FF:FF"
    else:
        Mac = sys.argv[1]
    print(str(Mac) + " is " + str(MC.CheckMAC(Mac)))
    print(str(Mac) + " is (Reg) " + str(MCReg.CheckMacReg((Mac))))
