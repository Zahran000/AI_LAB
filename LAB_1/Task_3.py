n = int(input("Enter amount of numbers you want to enter: "))
numbers = [0] * n

for i in range(n):
    numbers[i] = int(input(f"Enter number {i+1}: "))

evens = 0
odds = 0

print("Numbers in the list:")
for num in numbers:
    print(num, end = ' ')
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

print(f"\nEven numbers: {evens}")
print(f"Odd numbers: {odds}")

index = int(input("\nEnter index of the element you want to replace: "))
new_value = int(input("Enter new value: "))
numbers[index] = new_value

print("\nupdated list:")
for num in numbers:
    print(num, end=' ')

