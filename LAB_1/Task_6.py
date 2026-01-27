user_input = input("Enter any string: ")

longest_count = 1
current_count = 1
longest_substring = user_input[0]

for index in range(1, len(user_input)):
    if user_input[index] == user_input[index - 1]:
        current_count += 1
    else:
        if current_count >= longest_count:
            longest_count = current_count
            longest_substring = user_input[index - 1] * current_count
        current_count = 1

if current_count >= longest_count:
    longest_count = current_count
    longest_substring = user_input[-1] * current_count

print("\nLongest sequence of same chars:", longest_substring)
print("Length of sequence:", longest_count)

