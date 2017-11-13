from location import Location, manhattan_distance
from rider import Rider


class Driver:
    """A driver for a ride-sharing service.

    === Attributes ===
    @type id: str
        A unique identifier for the driver.
    @type location: Location
        The current location of the driver.
    @type is_idle: bool
        A property that is True if the driver is idle and False otherwise.
    """

    def __init__(self, identifier, location, speed):
        """Initialize a Driver.

        @type self: Driver
        @type identifier: str
        @type location: Location
        @type speed: int
        @rtype: None
        """
        
        self.id, self.location, self.speed = identifier, location, speed
        self.destination = None
        self.is_idle = True

    def __str__(self):
        """Return a string representation.

        @type self: Driver
        @rtype: str
        """
        return "Driver{} is in {} with {} speed.".format(self.id, self.loction, self.speed)

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @type self: Driver
        @rtype: bool
        """
        return (type(self) == type(other),
                self.id == other.id,
                self.location == other.location,
                self.speed == other.speed,
                self.destination == other.destination,
                self.is_idle == other.is_idle)

    def get_travel_time(self, destination):
        """Return the time it will take to arrive at the destination,
        rounded to the nearest integer.

        @type self: Driver
        @type destination: Location
        @rtype: int
        
        >>> d1 = Driver('Driver1', Location(0, 0), 2)
        >>> d1.get_travel_time(Location(1, 3))
        2
        """
        d = manhattan_distance(self.location, destination)
        t = d / self.speed
        return round(t)

    def start_drive(self, location):
        """Start driving to the location and return the time the drive will take.

        @type self: Driver
        @type location: Location
        @rtype: int
        """
        self.is_idle = False
        t = self.get_travel_time(location)
        self.destination = location        
        return int(t)

    def end_drive(self):
        """End the drive and arrive at the destination.

        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        #self.is_idle = True
        if self.destination is not None:
            self.location = self.destination
            self.destination = None
            
            
            

    def start_ride(self, rider):
        """Start a ride and return the time the ride will take.

        @type self: Driver
        @type rider: Rider
        @rtype: int
        """
        self.is_idle = False
        self.destination = rider.destination
        self.location = rider.origin
        t = self.get_travel_time(rider.destination)
        return int(t)

    def end_ride(self):
        """End the current ride, and arrive at the rider's destination.

        Precondition: The driver has a rider.
        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        if self.is_idle == False and self.destination is not None:
            self.location = self.destination
            self.destination = None
            self.is_idle = True