import time

# Defining the starting numbers
a, b = 0, 1

print("--- Starting the Fibonacci Sequence ---")

# This loop runs 20 times automatically without any input
for _ in range(20):
    print(a)
    # The math: next number is a + b
    a, b = b, a + b
    # Adding a small pause so it doesn't just flash on screen
    time.sleep(0.3)

print("--- Done! ---")