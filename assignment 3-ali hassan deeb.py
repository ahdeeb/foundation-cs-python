def count_tags(html_code, tag):
    return html_code.count(f'<{tag}>')

print("1. Count Digits")
print("2. Find Max")
print("3. Count Tags")
print("4. Exit")
print("------------")

while True:
    user_choice = input("Enter your choice: ")
    user_choice = int(user_choice)

    if user_choice == 1:
        count_number = input("Enter a number and we will calculate the sum of the characters: ")
        print(f"The number of characters is: {len(count_number)}")
    
    elif user_choice == 2:
        max_number = input("Enter a list of numbers separated by commas: ")
        numbers = [int(x) for x in max_number.split(",")]
        numbers.sort()  # Sorts the list in place
        print(f"The maximum number is: {numbers[-1]}")
    
    elif user_choice == 3:
        html_code = input("Enter the HTML code: ")  # Get HTML code from user
        tag = input("Enter the tag to count: ").strip()
        count = count_tags(html_code, tag)
        print(f"The tag <{tag}> occurs {count} times.")
    
    elif user_choice == 4:
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice. Please try again.")