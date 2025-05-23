# --------------------------------------------
# Software Configuration Management System
# --------------------------------------------

import datetime
import os

# Step 1: Dictionary to track current versions
version_registry = {}

# Step 2: File to log version history
LOG_FILE = "version_log.txt"

# Step 3: Add or update software version
def add_version():
    software = input("Enter software/module name: ").strip()
    version = input("Enter new version (e.g., v1.2.0): ").strip()
    description = input("Enter description of update/modification: ").strip()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Update in-memory registry
    version_registry[software] = version

    # Append to log file
    try:
        with open(LOG_FILE, 'a') as log:
            log.write(f"{timestamp} | {software} updated to {version} | {description}\n")
        print(f"\n✅ Version for '{software}' updated to '{version}' and logged.")
    except Exception as e:
        print(f"❌ Failed to write to log file: {e}")

# Step 4: View current version status
def view_versions():
    print("\n📋 --- Current Software Versions ---")
    if not version_registry:
        print("No versions tracked yet.")
    else:
        for software, version in version_registry.items():
            print(f"🔹 {software}: {version}")

# Step 5: Show version history log
def view_log():
    print("\n📜 --- Version History Log ---")
    if not os.path.exists(LOG_FILE):
        print("Log file not found. No history available yet.")
        return

    with open(LOG_FILE, 'r') as log:
        content = log.read()
        if content.strip():
            print(content)
        else:
            print("Log is currently empty.")

# Step 6: Main menu-driven interface
def main():
    while True:
        print("\n🛠️ --- Configuration Management Menu ---")
        print("1. Add/Update Software Version")
        print("2. View Current Versions")
        print("3. View Version History Log")
        print("4. Exit")
        choice = input("Enter your choice (1–4): ").strip()

        if choice == '1':
            add_version()
        elif choice == '2':
            view_versions()
        elif choice == '3':
            view_log()
        elif choice == '4':
            print("👋 Exiting Configuration Management System. Goodbye!")
            break
        else:
            print("⚠️ Invalid input. Please choose between 1 and 4.")

# Step 7: Run the program
if __name__ == "__main__":
    main()
