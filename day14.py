class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        #self.maximumDifference = max(self.__elements) - min(self.__elements)
        min = self.__elements[0]
        max = self.__elements[0]
        for i in range(len(self.__elements)):
            if(self.__elements[i] > max):
                max = self.__elements[i]
            if(self.__elements[i] < min):
                min = self.__elements[i]
        self.maximumDifference = max - min



_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()

print(d.maximumDifference)