print('Welcome to the Space Travel Calculator')
distance = int(input("Enter the distance to the celestial object in light years"))
speed = int(input("Enter the spacecraft speed in fraction of the speed of light"))
time = distance/speed
print("It will take ", time, " minutes to get there")