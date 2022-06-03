class FuelPump:
'''
class FuelPump to control a quantity and price of the fuel of a pump.

Variables:
fuelPrice : float
   value of the liter of the fuel.
fuelQuantity:
    numbers of liters that remain in the pump.

constructo/getter/setter

__init__ : constructor
    the variables are defined with a default value of 0
get_fuelPrice: getter of fuelPrice
set_fuelPrice: setter of fuelPrice
get_fuelQuantity: getter of fuelQuantity
set_fuelQuantity: setter of fuelQuantity
'''


    def __init__(self, fuelPrice=5,fuelQuanity=100):
        self._fuelPrice = fuelPrice  
        self._fuelQuantity = fuelQuanity
        
    def get_fuelPrice(self):
        return self._fuelPrice
    
    def set_fuelPrice(self, value):
        self._fuelPrice = value
        
    def get_fuelQuantity(self):
        return self._fuelQuantity

    def set_fuelQuantity(self, value):
        self._fuelQuantity = value




    def setPrice(self, price):   
        '''
		Defines the new price of the liter of the fuel.
		
		Defines the new price of the liter of the fuel calling
		the fuelPrice setter, passing price as the price.
		If the price is too low, defines the price as 0.

		Parameters
		----------
		price : float
			Must be 0 or bigger.

		Examples
		--------
		>>> setPrice(5.4)
		The price for the fuel liter is $5.4
		>>> setPrice(-10)
		The price for the fuel liter is $0

		'''
        if price < 0:
            self.set_fuelPrice(0)
        else:
            self.set_fuelPrice(price)
        print('The price for fuel liter is %d' % self.get_fuelPrice())

    def setQuantity(self, liters):

        if liters < 0:
            self.set_Quantity(0)
        else:
            self.set_fuelQuantity(liters)
        print('There are %d of fuel left in the pump' % self.get_fuelQuantity())


    def fillWithPrice(self, price):
        '''
		Returns how many liters of fuel will be filled by price and update the quantity of fuel 
    that remain in the pump calling the setQuantity() with the get_fuelQuantity() - pumped 
     valor.
		

		Parameters
		----------
		price : float
		 the paid price

      Returns :
      ___________________
      pumpedFuel : float

      The quantity of fuel that will be pumped, if there is not enought fuel or the fuelPrice 
      is not defined, return 0.
      The value us defined dividing the price by the get_fuelPrice().
      
		'''
        if self.get_fuelPrice() is None:
              print('The fuel price is not defined')
              return 0
        pumpedFuel = price / self.get_fuelPrice()
        if self.get_fuelPrice() > price:
            print('The price for a liter is $%d and you gave $%d' % (self.get_fuelPrice(), price))
            return 0
        elif self.get_fuelQuantity() < pumpedFuel:
              print('There are only %d liters of fuel remaining' % self.get_fuelQuantity())
              return 0
        self.setQuantity(self.get_fuelQuantity() - pumpedFuel) 
        return pumpedFuel


    def fillWithLiters(self, liters):
'''
          Returns how much should be payed for the pumped fuel.


          Returns he final paid price, or 0 if there is not enough fuel or the price is not 
          defined, and updates the quantity of fuel that there is in the pump calling 
          setQuantity() with the get_fuelQuantity() - liters.

          Parameters
		       ----------
          liters : float
            The amount of liters to be filled.


          Returns:
         _________________

            price : float
            The price that should be paid for the pumped fuel, that is defined by the 
            multiplying the liters by get_fuelPrice() .
            If there is not enought fuel to be pumped, or the price is not defined, returns 0.    


'''




      
      
        if self.get_fuelPrice() is None:
              print('The fuel price is not defined')
              return 0

        if self.get_fuelQuantity() < liters:
              print('There is not enought fuel')
              return 0
        self.setQuantity(self.get_fuelQuantity() - liters)
        return liters * self.get_fuelPrice()





f = FuelPump()
print(f.fillWithPrice(5))
print(f.fillWithLiters(10))
print(f.fillWithPrice(-5))
print(f.fillWithLiters(-10))
