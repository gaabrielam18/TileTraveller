Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 

#Einstein's famous equation states that the energy in an object at rest equals its mass times the square of the speed of light.  (The speed of light is 300,000,000 m/s.)

#Complete the skeleton code below so that it:
#* Accepts the mass of an object (remember to convert the input string to a number, in this case, a float).
#* Calculate the energy, e
#* Prints e


m_str = input('Input m: ')  # do not change this line
m_float= float(m_str)# change m_str to a float
# remember you need c
# e = 
e=(m_float*300000000**2)
print("e =", e)  # do not change this line
