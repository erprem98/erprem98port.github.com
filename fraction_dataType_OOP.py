class Fraction:
    def __init__(self,n,d):
        self.n=n
        self.d=d

    def __str__(self):
        return "{}/{}".format(self.n,self.d)
    

    def __add__(self, other):
       temp_num=self.n * other.d + self.d * other.n
       temp_den=self.d * other.d

       return "{}/{}".format(temp_num, temp_den)
    
    def __sub__(self, other):
        temp_num = self.n * other.d - self.d * other.n
        temp_den = self.d * other.d

        return "{}/{}".format(temp_num, temp_den)

    
a=Fraction(2,3)
b=Fraction(2,7)
print(a+b)



