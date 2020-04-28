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

    def checkArgs(self, argv):

        """
        Check for arguments validity.
        """

        def isNum(value):

            """
            Return True if value is a digit.
            """

            try:
                int(value)
            except:
                False
            else:
                return True
            
        return isNum(0) # to delete

    def needHelp(self, argv):

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
