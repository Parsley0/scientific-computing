import sympy as sp

# QUESTION 1
# Define the function f(x) = 3x^2 + 2x - 5
x = sp.symbols('x')
L = 3*x**2 + 2*x - 5

L_prime = sp.diff(L, x)
print(f"First derivative (gradient) of L(x): {L_prime}")

optimal_x = sp.solve(L_prime, x)
print(f"Optimal solution (x when gradient is zero): {optimal_x}")

L_double_prime = sp.diff(L_prime, x)
print(f"Second derivative of L(x): {L_double_prime}")

second_derivative_at_optimal_x = L_double_prime.subs(x, optimal_x[0])
if second_derivative_at_optimal_x > 0:
    print(f"x = {optimal_x[0]} is a minimum.")
elif second_derivative_at_optimal_x < 0:
    print(f"x = {optimal_x[0]} is a maximum.")
else:
    print(f"x = {optimal_x[0]} is a saddle point.")

# QUESTION 2
# Define the feature matrix A
A = sp.Matrix([[2, 1], [1, 3]])

det_A = A.det()
print(f"Determinant of A: {det_A}")

eigenvalues = A.eigenvals()
print(f"Eigenvalues of A: {eigenvalues}")

char_poly = A.charpoly()
print(f"Characteristic polynomial of A: {char_poly.as_expr()}")

for eigenvalue in eigenvalues:
    verification = char_poly.as_expr().subs(x, eigenvalue)
    print(f"Verification for eigenvalue {eigenvalue}: {verification}")

 # QUESTION 3
    # Define the Laplace Transform H(s)
    s = sp.symbols('s')
    H = 1 / (s**2 + 3*s + 2)
    
    denominator_factors = sp.factor(s**2 + 3*s + 2)
    print(f"Factored denominator: {denominator_factors}")

    t = sp.symbols('t')
    h_t = sp.inverse_laplace_transform(H, s, t)
    print(f"Inverse Laplace Transform h(t): {h_t}")

    poles = sp.solve(s**2 + 3*s + 2, s)
    print(f"Poles of the system: {poles}")
    
    # QUESTION 4
    # Define the cost function C(x) = 5x^3 - 10x^2 + 4x + 3
    C = 5*x**3 - 10*x**2 + 4*x + 3

    C_prime = sp.diff(C, x)
    print(f"First derivative (gradient) of C(x): {C_prime}")

    optimal_x_C = sp.solve(C_prime, x)
    print(f"Optimal solution (x when gradient is zero): {optimal_x_C}")

    C_double_prime = sp.diff(C_prime, x)
    for sol in optimal_x_C:
        second_derivative_at_sol = C_double_prime.subs(x, sol)
        if second_derivative_at_sol > 0:
            print(f"x = {sol} is a minimum.")
        else:
            print(f"x = {sol} is a maximum.")
            
    # QUESTION 5
    # Define the encryption function C = P^e % N
    P, e, N = sp.symbols('P e N')
    C = P**e % N
    print(f"Symbolic encryption function C = P^e % N: {C}")

    P_val = 7
    e_val = 3
    N_val = 33
    C_val = pow(P_val, e_val, N_val)
    print(f"Ciphertext C for P=7, e=3, N=33: {C_val}")

    P_inverse = sp.mod_inverse(P_val, N_val)
    print(f"Modular inverse of P=7 mod N=33: {P_inverse}")

    decrypted_message = (C_val * P_inverse) % N_val
    print(f"Decrypted message: {decrypted_message}")