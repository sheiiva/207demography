############################################
#                MATHEMATICS               #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#        Project : 207demography_2019      #
#                                          #
############################################

import csv
import sys

class Demography():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._country = sys.argv[1:]
        self._data = []

    def getData(self):
        """
        Get data from CSV file
        """

        with open("./207demography_data.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                self._data.append(row)

    def printCountry(self):
        """
        Print country's name
        """
        x = 0
        i = 0
        
        while x < len(self._data):
            if (i == len(self._country)):
                break
            if (i < 1):
                if (self._data[x][1] == self._country[i]):
                    print("Country = {}".format(self._data[x][0]), end="")
                    i += 1
                    x = 0
                else:
                    x += 1
            elif (i >= 1):
                if (self._data[x][1] == self._country[i]):
                    print(", {}".format(self._data[x][0]), end="")
                    i += 1
                    x = 0
                else:
                    x += 1
        print()
        
    def run(self):

        """
        Run computations and process output printing.
        """

        self.getData()
        self.printCountry()
        return 0
