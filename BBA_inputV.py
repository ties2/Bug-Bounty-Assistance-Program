def test_reflected_cross_site_scripting():
    """Testing for Reflected Cross Site Scripting."""
    print("Testing for Reflected Cross Site Scripting...")

def test_stored_cross_site_scripting():
    """Testing for Stored Cross Site Scripting."""
    print("Testing for Stored Cross Site Scripting...")

def test_http_verb_tampering():
    """Testing for HTTP Verb Tampering."""
    print("Testing for HTTP Verb Tampering...")

def test_http_parameter_pollution():
    """Testing for HTTP Parameter Pollution."""
    print("Testing for HTTP Parameter Pollution...")

def test_sql_injection():
    """Testing for SQL Injection."""
    print("Testing for SQL Injection...")

def test_oracle():
    """Testing for Oracle."""
    print("Testing for Oracle...")

def test_mysql():
    """Testing for MySQL."""
    print("Testing for MySQL...")

def test_sql_server():
    """Testing for SQL Server."""
    print("Testing for SQL Server...")

def test_postgresql():
    """Testing for PostgreSQL."""
    print("Testing for PostgreSQL...")

def test_ms_access():
    """Testing for MS Access."""
    print("Testing for MS Access...")

def test_nosql_injection():
    """Testing for NoSQL Injection."""
    print("Testing for NoSQL Injection...")

def test_orm_injection():
    """Testing for ORM Injection."""
    print("Testing for ORM Injection...")

def test_client_side():
    """Testing for Client-side."""
    print("Testing for Client-side...")

def test_ldap_injection():
    """Testing for LDAP Injection."""
    print("Testing for LDAP Injection...")

def test_xml_injection():
    """Testing for XML Injection."""
    print("Testing for XML Injection...")

def test_ssi_injection():
    """Testing for SSI Injection."""
    print("Testing for SSI Injection...")

def test_xpath_injection():
    """Testing for XPath Injection."""
    print("Testing for XPath Injection...")

def test_imap_smtp_injection():
    """Testing for IMAP SMTP Injection."""
    print("Testing for IMAP SMTP Injection...")

def test_code_injection():
    """Testing for Code Injection."""
    print("Testing for Code Injection...")

def test_local_file_inclusion():
    """Testing for Local File Inclusion."""
    print("Testing for Local File Inclusion...")

def test_remote_file_inclusion():
    """Testing for Remote File Inclusion."""
    print("Testing for Remote File Inclusion...")

def test_command_injection():
    """Testing for Command Injection."""
    print("Testing for Command Injection...")

def test_format_string_injection():
    """Testing for Format String Injection."""
    print("Testing for Format String Injection...")

def test_incubated_vulnerability():
    """Testing for Incubated Vulnerability."""
    print("Testing for Incubated Vulnerability...")

def test_http_splitting_smuggling():
    """Testing for HTTP Splitting Smuggling."""
    print("Testing for HTTP Splitting Smuggling...")

def test_http_incoming_requests():
    """Testing for HTTP Incoming Requests."""
    print("Testing for HTTP Incoming Requests...")

def test_host_header_injection():
    """Testing for Host Header Injection."""
    print("Testing for Host Header Injection...")

def test_server_side_template_injection():
    """Testing for Server-side Template Injection."""
    print("Testing for Server-side Template Injection...")

def test_server_side_request_forgery():
    """Testing for Server-Side Request Forgery."""
    print("Testing for Server-Side Request Forgery...")

process_steps = {
    '1': test_reflected_cross_site_scripting,
    '2': test_stored_cross_site_scripting,
    '3': test_http_verb_tampering,
    '4': test_http_parameter_pollution,
    '5': test_sql_injection,
    '5.1': test_oracle,
    '5.2': test_mysql,
    '5.3': test_sql_server,
    '5.4': test_postgresql,
    '5.5': test_ms_access,
    '5.6': test_nosql_injection,
    '5.7': test_orm_injection,
    '5.8': test_client_side,
    '6': test_ldap_injection,
    '7': test_xml_injection,
    '8': test_ssi_injection,
    '9': test_xpath_injection,
    '10': test_imap_smtp_injection,
    '11': test_code_injection,
    '11.1': test_local_file_inclusion,
    '11.2': test_remote_file_inclusion,
    '12': test_command_injection,
    '13': test_format_string_injection,
    '14': test_incubated_vulnerability,
    '15': test_http_splitting_smuggling,
    '16': test_http_incoming_requests,
    '17':test_host_header_injection,
    '18': test_server_side_template_injection,
    '19': test_server_side_request_forgery
}

while True:
    print("\nMain Menu:")
    print("1. Testing for Reflected Cross Site Scripting")
    print("2. Testing for Stored Cross Site Scripting")
    print("3. Testing for HTTP Verb Tampering")
    print("4. Testing for HTTP Parameter Pollution")
    print("5. Testing for SQL Injection")
    print("5.1. Testing for Oracle")
    print("5.2. Testing for MySQL")
    print("5.3. Testing for SQL Server")
    print("5.4. Testing for PostgreSQL")
    print("5.5. Testing for MS Access")
    print("5.6. Testing for NoSQL Injection")
    print("5.7. Testing for ORM Injection")
    print("5.8. Testing for Client-side")
    print("6. Testing for LDAP Injection")
    print("7. Testing for XML Injection")
    print("8. Testing for SSI Injection")
    print("9. Testing for XPath Injection")
    print("10. Testing for IMAP SMTP Injection")
    print("11. Testing for Code Injection")
    print("11.1. Testing for Local File Inclusion")
    print("11.2. Testing for Remote File Injection")
    print("12. Testing for Command Injection")
    print("13. Testing for Format String Injection")
    print("14. Testing for Incubated Vulnerability")
    print("15. Testing for HTTP Splitting Smuggling")
    print("16. Testing for HTTP Incoming Requests")
    print("17. Testing for Host Header Injection")
    print("18. Testing for Server-side Template Injection")
    print("19. Testing for Server-Side Request Forgery")
    print("E. Exit")
    
    option = input("Enter an option: ").strip()

    if option == 'E' or option == 'e':
        break

    if option in process_steps:
        print(process_steps[option].__name__)
        process_steps[option]()
    else:
        print("Invalid option. Please try again.")