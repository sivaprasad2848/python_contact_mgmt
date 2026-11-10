class vehicle:
			no_of_tyres=0
			fuel_type=None
			def __init__(self):
				print("This is constructor")
			def __del__(self):
				print("This is destrcutor")
			def set_data(self,t,f):
				self.no_of_tyres=t
				self.fuel_type=f
			def display(self):
				print(self.no_of_tyres)
				print(self.fuel_type)
car=vehicle()
car.set_data(6,"Diesel")
car.display()