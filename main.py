import sys

sys.path.append("./src")

from invoicing_service import InvoicingService


def display_menu():
    print("Please choose the invoicing method:")
    print("1. Anonymous invoices")
    print("2. Named invoices")
    print("3. Exit")

    choice = input("\nEnter the number of your choice: ")

    return choice


def main():
    while True:
        user_choice = display_menu()

        if user_choice == "1":
            InvoicingService.anonymous_invoicing()
            break
        elif user_choice == "2":
            InvoicingService.named_invoicing()
            break
        elif user_choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please choose again.")


main()
