# --------------------------------------------
# Software Quality Report Generator
# --------------------------------------------

def read_test_metrics(file_path):
    test_cases = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    case_id = parts[0].strip()
                    status = parts[1].strip().lower()  # "pass" or "fail"
                    try:
                        defects = int(parts[2].strip())    # ensure defects is an integer
                        test_cases.append((case_id, status, defects))
                    except ValueError:
                        print(f"⚠️ Skipped invalid defect count in line: {line.strip()}")
    except FileNotFoundError:
        print("⚠️ Error: File not found.")
    except Exception as e:
        print(f"⚠️ Error reading file: {e}")
    return test_cases

def generate_quality_report(test_cases):
    if not test_cases:
        print("No test data available.")
        return

    total = len(test_cases)
    passed = sum(1 for _, status, _ in test_cases if status == "pass")
    failed = sum(1 for _, status, _ in test_cases if status == "fail")
    total_defects = sum(defects for _, _, defects in test_cases)

    pass_rate = (passed / total) * 100
    fail_rate = (failed / total) * 100
    defect_density = total_defects / total if total > 0 else 0

    print("\n📊 --- SOFTWARE QUALITY REPORT ---")
    print(f"Total Test Cases     : {total}")
    print(f"✅ Passed             : {passed}")
    print(f"❌ Failed             : {failed}")
    print(f"✔️  Pass Rate (%)      : {pass_rate:.2f}")
    print(f"✖️  Fail Rate (%)      : {fail_rate:.2f}")
    print(f"🐞 Total Defects Found: {total_defects}")
    print(f"📉 Defect Density     : {defect_density:.2f} defects/test case")

def main():
    file_path = input("Enter the path to the test metrics file (e.g., test_metrics.txt): ").strip()
    test_cases = read_test_metrics(file_path)
    generate_quality_report(test_cases)

if __name__ == "__main__":
    main()
