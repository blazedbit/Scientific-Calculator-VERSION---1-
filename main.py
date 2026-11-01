# MENU DRIVEN FILE HERE

from function import addition, subtraction, multiplication, division, square_root, power, logarithm, sine, cosine, tangent, factorial, absolute_value, percentage, modulo, multiple_operations

while True:
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Logarithm")
    print("8. Multiple Operations")
    print("9. sine")
    print("10. cosine")
    print("11. tangent")
    print("12. factorial")
    print("13. absolute value")
    print("14. percentage")
    print("15. modulo")
    print("16. Exit")

    choice = input("Enter your choice (1-16): ")

    if choice == '1':        
        out = addition()
        print("The result of addition is:", out)
    elif choice == '2':
        out = subtraction()
        print("The result of subtraction is:", out)
    elif choice == '3':
        out = multiplication()
        print("The result of multiplication is:", out)
    elif choice == '4':
        out = division()
        print("The result of division is:", out)
    elif choice == '5':
        out = square_root()
        print("The result of square root is:", out)
    elif choice == '6':
        out = power()
        print("The result of power is:", out)
    elif choice == '7':
        out = logarithm()
        print("The result of logarithm is:", out)
    elif choice == '9':
        out = sine()
        print("The result of sine is:", out)
    elif choice == '10':
        out = cosine()
        print("The result of cosine is:", out)
    elif choice == '11':
        out = tangent()
        print("The result of tangent is:", out)
    elif choice == '12':
        out = factorial()
        print("The result of factorial is:", out)
    elif choice == '13':
        out = absolute_value()
        print("The result of absolute value is:", out)
    elif choice == '14':
        out = percentage()
        print("The result of percentage is:", out)
    elif choice == '15':
        out = modulo()
        print("The result of modulo is:", out)
    elif choice == '8':
        out = multiple_operations()
        print("The result of multiple operations is:", out)
    elif choice == '16':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
