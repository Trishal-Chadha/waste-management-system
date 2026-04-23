from predict import predict_status

print("SMART WASTE MANAGEMENT SYSTEM")

fill = float(input("Enter Fill Level (%): "))
weight = float(input("Enter Weight (kg): "))
time = float(input("Enter Time (hours): "))

result = predict_status(fill, weight, time)

print(result)