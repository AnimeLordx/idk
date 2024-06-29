def generate_squares(n):
    for i in range(n):
        yield i**2

n = int(input("Squares of numbers up to: "))

squares = generate_squares(n)

for square in squares:
    print(square)