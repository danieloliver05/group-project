import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# SIR model differential equations
def sir_model(y, t, beta, alpha):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - alpha * I
    dRdt = alpha * I
    return dSdt, dIdt, dRdt

# Total population, initial number of infected and recovered individuals, and initial susceptible individuals
N = 1000
I0 = 50
R0 = 0
S0 = N - I0 - R0

# Contact rate, beta, and mean recovery rate, alpha
beta = 0.2
alpha = 0.4

# Time vector
t = np.linspace(0, 160, 160)

# Initial conditions vector
y0 = S0, I0, R0

# Integrate the SIR equations over the time grid, t.
solution = odeint(sir_model, y0, t, args=(beta, alpha))
S, I, R = solution.T

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(t, S, 'b', label='Susceptible')
plt.plot(t, I, 'r', label='Infected')
plt.plot(t, R, 'g', label='Recovered')
plt.xlabel('Time (days)')
plt.ylabel('Number of individuals')
plt.title('SIR Model')
plt.legend()
plt.grid(True)
plt.show()

