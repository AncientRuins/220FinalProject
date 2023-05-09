# solar_system_3d.py

import itertools
import math
import matplotlib.pyplot as plt

from vectors import Vector

class SolarSystem:
    def __init__(self, size, projection_2d=False):
        self.size = size
        self.x_max = self.size/2
        self.x_min = -self.size/2
        self.y_max = self.size/2
        self.y_min = -self.size/2
        self.z_max = self.size/2
        self.z_min = -self.size/2

        self.projection_2d = projection_2d
        self.bodies = []

        self.fig, self.ax = plt.subplots(
            1,
            1,
            subplot_kw={"projection": "3d"},
            figsize=(self.size / 50, self.size / 50),
        )
        if self.projection_2d:
            self.ax.view_init(10, 0)
        else:
            self.ax.view_init(0, 0)
        self.fig.tight_layout()

    def add_body(self, body):
        self.bodies.append(body)
        
    def remove_body(self, body):
        self.bodies.remove(body)

    def update_all(self):
        xmax = self.size/2
        xmin = -self.size/2
        ymax = self.size/2
        ymin = -self.size/2
        zmax = self.size/2
        zmin = -self.size/2

        for body in self.bodies:
            if body.position[0] > xmax:
                xmax = body.position[0]
            elif body.position[0] < xmin:
                xmin = body.position[0]
            elif body.position[1] > ymax:
                ymax = body.position[1]
            elif body.position[1] < ymin:
                ymin = body.position[1]
            if body.position[2] > zmax:
                zmax = body.position[2]
            elif body.position[2] < zmin:
                zmin = body.position[2] 

        self.x_min = xmin
        self.x_max = xmax
        self.y_min = ymin
        self.y_max = ymax
        self.z_min = zmin
        self.z_max = zmax

        self.bodies.sort(key=lambda item: item.position[0])
        for body in self.bodies:
            body.move()
            body.draw()

    def move_all(self):
        self.calculate_all_body_interactions()
        self.draw_all()

    def draw_all(self):
        self.ax.set_xlim((self.x_min, self.x_max))
        self.ax.set_ylim((self.y_min, self.y_max))
        self.ax.set_zlim((self.z_min, self.z_max))
        if self.projection_2d:
            self.ax.xaxis.set_ticklabels([])
            self.ax.yaxis.set_ticklabels([])
            self.ax.zaxis.set_ticklabels([])
        else:
            self.ax.axis(False)
        plt.pause(0.001)
        self.ax.clear()

    def calculate_all_body_interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                first.accelerate_due_to_gravity(second)

class SolarSystemBody:
    min_display_size = 10
    display_log_base = 1.3

    def __init__(
        self,
        solar_system,
        mass,
        position=(0, 0, 0),
        velocity=(0, 0, 0),
    ):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )
        self.colour = "black"

        self.solar_system.add_body(self)

    def move(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
            self.position[2] + self.velocity[2],
        )

    def draw(self):
        self.solar_system.ax.plot(
            *self.position,
            marker="o",
            markersize=self.display_size + self.position[0] / 30,
            color=self.colour
        )
        if self.solar_system.projection_2d:
            self.solar_system.ax.plot(
                self.position[0],
                self.position[1],
                -self.solar_system.size / 2,
                marker="o",
                markersize=self.display_size / 2,
                color=(.5, .5, .5),
            )

    def accelerate_due_to_gravity(self, other):
        distance = Vector(*other.position) - Vector(*self.position)
        distance_mag = distance.get_magnitude()
        
        if distance_mag < self.display_size or distance_mag < other.display_size:
            if self.mass < other.mass:
                #delete this
                other.velocity = (other.velocity * other.mass + self.velocity * self.mass)/(other.mass + self.mass)
                other.mass += self.mass
                self.solar_system.remove_body(self)
            else:
                self.velocity = (other.velocity * other.mass + self.velocity * self.mass)/(other.mass + self.mass)
                self.mass += other.mass
                other.solar_system.remove_body(other)
                
        
        force_mag = self.mass * other.mass / (distance_mag ** 2)
        force = distance.normalize() * force_mag

        reverse = 1
        for body in self, other:
            acceleration = force / body.mass
            body.velocity += acceleration * reverse
            reverse = -1

class Sun(SolarSystemBody):
    def __init__(
        self,
        solar_system,
        mass=10_000,
        position=(0, 0, 0),
        velocity=(0, 0, 0),
    ):
        super(Sun, self).__init__(solar_system, mass, position, velocity)
        self.colour = "yellow"

class Planet(SolarSystemBody):
    colours = itertools.cycle([(1, 0, 0), (0, 1, 0), (0, 0, 1)])

    def __init__(
        self,
        solar_system,
        mass=10,
        position=(0, 0, 0),
        velocity=(0, 0, 0),
    ):
        super(Planet, self).__init__(solar_system, mass, position, velocity)
        self.colour = next(Planet.colours)