import math

def calculate_steps(num_elements):
    steps = math.log2(num_elements)
    return math.ceil(steps)

num_elements = 128

max_steps = calculate_steps(num_elements)
print(f"the maximum steps required is : {max_steps}")


