
# Implement suggested methods if needed.  Add or remove helper methods or attributes you need; 
# just make sure you keep the constructor parameters the same for the tests.
class Domino:
    def __init__(self, value_1: int, value_2: int) -> None:
        if value_1 > value_2:
            self.value = (value_2, value_1)
        else:
            self.value = (value_1, value_2)

    # Returns true if value is one of the sides of the domino
    def contains_val(self, value):
        return value in self.value

    # returns true is the domino is a double
    def is_double(self):
        return self.value[0] == self.value[1]
    
    # sets which pip values are open (can be played on) and closed, given the value played on
    # matched_value: the value that you are playing on, e.g. if your domino is 7-5, and you are
    # playing on a 5 on the board, matched_value will be 5.
    # set attributes self.open_end and self.closed_end to the appropriate values to get
    # __str__ to work. These should be declared here, NOT in the constructor
    def set_open_value(self, matched_value:int):
        if self.value[0] == matched_value:
            self.open_end = self.value[1] 
            self.closed_end = self.value[0] 
        else:
            self.open_end = self.value[0] 
            self.closed_end = self.value[1] 
            
    # returns a string representing the domino; used for casting as string and string formats
    def __str__(self) -> str:
        return f"{self.open_end}-{self.closed_end}" if hasattr(self, "open_end") \
            else f"{self.value[0]}-{self.value[1]}"

    # DO NOT CHANGE __eq__ or __hash__ BELOW.  These allow you to use == on dominos
    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, Domino):
            return obj.value == self.value
        return False

    def __hash__(self) -> int:
        return hash(self.value)
