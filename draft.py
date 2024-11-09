import numpy as np
import matplotlib.pyplot as plt

G = 1

#Three body problem simple simulation. Kevin Eisenberg, 11/9/2024
#Do not run on jupyter notebook, it will not work (plt pause). Run on a proper environment (made in VS code)


#FORM OF FORCES: F12 MEANS FORCE ON 1 DUE TO 2 (1->2)

class Planet():
    def __init__(self,mass,pos,radius=0.1,v=[0,0]): #pos is a tuple (x,y), velocity is a tuple
        self.mass = mass
        self.pos = np.array(pos,dtype=float) #dtype prevents errors down the road
        self.v = np.array(v,dtype=float)
        self.radius = radius
    
def gravity_acceleration(planet1,planet2):
    
    d = planet2.pos - planet1.pos #displacement vector
    
    r = np.linalg.norm(d)
    if r <= (planet1.radius + planet2.radius):
        raise ValueError('Collision has occurred!')
    magnitude = (G*planet1.mass*planet2.mass)/r**2
    
    vector = magnitude * d/r #magnitude in the unit direction of r, r/|r|
    a = vector/planet1.mass

    return a

def update_position(planet,dt):
    planet.pos += planet.v*dt

def setup(planetList):
    plt.figure(figsize=(7,7))
    plt.ylim((0,20))
    plt.xlim((0,20))
    plt.title('3 body problem')
    axs = plt.axes()
    axs.set_facecolor('black')
    for planet in planetList:
        plt.scatter(planet.pos[0],planet.pos[1],c='w',s=planet.radius*5)
    
    

def step(planet1,planet2,planet3,dt):

    a12 = gravity_acceleration(planet1,planet2)
    a21 = gravity_acceleration(planet2,planet1)
    a13 = gravity_acceleration(planet1,planet3)
    a31 = gravity_acceleration(planet3,planet1)
    a23 = gravity_acceleration(planet2,planet3)
    a32 = gravity_acceleration(planet3,planet2)

    planet1.v += a12*dt
    planet2.v += a21*dt
    planet1.v += a13*dt
    planet3.v += a31*dt
    planet2.v += a23*dt
    planet3.v += a32*dt

    update_position(planet1,dt)
    update_position(planet2,dt)
    update_position(planet3,dt)
    plt.ylim((0,20))
    plt.xlim((0,20))
    plt.scatter(planet1.pos[0],planet1.pos[1],color='white',s=planet1.radius*5)
    plt.scatter(planet2.pos[0],planet2.pos[1],color='red',s=planet2.radius*5)
    plt.scatter(planet3.pos[0],planet3.pos[1],color='blue',s=planet3.radius*5)

    plt.pause(0.001)

#--------------------------------------------
sun = Planet(600,(10,10),radius=0.1,v=[-1,11])
mars = Planet(500,(8,10),radius=0.1,v=[3,5])
moon = Planet(500,(12,10),radius=0.1,v=[-3,7])

setup([sun,mars,moon])
for i in range(100):
    step(sun,mars,moon,0.005)