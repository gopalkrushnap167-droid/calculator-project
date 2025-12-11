def add_numbers():
    nums = list(map(float, input("Enter numbers separated by space: ").split()))
    return sum(nums)

def subtract_numbers():
    nums = list(map(float, input("Enter numbers separated by space: ").split()))
    result = nums[0]
    for n in nums[1:]:
        result -= n
    return result

def multiply_numbers():
    nums = list(map(float, input("Enter numbers separated by space: ").split()))
    result = 1
    for n in nums:
        result *= n
    return result

def divide_numbers():
    a = float(input("Enter dividend: "))
    b = float(input("Enter divisor: "))
    if b == 0:
        return "Error! Division by zero."
    return a / b

def modulus_numbers():
    a = float(input("Enter number: "))
    b = float(input("Enter modulus base: "))
    if b == 0:
        return "Error! Modulus by zero."
    return a % b

def percentage():
    a = float(input("Enter obtained value: "))
    b = float(input("Enter total value: "))
    return (a / b) * 100


while True:
    print("\n---- CALCULATOR ----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Percentage")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Result:", add_numbers())

    elif choice == 2:
        print("Result:", subtract_numbers())

    elif choice == 3:
        print("Result:", multiply_numbers())

    elif choice == 4:
        print("Result:", divide_numbers())

    elif choice == 5:
        print("Result:", modulus_numbers())

    elif choice == 6:
        print("Result:", percentage())

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
