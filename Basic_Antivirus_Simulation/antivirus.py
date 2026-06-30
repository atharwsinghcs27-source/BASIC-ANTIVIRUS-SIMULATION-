import os
import shutil

# Load virus signatures
with open("virus_signatures.txt", "r") as f:
    signatures = [line.strip().lower() for line in f]

scan_folder = "TestFiles"
quarantine_folder = "Quarantine"

infected_files = []
total_files = 0

for file in os.listdir(scan_folder):

    total_files += 1

    filepath = os.path.join(scan_folder, file)

    try:
        with open(filepath, "r", errors="ignore") as f:
            content = f.read().lower()

            infected = False

            for sig in signatures:

                if sig in content:

                    infected_files.append(file)

                    shutil.move(
                        filepath,
                        os.path.join(quarantine_folder, file)
                    )

                    print(f"[THREAT DETECTED] {file}")

                    infected = True
                    break

            if not infected:
                print(f"[SAFE] {file}")

    except:
        print(f"Cannot scan {file}")

safe_files = total_files - len(infected_files)

with open("scan_report.txt", "w") as report:

    report.write("BASIC ANTIVIRUS SCAN REPORT\n\n")
    report.write(f"Total Files: {total_files}\n")
    report.write(f"Safe Files: {safe_files}\n")
    report.write(f"Infected Files: {len(infected_files)}\n\n")

    report.write("Detected Threats:\n")

    for file in infected_files:
        report.write(file + "\n")

print("\nScan Completed")
print("Report Generated")