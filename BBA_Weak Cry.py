def testing_for_Weak_Transport_Layer_Security():
    print("testing_for_Weak_Transport_Layer_Security...")

def testing_for_Padding_Oracle():
    print("testing_for_Padding_Oracle...")

def testing_for_Sensitive_Information_Sent_via_Unencrypted_Channels():
    print("testing_for_Sensitive_Information_Sent_via_Unencrypted_Channels...")

def testing_for_Weak_Encryption():
    print("testing_for_Weak_Encryption...")

process_steps = {
    '1': testing_for_Weak_Transport_Layer_Security,
    '2': testing_for_Padding_Oracle,
    '3': testing_for_Sensitive_Information_Sent_via_Unencrypted_Channels,
    '4': testing_for_Weak_Encryption,
}

while True:
    print("\nMain Menu:")
    print("1. testing_for_Weak_Transport_Layer_Security")
    print("2. testing_for_Padding_Oracle")
    print("3. testing_for_Sensitive_Information_Sent_via_Unencrypted_Channels")
    print("4. testing_for_Weak_Encryption")
    print("E. Exit")

    option = input("Enter an option: ").strip()

    if option == 'E' or option == 'e':
        break

    if option in process_steps:
        print(process_steps[option].__name__)
        process_steps[option]()
    else:
        print("Invalid option. Please try again.")