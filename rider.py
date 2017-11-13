"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
@type WAITING: str
    A constant used for the waiting rider status.
@type CANCELLED: str
    A constant used for the cancelled rider status.
@type SATISFIED: str
    A constant used for the satisfied rider status
"""

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:
    """A rider for a ride-sharing service.

    === Attributes ===
    @type id: str
        A unique identifier for the rider.
    @type origin: location
        The current location of the rider.
    @type destination: location
        The destination of the rider
    @type status: constant
        The status of the rider
    @type patience: int
        The number of time units of the rider will wait to be picked up before they cancle
    """

    

    def __init__(self, identifier, origin, destination, patience):
        """
        Initialize a Rider.

        @type self: Rider
        @type identifier: str
        @type origin: Location
        @type destination: Location
        @type patience: int
        @rtype: None
        """    
        self.id, self.origin, self.destination = identifier, origin, destination, 
        self.patience = patience
        self.status = WAITING
        
