from PIL import Image

f = open("password")
password = f.readline().strip()
f.close()

img = Image.open('Harry_Potter_Fatlady.jpg')
img.show()

print "Password?"
a = raw_input()
while a != password:
  print "Are you a Gryffindor? Try again?"
  a = raw_input()

print "Welcome."
img = Image.open("Gryffindor-Common-room.jpg")
img.show()
