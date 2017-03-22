#!/Users/mschmid/anaconda/bin/python
"""Main Script for running the weatherplotter.
Version 0.4
Manuel Schmid
22.Februar 2017

Needed Libraries:

Pandas
datetime
numpy
seaborn
matplotlib
"""


from weatherAnalyst import *
from weatherstationclass import *

def main():
    ws = weatherstation()
    ws.whichDataset()
    ws.which_station()
    ws.time_interval()
    ws.checkPrintFlag()
    ws.printValues()

if __name__ == '__main__':
    main()
    #asks if you want to start again? probably dirty solution but whatever
    while True:
        startAgain = input('Do you want to make another plot? (y/n)')
        if startAgain == "y":
            main()
        if startAgain == "n":
            break
        else:
            print("'y' or 'n'")
