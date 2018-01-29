# Place for main Function
import sys
from MACCorrect import MACParser

if __name__ == "__main__":
    if(len(sys.argv)):
        print(MACParser.CheckMAC("FF:FF:FF:FF:FF:FF"))
    else:
        print(MACParser.CheckMAC(sys.argv[1]))
