# Simulating a Solar System in 3D

This code is based on that found in the article ["Simulating a 3D Solar System In Python Using Matplotlib"](https://thepythoncodingbook.com/2021/12/11/simulating-3d-solar-system-python-matplotlib/).

This was modified in several ways to achieve the goals we desired. 

1. The first was to add collisions between the various objects when they get too close to each other. This helps to simulate an actual solar system in greater detail, as collisions are an integral part of the solar system formation for some systems. For instance, the moon is theorized to be the result of the collision of Earth with another planet.

2. The second was to add a scaling view to the outputted 3D plot. Originally, if the objects got too far away from the center, they could not be seen again. To combat this, we add a scaling view to the plot so that all objects are visible at all times.

3. Finally, we added a way to input information to the program via the console log. Now, there are two ways to simulate a solar system: Via code and via the console. Using the code approach, users can create objects in python and add them to a solar system, which makes it easy to use for people with prior coding experience. For people who have no coding experience, they can still use this simulation via the console log, which aks for inputs regarding the number of objects and the mass, position, and velocity of each object. With that information, the program creates the corresponding solar system for simulation.

In the binary_star_system.py file is a simple binary star system with 2 suns and 2 planets, all created via code. Running this file creates and simulates this system until the program is manually terminated.

In the simple_solar_system.py file is the console log code, so that users can directly use the console for input.

The solar_system_3d.py file contains the code that simulates the solar system and defines the various objects used in the solar system simulation.

Finally, the vectors.py file contains a self-defined vector class that is used in all position and velocity calculations.