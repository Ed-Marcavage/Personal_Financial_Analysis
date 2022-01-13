class InputNotInRangeError(Exception):
    """Exception raised for numbers out of range

    Attributes:
        number -- input number which caused the error
        message -- explanation of the error
    """

    def __init__(self, number, message="Number is not in range"):
        self.number = number
        self.message = message
        super().__init__(self.message)


def InputNotInRange(input, lower, upper):
  if not lower <= input <= upper:
    raise InputNotInRangeError(input)

