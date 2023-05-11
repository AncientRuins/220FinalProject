from solar_system_3d import SolarSystem, Sun, Planet

#This is how to create a solar system programatically
solar_system = SolarSystem(400, projection_2d=True)

#To prevent any issues, run only one system at a time

#This is the first system (two body binary star system)
'''
Sun(solar_system, position=(40, 40, 40), velocity=(6, 0, 6))
Sun(solar_system, position=(-40, -40, 40), velocity=(-6, 0, -6))
'''

#This is the second system (three body system)
'''
sun = Sun(solar_system)

planet1 = Planet(
        solar_system,
        position=(150, 50, 0),
        velocity=(0, 5, 5),
    )
planet2 = Planet(
        solar_system,
        mass=20,
        position=(100, -50, 150),
        velocity=(5, 0, 0)
    )
'''


#This is the third system (collision system)
'''
Planet(
    solar_system,
    200,
    position=(-100, -100, 100),
    velocity=(2, 1, -1),
)


Planet(
    solar_system,
    100,
    position=(100, 100, -100),
    velocity=(-2, -3, 3),
)
'''

#This is the fourth system (a binary start system with two planets)
'''
suns = (
    Sun(solar_system, position=(40, 40, 40), velocity=(6, 0, 6)),
    Sun(solar_system, position=(-40, -40, 40), velocity=(-6, 0, -6)),
)

planets = (
    Planet(
        solar_system,
        10,
        position=(100, 100, 0),
        velocity=(0, 10, 6),
    ),
    Planet(
        solar_system,
        20,
        position=(0, 0, 0),
        velocity=(-11, 11, 0),
    ),
)
'''

#This loop is used to run the simulation
while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()