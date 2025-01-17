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
import math


COUNTRYNAME = 0


class Demography():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._country = sys.argv[1:]
        self._data = []
        self._keys = []
        self._population = []
        self._years = []
        self._sumPopulation = 0
        self._sumYears = 0
        self._powPopulation = 0
        self._powYears = 0
        self._xy = 0

    def getData(self):

        """
        Get data from CSV file.
        """

        with open("./deps/207demography_data.csv", 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                self._data.append(row)

    def printCountryName(self):

        """
        Print country's name.
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

        count = 0

        for country in self._country:
            for x in range(len(self._data)):
                if (self._data[x][1] == country):
                    self._keys.append(x)
                    count += 1
        if count != len(self._country):
            exit(84)

    def getPopulation(self):

        """
        Get country's population
        """

        for i in range(2, len(self._data[1])):
            self._population.append(0)
        for key in self._keys:
            x = 0
            for population in range(2, len(self._data[key])):
                self._population[x] += (int(self._data[key][population]))
                x += 1
        for i in range(len(self._population)):
            self._sumPopulation += self._population[i]
            self._powPopulation += (self._population[i]**2)

    def getYears(self):

        """
        Get years' values.
        """

        for i in range(2, len(self._data[0])):
            self._years.append(int(self._data[0][i]))
        for i in range(len(self._years)):
            self._sumYears += self._years[i]
            self._powYears += (self._years[i]**2)

    def getXY(self):

        """
        Get self._population * self._years sum
        """

        for i in range(len(self._population)):
            self._xy += self._population[i] * self._years[i]

    def printFit1(self):

        """
        Print Fit1 result.
        """

        def getParameters():

            """
            Get a and b paramaters.
            """

            a = (len(self._years) * self._xy - self._sumPopulation * self._sumYears) / (len(self._years) * self._powYears - self._sumYears ** 2)

            b = (self._sumPopulation * self._powYears - self._sumYears * self._xy) / (len(self._years) * self._powYears - self._sumYears ** 2)

            return (a, b)

        a, b = getParameters()
        mean_square = 0

        print("Fit1")
        if (b >= 0):
            print("   Y = {:.2f} X + ".format(a/1000000), end="")
            print("{:.2f}".format(b/1000000))
        else:
            print("   Y = {:.2f} X - ".format(a/1000000), end="")
            print("{:.2f}".format(abs(b/1000000)))
        for i in range(len(self._population)):
            mean_square += ((self._years[i] * a + b) - self._population[i])**2 / len(self._population)
        print("   Root-mean-square deviation: {:.2f}".format(math.sqrt(mean_square)/1000000))
        print("   Population in 2050: {:.2f}".format((2050 * a + b)/1000000))

    def printFit2(self):

        """
        Print Fit2 result.
        """

        def getParameters():

            """
            Get a and b paramaters.
            """

            a = (len(self._population) * self._xy - self._sumYears * self._sumPopulation) / (len(self._population) * self._powPopulation - self._sumPopulation**2)

            b = (self._sumYears * self._powPopulation - self._sumPopulation * self._xy) / (len(self._population) * self._powPopulation - self._sumPopulation ** 2)

            return (a, b)

        a, b = getParameters()
        mean_square = 0

        print("Fit2")
        if (b >= 0):
            print("   X = {:.2f} Y + ".format(a*1000000), end="")
            print("{:.2f}".format(b))
        else:
            print("   X = {:.2f} Y - ".format(a*1000000), end="")
            print("{:.2f}".format(abs(b)))

        for i in range(len(self._population)):
            mean_square += ((self._years[i] - b) / a - self._population[i])**2 / len(self._population)
        print("   Root-mean-square deviation: {:.2f}".format(math.sqrt(mean_square)/1000000))
        print("   Population in 2050: {:.2f}".format((2050 - b) / a/1000000))

    def correlation(self):

        """
        Compute and print correlation.
        """

        correlation = (len(self._population) * self._xy) - (self._sumYears * self._sumPopulation)
        correlation /= math.sqrt((len(self._years) * self._powYears - self._sumYears**2) * (len(self._population) * self._powPopulation - self._sumPopulation**2))
        print("Correlation: {:.4f}".format(correlation))

    def run(self):

        """
        Run computations and process output printing.
        """

        def computeData():
            self.getData()
            self.getKeys()
            self.getPopulation()
            self.getYears()
            self.getXY()

        computeData()
        self.printCountryName()
        self.printFit1()
        self.printFit2()
        self.correlation()
