import csv

# Writing data to CSV
with open("traffic.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Time", "Vehicle_Count"])
    writer.writerow(["08:00", 100])
    writer.writerow(["09:00", 200])
    writer.writerow(["10:00", 150])
    writer.writerow(["17:00", 300])
    writer.writerow(["18:00", 350])

# Initialize variables
max_count = 0
peak_time = ""

# Reading data from CSV
with open("traffic.csv", "r") as f:
    rows = csv.DictReader(f)
    for row in rows:
        count = int(row["Vehicle_Count"])
        if count > max_count:
            max_count = count
            peak_time = row["Time"]

# Writing result to new CSV
with open("traffic_result.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Peak_Time", "Max_Vehicles"])
    writer.writerow([peak_time, max_count])

print("Traffic analysis complete!")