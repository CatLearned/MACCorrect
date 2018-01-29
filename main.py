# Place for main Function
import sys
from MACCorrect import MACParser

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print("FF:FF:FF:FF:FF:FF" + " is " + str(MACParser.CheckMAC("FF:FF:FF:FF:FF:FF")))
    else:
        print(sys.argv[1] + " is " + str(MACParser.CheckMAC(sys.argv[1])))
