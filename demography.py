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

COUNTRYNAME = 0

class Demography():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._country = sys.argv[1:]
        self._data = []
        self._keys = []

    def getData(self):

        """
        Get data from CSV file
        """

        with open("./deps/207demography_data.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                self._data.append(row)

    def printCountry(self):

        """
        Print country's name
        """

        print("Country: ", end="")
        for key in self._keys:
            print(self._data[key][COUNTRYNAME], end="")
            if key != self._keys[len(self._keys) - 1]:
                print(", ", end="")
        print()

    def getKeys(self):

        """
        Find countries' keys in data and stock it.
        """

        for country in self._country:
            for x in range(len(self._data)):
                if (self._data[x][1] == country):
                    self._keys.append(x)
        print(self._keys)

    def run(self):

        """
        Run computations and process output printing.
        """

        self.getData()
        self.getKeys()
        self.printCountry()
        return 0
