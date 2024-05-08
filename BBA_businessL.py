def introduction_to_Business_Logic():
    print("introduction_to_Business_Logic...")

def test_Business_Logic_Data_Validation():
    print("test_Business_Logic_Data_Validation...")

def test_Ability_to_Forge_Requests():
    print("test_Ability_to_Forge_Requests...")

def test_Integrity_Checks():
    print("test_Integrity_Checks...")

def test_Process_Timing():
    print("test_Process_Timing...")

def test_Number_of_Times_a_Function_Can_Be_Used_Limits():
    print("test_Number_of_Times_a_Function_Can_Be_Used_Limits...")

def testing_for_the_Circumvention_of_Work_Flows():
    print("testing_for_the_Circumvention_of_Work_Flows...")

def test_Defenses_Against_Application_Misuse():
    print("test_Defenses_Against_Application_Misuse...")

def test_Upload_of_Unexpected_File_Types():
    print("test_Upload_of_Unexpected_File_Types...")

def test_Upload_of_Malicious_Files():
    print("test_Upload_of_Malicious_Files...")

process_steps = {
    '1': introduction_to_Business_Logic,
    '2': test_Business_Logic_Data_Validation,
    '3': test_Ability_to_Forge_Requests,
    '4': test_Integrity_Checks,
    '5': test_Process_Timing,
    '6': test_Number_of_Times_a_Function_Can_Be_Used_Limits,
    '7': testing_for_the_Circumvention_of_Work_Flows,
    '8': test_Defenses_Against_Application_Misuse,
    '9': test_Upload_of_Unexpected_File_Types,
    '10': test_Upload_of_Malicious_Files,
}

while True:
    print("\nMain Menu:")
    print("1. Introduction to Business Logic")
    print("2. Test Business Logic Data Validation")
    print("3. Test Ability to Forge Requests")
    print("4. Test Integrity Checks")
    print("5. Test Process Timing")
    print("6. Test Number of Times a Function Can Be Used Limits")
    print("7. Testing for the Circumvention of Work Flows")
    print("8. Test Defenses Against Application Misuse")
    print("9. Test Upload of Unexpected File Types")
    print("10. Test Upload of Malicious Files")
    print("E. Exit")

    option = input("Enter an option: ").strip()

    if option == 'E' or option == 'e':
        break

    if option in process_steps:
        print(process_steps[option].__name__)
        process_steps[option]()
    else:
        print("Invalid option. Please try again.")