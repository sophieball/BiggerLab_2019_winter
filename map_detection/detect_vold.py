import pygame
import random
from phoenix import *
from death import *

phoenix = Phoenix()
print phoenix
death = Death()

phoenix.add_member("Harry")
phoenix.add_member("Hermione")
phoenix.add_member("Ron")

for i in range(3):
	phoenix.say_something()
	phoenix.print_says()

	death.check(phoenix)
	print phoenix.get_members()
