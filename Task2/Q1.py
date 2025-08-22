# Right-angled triangle of '*'
def print_right_triangle(n=5):
    for i in range(1, n+1):
        print("*" * i)

# Number pyramid
def print_number_pyramid(n=5):
    for i in range(1, n+1):
        print(" "*(n-i) + " ".join(str(j) for j in range(1, i+1)))

# 8x8 Checkerboard
def print_checkerboard(size=8):
    for i in range(size):
        print("".join(("█" if (i+j)%2==0 else " ") for j in range(size)))

# Run all
print_right_triangle()
print()
print_number_pyramid()
print()
print_checkerboard()
