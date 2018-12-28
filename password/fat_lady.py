from PIL import Image

# file operation
f = open("password")
# readline reads in \n. Let students try this without strip
password = f.readline().strip()
f.close()

img = Image.open('Harry_Potter_Fatlady.jpg')
img.show()

print "Password?"
a = raw_input() #raw_input vs input
while a != password: # while loop
  print "Are you a Gryffindor? Try again?"
  a = raw_input()

print "Welcome."
img = Image.open("Gryffindor-Common-room.jpg")
img.show()
