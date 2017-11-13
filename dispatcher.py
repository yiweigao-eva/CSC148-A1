from driver import Driver
from rider import Rider


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.
    """

    def __init__(self):
        """Initialize a Dispatcher.

        @type self: Dispatcher
        @rtype: None
        """
        self.driver_fleet = []
        self.driverwaitlist = []
        self.riderwaitlist = []

    def __str__(self):
        """Return a string representation.

        @type self: Dispatcher
        @rtype: str
        """
        return "{} driver in waitlist, and {} rider in waitlist".format(len(self.driverwaitlist), len(self.riderwaitlist))

    def request_driver(self, rider):
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: Driver | None
        """
        driver = None
        if self.driverwaitlist == []:
            self.riderwaitlist.append(rider)
        else:
            time = self.driverwaitlist[0].get_travel_time(rider.origin)
            fast = self.driverwaitlist[0]
            for driver in self.driverwaitlist:
                if driver.get_travel_time(rider.origin) < time:
                    time = driver.get_travel_time(rider.origin)
                    fast = driver
            driver = fast
        return driver

    def request_rider(self, driver):
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        @type self: Dispatcher
        @type driver: Driver
        @rtype: Rider | None
        """
        rider = None
        
        if driver not in self.driver_fleet:
            self.driver_fleet.append(driver)
            
        if driver.is_idle:
            if self.riderwaitlist == []:
                self.driverwaitlist.append(driver)
            else:
                rider = riderwaitlist[0]
            
        return rider
        

    def cancel_ride(self, rider):
        """Cancel the ride for rider.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """
        self.riderwitlist.remove(rider)
