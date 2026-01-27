def duplicate(numbers_list):
    occurrence_count = [0] * len(numbers_list)
    
    for i in range(len(numbers_list)):
        current_number = numbers_list[i]
        for j in range(len(numbers_list)):
            if current_number == numbers_list[j]:
                occurrence_count[i] += 1

    duplicates = []
    for i in range(len(numbers_list)):
        if occurrence_count[i] > 1 and numbers_list[i] not in duplicates:
            duplicates.append(numbers_list[i])
    
    return duplicates

user_numbers = []
for i in range(10):
    user_input = int(input(f"Enter number {i+1}: "))
    user_numbers.append(user_input)

repeated_numbers = duplicate(user_numbers)

if repeated_numbers:
    print("\nThe following numbers are repeated more than once:")
    for number in repeated_numbers:
        print(f"- {number}")
else:
    print("\nNo numbers are repeated.")

