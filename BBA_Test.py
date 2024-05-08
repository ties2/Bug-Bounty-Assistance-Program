def vulnerability():
  # Define your functions
  def SQL_Injection():
      print("SQL_Injection")
  # ...

  # Create a dictionary to map vulnerability names to functions
  vulnerabilities = {
      "SQL Injection": SQL_Injection,
      # ...
  } 

  while True:
      # Print the menu
      for i, vulnerability_name in enumerate(vulnerabilities, start=1):
          print(f"{i}. {vulnerability_name}")
      
      # Ask the user to choose a vulnerability
      choice = int(input("Enter the number of a vulnerability to run, or 0 to exit: "))
      
      # Exit the loop if the user chooses 0
      if choice == 0:
          break
      
      # Get the chosen vulnerability name
      vulnerability_name = list(vulnerabilities.keys())[choice-1]
      
      # Run the chosen vulnerability
      vulnerabilities[vulnerability_name]()
