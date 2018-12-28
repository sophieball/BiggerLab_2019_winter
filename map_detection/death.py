class Death:
	def __init__(self):
		self.killed = 0

	def check(self, phoenix):
		says = phoenix.broadcast()
		for s in says.keys():
			if says[s] == "Voldemort":
				phoenix.killed(s)