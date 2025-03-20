numbers = [int(faiz) for faiz in input("Enter the number and seperate with space: ").split()]

if numbers:
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    print("Largest number:", largest)
else:
    print("List is empty")
