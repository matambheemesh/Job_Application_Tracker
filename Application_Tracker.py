import json

applications = []

def load_data():
    global applications

    try:
        with open("applications.json", "r") as file:
            applications = json.load(file)

    except FileNotFoundError:
        applications = []

load_data()





def save_data():
    with open("applications.json", "w") as file:
        json.dump(applications, file, indent=4)
    

def add_application():
    company = input("Enter the company name ")
    role = input("Enter the role applied for ")
    location = input("Enter the location of the job ")
    pacakge = input("Enter the package offered ")
    date_applied = input("Enter the date applied (YYYY-MM-DD) ")    
    print(" \nstatus options:")
    print("1.applied")
    print("2.Assessment")
    print("3.Interview") 
    print("4.Offer")
    print("5.Rejected")

    status_choice = input("Enter the status choice (1-5) ")
    
    status_map = {
        "1": "Applied", 
        "2": "Assessment",
        "3": "Interview",
        "4": "Offer",
        "5": "Rejected"
    }

    status = status_map.get(status_choice, "Applied")

    application = {
        "company": company,
        "role": role,
        "location": location,
        "package": pacakge,
        "date_applied": date_applied,
        "status": status
    }
    applications.append(application)
    save_data()
    print("\n Application added successfully!")


def view_applications():
    if len(applications) == 0:
        print("No applications found.")
        return
    print("\n ======All Applications=======")
    for i, app in enumerate(applications, start=1):
        print("-"*40)
        print(f"\nApplication {i}:")
        print(f"  Company: {app['company']}")
        print(f"  Role: {app['role']}")
        print(f"  Location: {app['location']}")
        print(f"  Package: {app['package']}")
        print(f"  Date Applied: {app['date_applied']}")
        print(f"  Status: {app['status']}")
    print("-"*40)



def search_application():
    company_name = input("Enter the company name to search: ")
    found = False
    for app in applications:
        if app['company'].lower() == company_name.lower():
            print("\nApplication found:")
            print(f"  Company: {app['company']}")
            print(f"  Role: {app['role']}")
            print(f"  Location: {app['location']}")
            print(f"  Package: {app['package']}")
            print(f"  Date Applied: {app['date_applied']}")
            print(f"  Status: {app['status']}")
            found = True
            break
    if not found:
        print("Application not found.")


def update_status():
    company_name = input("Enter the company name to update status: ")
    for app in applications:
        if app['company'].lower() ==company_name.lower():
            print("\nCurrent status:", app['status'])
            print(" \nstatus options:")
            print("1.applied")
            print("2.Assessment")
            print("3.Interview") 
            print("4.Offer")
            print("5.Rejected")

            status_choice = input("Enter the new status choice (1-5) ")
    
            status_map = {
                "1": "Applied", 
                "2": "Assessment",
                "3": "Interview",
                "4": "Offer",
                "5": "Rejected"
            }

            new_status = status_map.get(status_choice, app['status'])
            app['status'] = new_status
            save_data()
            print("\nStatus updated successfully!")
            return
        print("Application not found.")


def delete_application():
    comapny_name = input("Enter the company name to delete application: ")
    for app in applications:
        if app['company'].lower() == comapny_name.lower():
            applications.remove(app)
            save_data()
            print("\nApplication deleted successfully!")
            return
    print("Application not found.")


def show_statistics():
    for app in applications:
        status_count = {}
        for app in applications:
            status = app['status']
            if status in status_count:
                status_count[status] += 1
            else:
                status_count[status] = 1
    print("\nApplication Statistics:")
    print(f"Total Applications: {len(applications)}")
    for status, count in status_count.items():
        print(f"  {status}: {count}")       

while True:

    print("\n")
    print("=" * 40)
    print("WELCOME TO JOB APPLICATION TRACKER")
    print("=" * 40)

    print("1. Add Application")
    print("2. View Applications")
    print("3. Search Application")
    print("4. Update Status")
    print("5. Delete Application")
    print("6. Dashboard Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_application()
        input("\nPress Enter To Continue...")

    elif choice == "2":
        view_applications()
        input("\nPress Enter To Continue...")

    elif choice == "3":
        search_application()
        input("\nPress Enter To Continue...")

    elif choice == "4":
        update_status()
        input("\nPress Enter To Continue...")

    elif choice == "5":
        delete_application()
        input("\nPress Enter To Continue...")

    elif choice == "6":
        show_statistics()
        input("\nPress Enter To Continue...")

    elif choice == "7":
        print("Thank you for using Job Application Tracker!")
        break

    else:
        print("Invalid Choice. Try Again.")
