import csv
import os

# ---------- FILE SETUP ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE_NAME = os.path.join(DATA_DIR, "job_applications.csv")


def setup():
    """Create data folder and CSV file if they don't exist"""
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Company", "Role", "Date", "Status"])


# ---------- CORE FEATURES ----------
def add_job():
    print("\n➕ Add New Job Application")
    company = input("Company Name: ")
    role = input("Job Role: ")
    date = input("Applied Date (DD-MM-YYYY): ")
    status = "Applied"

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([company, role, date, status])

    print("✅ Job added successfully!")


def view_jobs():
    print("\n📄 Job Applications List\n")

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        found = False
        for row in reader:
            found = True
            print(
                f"Company: {row[0]} | Role: {row[1]} | "
                f"Date: {row[2]} | Status: {row[3]}"
            )

        if not found:
            print("No job applications found.")


def update_status():
    company_name = input("\nEnter company name to update status: ")
    updated_rows = []
    found = False

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if row[0].lower() == company_name.lower():
                print(f"Current Status: {row[3]}")
                row[3] = input("New Status (Interview / Rejected / Offer): ")
                found = True
            updated_rows.append(row)

    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(updated_rows)

    if found:
        print("🔄 Status updated successfully!")
    else:
        print("❌ Company not found.")


# ---------- MAIN MENU ----------
def menu():
    setup()

    while True:
        print("\n===== SMART JOB APPLICATION TRACKER =====")
        print("1. Add Job")
        print("2. View Jobs")
        print("3. Update Job Status")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            update_status()
        elif choice == "4":
            print("👋 Exiting application. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


# ---------- PROGRAM START ----------
if __name__ == "__main__":
    menu()
