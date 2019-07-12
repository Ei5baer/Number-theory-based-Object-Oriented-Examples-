import math

########################

def gcd ( a, b ) :
  assert ( a >= 0 and b >= 0 and a >= b  )
  if ( b==0 ) :
    return a
  else :
    return gcd ( b , a % b ) 

########################

def gcd_exteuclid ( a , b ) :
  assert ( 0 <= a and 0 <= b and a >= b ) 
  if ( b == 0 ) :
    return ( a , 1 , 0 )
  ( g , x, y ) = gcd_exteuclid ( b , a % b ) 
  return ( g , y , x - y * ( a // b ) )

########################
def is_prime ( alleged_prm ) :
  for k in range ( 2, int ( math.sqrt( alleged_prm ) ) ) :
    if ( alleged_prm % k == 0 ) :
      return False
  return True






class GFelem ( ) :
  def __init__ ( self , val , prm ) :
    assert ( is_prime( prm ) ) 
    assert ( 0 <= val and val < prm  ) 
    self.m_prime = prm 
    self.m_value = val
 
  def __str__ ( self ) :
    ret_str = "GFelem(" + str(self.m_value) + "," + str(self.m_prime) + ")"
    return ret_str

  def value ( self ) :
    return self.m_value

  def order ( self ) :
    return self.m_prime

  def __add__ ( self , gfval ) :
    assert ( gfval.order() == self.order() )
    return GFelem( ( self.m_value + gfval.value() ) % self.m_prime , self.m_prime )

  def __mul__ ( self , gfval ) :
    assert ( gfval.order() == self.order() )
    return GFelem( ( self.m_value * gfval.value() ) % self.m_prime , self.m_prime )

  def add_inv ( self ) :
    return GFelem( self.m_prime - self.m_value , self.m_prime )

  def mul_inv ( self ) :
    ( g , x, y ) = gcd_exteuclid ( self.m_prime , self.m_value )
    # so 1 = g = x * self.m_prime + y * self.m_value
    # therefore y % self_m_prime is multiplicative inverse of self.m_value  
    return GFelem( y % self.m_prime , self.m_prime )

  def __div__ ( self , gfval ) :
    assert ( self.order() == gfval.order() ) 
    return self * gfval.mul_inv() 

  def __sub__ ( self , gfval ) :
    assert ( self.order() == gfval.order() ) 
    #return self + gfval.add_inv() 
    return GFelem (  ( self.m_value - gfval.value() ) % self.m_prime , self.m_prime )

########################
    
gf_3_5 = GFelem(3,5)
gf_4_5 = GFelem(4,5)
print (gf_3_5 + gf_4_5 )
print (gf_4_5 * gf_4_5 )

