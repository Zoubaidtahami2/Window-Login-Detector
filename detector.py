import csv

failed = 0
night = 0

with open("sample_logs.txt", errors="ignore") as f:
    for line in f:

        if "Failure" in line:
            failed += 1

        if " 12:" in line or " 01:" in line or " 02:" in line or " 03:" in line or " 04:" in line:
            night += 1


print("===== ALERT REPORT =====")
print("Failed Logins:", failed)
print("Night Logins:", night)


with open("report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Type", "Count"])
    writer.writerow(["Failed", failed])
    writer.writerow(["Night", night])

print("Report saved as report.csv")

