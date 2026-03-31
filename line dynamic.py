import matplotlib.pyplot as plt

# Number of data points
n = int(input("Enter number of data points: "))

x = []
y = []

# Taking user input
print("Enter X values:")
for i in range(n):
    value = float(input(f"X[{i+1}]: "))
    x.append(value)

print("Enter Y values:")
for i in range(n):
    value = float(input(f"Y[{i+1}]: "))
    y.append(value)

# Plotting the line chart
plt.plot(x, y, marker='o')
plt.xlabel("X-axis")
plt.ylabel("Y6-axis")
plt.title("Line Chart from User Input")
plt.grid(True)
plt.show()
