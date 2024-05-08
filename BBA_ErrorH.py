def testing_for_Improper_Error_Handling():
    print("testing_for_Improper_Error_Handling ...")

def testing_for_Stack_Traces():
    print("testing_for_Stack_Traces...")



process_steps = {
    '1': testing_for_Improper_Error_Handling,
    '2': testing_for_Stack_Traces,

}

while True:
    print("\nMain Menu:")
    print("1. testing_for_Improper_Error_Handling")
    print("2. testing_for_Stack_Traces")
    print("E. Exit")
    
    option = input("Enter an option: ").strip()

    if option == 'E' or option == 'e':
        break

    if option in process_steps:
        print(process_steps[option].__name__)
        process_steps[option]()
    else:
        print("Invalid option. Please try again.")