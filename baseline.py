import math

def gcd (a, b):
    assert (a>=b and b>=0)
    if (b == 0):
        return (a,1,0)
    (g, x, y) = gcd (b, a%b) 
    #g is gcd of a and b, and g = x*b + y*(a%b)
    alpha = y 
    beta = x - a//b
    return (g, alpha , beta )





    

class GFelem():

    def __init__ (self, val, prm):
        assert ( is_prime(prm))
        assert (val<prm and val>=0)
        self.m_prime = prm
        self.m_val = val

    def __str__ (self):
        ret_str = "GFelem(" + str(self.m_val) + "," + str(self.m_prime) + ")"
        return ret_str

    def value (self):
        return self.m_val

    def order (self):
        return self.m_prime

    def __add__ (self, gfval):
        assert ( order(gfval) == order(self))
        return GFelem ((self.m_value + gfval.value()) % self.m_prime, self.m_prime)

    def __mul__ (self, gfval):
        assert ( order(gfval) == order(self))
        return GFelem ((self.m_value * gfval.value()) % self.m_prime, self.m_prime)

    def add_inv (self):
        #assert (order(gfval) == order(self))
        return GFelem ((self.m_prime - self.m_value % self.m_prime), self.m_prime)

    def mul_inv (self):
        g_tuple = gcd(self.m_val,self.m_prime)
        m_inv = g_tuple[1]
        return GFelem((m_inv % self.m_prime), self.m_prime)

    def __sub__ (self,gfval):
        

    
