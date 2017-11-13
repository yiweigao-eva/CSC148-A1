class Location:
    def __init__(self, row, column):
        """Initialize a location.

        @type self: Location
        @type row: int
        @type column: int
        @rtype: None
        """
        self.row, self.column = row, column

    def __str__(self):
        """Return a string representation.

        @rtype: str
        """
        return "({}, {})".format(self.row, self.column)

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @rtype: bool
        """
        return (type(self) == type(other),
                self.row == other.row,
                self.column == other.column)



def manhattan_distance(origin, destination):
    """Return the Manhattan distance between the origin and the destination.

    @type origin: Location
    @type destination: Location
    @rtype: int
    """
    d = abs(origin.row - destination.row) + abs(origin.column - destination.column)
    return int(d)


def deserialize_location(location_str):
    """Deserialize a location.

    @type location_str: str
        A location in the format 'row,col'
    @rtype: Location
    
    >>> str(deserialize_location('1,3'))
    Location(1, 3)
    >>> deserialize_location('10,220')
    Location(10, 220)
    """
    row = 0
    column = 0
    i = 0
    while i < len(location_str):
        if location_str[i] == ',':
            row = int(location_str[0:i])
            column = int(location_str[i+1:])
        i += 1
    new = Location(row, column)
    return new
                
            