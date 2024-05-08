def testing_GraphQL():
    print("testing_GraphQL...")


process_steps = {
    '1': testing_GraphQL
}

while True:
    print("\nMain Menu:")
    print("1. testing_GraphQL")
    print("E. Exit")

    option = input("Enter an option: ").strip()

    if option == 'E' or option == 'e':
        break

    if option in process_steps:
        print(process_steps[option].__name__)
        process_steps[option]()
    else:
        print("Invalid option. Please try again.")