import random
class Phoenix:
	def __init__(self):
		self.cur_members = []
		self.says = {}
		self.all_members = ["Voldemort"]

	def add_member(self, name):
		self.cur_members.append(name)
		self.all_members.append(name)

	def killed(self, name):
		self.cur_members.remove(name)

	def say_something(self):
		self.says = {}
		for m in self.cur_members:
			self.says[m] = random.choice(self.all_members)

	def print_says(self):
		print self.says

	def broadcast(self):
		return self.says

	def get_members(self):
		return self.cur_members