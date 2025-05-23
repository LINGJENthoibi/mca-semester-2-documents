#lab_experiment 1
def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n-1, auxiliary, source, destination)
#example: Solve for 4 disks
n = 4
hanoi(n, 'A', 'B', 'C')

#lab_experiment 2
def exchange_values(a, b):
    return b, a
print("Enter two values:")
a = str(input("a: "))
b = str(input("b: "))
a, b = exchange_values(a, b)
print("After exchange:")
print("a:", a)
print("b:", b)
