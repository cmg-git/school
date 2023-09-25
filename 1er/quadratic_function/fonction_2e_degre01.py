import numpy as np
import matplotlib.pyplot as plt

def second_degree(a, b, c):
    # Define a range of x values from -10 to 10 with a step of 1
    x = np.arange(-10, 11, 1)
    
    # Calculate f(x) = a*x**2 + b*x + c for each x
    f_x = a * x**2 + b * x + c

    # Calculate the discriminant Δ = b^2 - 4ac
    discriminant = b**2 - 4 * a * c
    
    # Find the roots of f(x) = 0 using the quadratic formula
    if discriminant > 0:
        root1 = (-b + np.sqrt(discriminant)) / (2 * a)
        root2 = (-b - np.sqrt(discriminant)) / (2 * a)
        print('Two real roots:')
        print('Root 1:', root1)
        print('Root 2:', root2)
    elif discriminant == 0:
        root1 = -b / (2 * a)
        print('One real root (double root):')
        print('Root:', root1)
    else:
        real_part = -b / (2 * a)
        imaginary_part = np.sqrt(-discriminant) / (2 * a)
        print('Two complex roots:')
        print('Root 1:', complex(real_part, imaginary_part))
        print('Root 2:', complex(real_part, -imaginary_part))
    print(f'Δ = {discriminant}')
    return x, f_x


def print_fx(x, f_x):
    # Print x and f(x) values
    for xi, fi in zip(x, f_x):
        print(f'x = {xi}, f(x) = {fi}')

def plot_fx(x, f_x):
    # Plot the function and points
    plt.plot(x, f_x, label='f(x) = {:.1f}x^2 + {:.1f}x + {:.1f}'.format(a, b, c))
    plt.plot(x, f_x, 'o', label='(x, f(x))')
    plt.axhline(0, color='red', linestyle='--', label='y = 0')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Plot of the Quadratic Function')
    plt.legend()
    plt.grid(True)
    # Draw a vertical line at x=0 (the y-axis)
    plt.axvline(x=0, color='red', linestyle='--', label='x = 0 (y-axis)')
    plt.show()

# Define the coefficients a, b, and c as float values
a = 1.0
b = -3.0
c = 2.0

x, f_x = second_degree(a, b, c)
print_fx(x, f_x)
plot_fx(x, f_x)