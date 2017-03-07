class Car(object):

	num_of_doors = 4
	num_of_wheels = 4
	car_type = "saloon"
	speed = 0
	cartypes = ["trailer", "saloon"]

	def __init__(self, name="General", model="GM", car_type="saloon"):
		self.name = name
		self.model = model
		self.car_type = car_type

		if self.car_type not in self.cartypes:
			return
			
		if type(self.num_of_doors) is not int or type(self.num_of_wheels) is not int or type(speed) is not int:
			return

		self.check_type()

	def check_type(self):
		if self.name == "Porshe" or self.name == "Koenigsegg":
			self.num_of_doors = 2

		if self.car_type == "trailer" :
			self.num_of_wheels = 8

	def is_saloon(self):
		return True and self.car_type == "saloon"

	def drive(self, speed):
		if type(speed) is str:
			return
		if self.car_type == "trailer":
			self.speed = speed * 11
		elif self.car_type == "saloon":
			self.speed = 10 ** speed
			
		return self
