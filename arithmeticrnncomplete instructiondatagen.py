import random
import numpy as np
from sympy import symbols, Poly, lcm, gcd, div, roots

def generate_arithmetic_data(digits, num_samples):
    data = []
    for _ in range(num_samples):
        a = random.randint(10**(digits-1), 10**digits - 1)
        b = random.randint(10**(digits-1), 10**digits - 1)
        
        # Addition
        result_add = a + b
        
        # Subtraction
        result_sub = a - b
        
        # Division
        result_div = None
        if b != 0:
            result_div = a / b
        
        # LCM
        result_lcm = lcm(a, b)
        
        # GCD
        result_gcd = gcd(a, b)
        
        # HCF
        result_hcf = result_gcd
        
        # Multiplication
        result_mul = a * b
        
        # Polynomial Roots
        x = symbols('x')
        polynomial = Poly(x**2 + a*x + b, x)
        result_poly_roots = roots(polynomial)
        
        data.append((a, b, result_add, result_sub, result_div, result_lcm, result_gcd, result_hcf, result_mul, result_poly_roots))
        
    return data

digits = 2  # Number of digits in the generated numbers
num_samples = 1000  # Number of examples to generate

data = generate_arithmetic_data(digits, num_samples)

# Print the generated data
for example in data:
    a, b, result_add, result_sub, result_div, result_lcm, result_gcd, result_hcf, result_mul, result_poly_roots = example
    print(f"Inputs: {a}, {b}")
    print(f"Addition: {result_add}")
    print(f"Subtraction: {result_sub}")
    print(f"Division: {result_div}")
    print(f"LCM: {result_lcm}")
    print(f"GCD: {result_gcd}")
    print(f"HCF: {result_hcf}")
    print(f"Multiplication: {result_mul}")
    print(f"Polynomial Roots: {result_poly_roots}")
    print()

