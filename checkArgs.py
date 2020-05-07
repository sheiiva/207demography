############################################
#                MATHEMATICS               #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#        Project : 207demography_2019      #
#                                          #
############################################


class ArgumentManager():

    def checkArgs(self, argv) -> int:

        """
        Check for arguments validity.
        """

        if (len(argv) < 2):
            print("Wrong number of arguments. Please run with -h.")
            return 84
        return 0

    def needHelp(self, argv) -> bool:

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
