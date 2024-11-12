import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from ipywidgets import interact, FloatSlider
from IPython.display import HTML

# Constants
G = 1  # Gravitational constant in normalized units
m1, m2, m3 = 1.0, 1.0, 1.0  # Masses of the three bodies

# Function to generate the animation based on initial conditions
def three_body_simulation(x1, y1, x2, y2, vx1, vy1, vx2, vy2):
    # Derived initial conditions for body 3 based on symmetry (keeps COM at origin)
    x3, y3 = 0.0, 0.0
    vx3, vy3 = -2 * vx1, -2 * vy1

    # Initial conditions array
    y0 = [x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3]

    # Time span for the simulation
    t_span = (0, 30)
    t_eval = np.linspace(*t_span, 1000)

    # Define the equations of motion
    def three_body_eq(t, y):
        x1, y1, x2, y2, x3, y3 = y[0:6]
        vx1, vy1, vx2, vy2, vx3, vy3 = y[6:12]
        r12 = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        r13 = np.sqrt((x3 - x1)**2 + (y3 - y1)**2)
        r23 = np.sqrt((x3 - x2)**2 + (y3 - y2)**2)
        
        ax1 = G * m2 * (x2 - x1) / r12**3 + G * m3 * (x3 - x1) / r13**3
        ay1 = G * m2 * (y2 - y1) / r12**3 + G * m3 * (y3 - y1) / r13**3
        
        ax2 = G * m1 * (x1 - x2) / r12**3 + G * m3 * (x3 - x2) / r23**3
        ay2 = G * m1 * (y1 - y2) / r12**3 + G * m3 * (y3 - y2) / r23**3
        
        ax3 = G * m1 * (x1 - x3) / r13**3 + G * m2 * (x2 - x3) / r23**3
        ay3 = G * m1 * (y1 - y3) / r13**3 + G * m2 * (y2 - y3) / r23**3
        
        return [vx1, vy1, vx2, vy2, vx3, vy3, ax1, ay1, ax2, ay2, ax3, ay3]

    # Solving the equations
    solution = solve_ivp(three_body_eq, t_span, y0, t_eval=t_eval, rtol=1e-9)
    x1_sol, y1_sol = solution.y[0], solution.y[1]
    x2_sol, y2_sol = solution.y[2], solution.y[3]
    x3_sol, y3_sol = solution.y[4], solution.y[5]

    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.grid()

    line1, = ax.plot([], [], 'o-', label="Body 1")
    line2, = ax.plot([], [], 'o-', label="Body 2")
    line3, = ax.plot([], [], 'o-', label="Body 3")

    trail1, = ax.plot([], [], 'r-', lw=0.5)
    trail2, = ax.plot([], [], 'b-', lw=0.5)
    trail3, = ax.plot([], [], 'g-', lw=0.5)

    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        line3.set_data([], [])
        trail1.set_data([], [])
        trail2.set_data([], [])
        trail3.set_data([], [])
        return line1, line2, line3, trail1, trail2, trail3

    def update(frame):
        # Update body positions as single-element lists
        line1.set_data([x1_sol[frame]], [y1_sol[frame]])
        line2.set_data([x2_sol[frame]], [y2_sol[frame]])
        line3.set_data([x3_sol[frame]], [y3_sol[frame]])
        
        # Update trails
        trail1.set_data(x1_sol[:frame], y1_sol[:frame])
        trail2.set_data(x2_sol[:frame], y2_sol[:frame])
        trail3.set_data(x3_sol[:frame], y3_sol[:frame])
        
        return line1, line2, line3, trail1, trail2, trail3

    ani = FuncAnimation(fig, update, frames=len(t_eval), init_func=init, blit=True)

    # Display the animation inline as HTML
    return HTML(ani.to_jshtml())

# Create sliders for the initial conditions
interact(
    three_body_simulation,
    x1=FloatSlider(value=0.970, min=-2, max=2, step=0.01, description='x1'),
    y1=FloatSlider(value=0.243, min=-2, max=2, step=0.01, description='y1'),
    x2=FloatSlider(value=-0.970, min=-2, max=2, step=0.01, description='x2'),
    y2=FloatSlider(value=-0.243, min=-2, max=2, step=0.01, description='y2'),
    vx1=FloatSlider(value=0.466, min=-1, max=1, step=0.01, description='vx1'),
    vy1=FloatSlider(value=-0.432, min=-1, max=1, step=0.01, description='vy1'),
    vx2=FloatSlider(value=0.466, min=-1, max=1, step=0.01, description='vx2'),
    vy2=FloatSlider(value=-0.432, min=-1, max=1, step=0.01, description='vy2')
)
