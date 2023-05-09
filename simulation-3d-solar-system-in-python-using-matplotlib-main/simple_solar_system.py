# simple_solar_system.py

from solar_system_3d import SolarSystem, Sun, Planet
import time

#This is how to create a solar system programatically
'''
solar_system = SolarSystem(400, projection_2d=True)

sun = Sun(solar_system)

t = 0.0

planet1 = Planet(
        solar_system,
        position=(100, 100, 100),
        velocity=(0, 0, 0),
    )
planet2 = Planet(
        solar_system,
        mass=20,
        position=(-100, -100, -100),
        velocity=(0, 50, 50)
    )

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()
    '''

#This is how to create a solar system via the console
n = int(input("How many celestial bodies do you want to add: "))
print(n)

solar_system = SolarSystem(400, projection_2d=True)
t = 0.0
    

for i in range(0, n):
    mass = float(input("\nNow requesting information about the next object.\nWhat is the mass of the object: "))
    xpos = float(input("What is the location in the x-direction: "))
    ypos = float(input("What is the location in the y-direction: "))
    zpos = float(input("What is the location in the z-direction: "))
    xvel = float(input("What is the velocity in the x-direction: "))
    yvel = float(input("What is the velocity in the y-direction: "))
    zvel = float(input("What is the velocity in the z-direction: "))
    print(mass, " ", xpos, " ", ypos, " ", zpos, " ", xvel, " ", yvel, " ", zvel)
    Planet(solar_system, mass=mass, position=(xpos, ypos, zpos), velocity=(xvel, yvel, zvel))
    

if n > 0:
    while True:
        solar_system.calculate_all_body_interactions()
        solar_system.update_all()
        solar_system.draw_all()