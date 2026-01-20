import math

# Define values (from assignment)
y_real = [100, 150, 200, 250, 300]
y_pred = [110, 140, 210, 240, 500]


# RMSE Function
def rmse(y_real, y_pred):
    sum = 0
    n = len(y_real)
    for i in range(n):
        sum += (y_pred[i] - y_real[i]) ** 2

    avg = sum / n

    return math.sqrt(avg)


# MAE Function
def mae(y_real, y_pred):
    sum = 0
    n = len(y_real)
    for i in range(n):
        sum += abs(y_pred[i] - y_real[i])

    return sum / n


# Print
print(f"MAE: {mae(y_real, y_pred):.2f}. RMSE: {rmse(y_real, y_pred):.2f}")

# Analysis print

print("")
