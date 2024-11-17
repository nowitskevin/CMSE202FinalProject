# CMSE202FinalProject
3 body problem for CMSE202 final project.

  The 3 body problem is a long-studied “unsolved problem” in physics. It involves 3 masses orbiting each other through an inverse square attractive force (usually gravity) which is not solvable analytically because of the coupled nonlinear differential equations. The resulting motion is chaotic, although hundreds of stable orbit initial conditions have been found experimentally. A large area of chaos theory includes numerically solving these systems and characterizing them. In this repository, the numerical aspect of the three body problem is examined. Two different numerical methods, Euler’s method and Runge-Kutta 4th order numerical integration are used. The Runge-Kutta method is used within the context of the scipy package solve_ivp function, while the Euler’s method is explicitly implemented. The code uses a famous stable orbit, the figure-eight orbit, and animates it side-by-side for Euler’s method and Runge-Kutta and also shows the energy oscillations (kinetic, potential, total). The scale of the simulation is not accurate to any celestial system, rather it is simple to aid in computation. The total energy of the system of planets is conserved as a physical law. The planets’ attributes are contained within the structure of the planet class, and the plotting is wrapped in an animation function which works on Jupyter notebook. Furthermore, the stability index of the orbit, the Lyapunov exponent, is calculated for the Runge-Kutta orbit, which is found to be 0.2, which means it is very stable, where 0 is perfectly stable. The Lyapunov exponent was calculated through an astrophysics library package for Python. The absolute error between the two numerical methods is found and plotted throughout the orbit. It can be seen through the numerical error accumulation and the instability of the oscillations in energy that the Runge-Kutta method is more stable in the long-term and a more accurate numerical integrator than Euler, which was expected because of the increased intermediate calculations in the time step. The Lyapunov constant was not zero which indicates that the regular oscillations of the energy within the figure 8 contribute to the “chaos” of the orbit, however the chaotic nature of this particular orbit is likely only inherent due to the nonzero numerical error of Runge-Kutta. For non-stable orbit configurations, the code has collision handling but the numerical error in both methods especially when the displacement is low and thus the gravity is very high results in non-conserved total energy, which is not physically correct, but is a consequence of the computational tool. The code also has no elastic or inelastic collision handling (linear nor angular momentum analysis) and is just confined to 2D space. We have shown through the animations that Runge-Kutta is the more stable integrator, and have also inherently shown some limitations in computational ability of this chaotic and complex system. 

Instructions for this repo:
combined.ipynb is the chief animation notebook which has the full Euler and RK4 animation with energy plots. It can be run as is or the initial conditions modified. It works best on Jupyter notebook because of the animation function, which would be different for a non-Jupyter environment. 


Nityaansh Parekh
Kevin Eisenberg - class definition, Euler's method animation with energy graph 
Dakshesh Ravi - Lyapunov exponent calculation
Jose Delgado
Fatih Imamoglu - RK4 animation, combining Euler and RK4 into one combined.ipynb
