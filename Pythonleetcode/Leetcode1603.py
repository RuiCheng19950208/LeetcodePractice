class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.small=small
        self.medium = medium
        self.big = big




    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType==3:
            if self.small>0:
                self.small-=1
                return True
            else:
                return False


        elif carType==2:
            if self.medium > 0:
                self.medium -= 1
                return True
            else:
                return False


        else:
            if self.big > 0:
                self.big -= 1
                return True
            else:
                return False


print(ParkingSystem)