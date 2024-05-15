import json
import requests
from bs4 import BeautifulSoup, Comment
import socket
import subprocess
import re 


def WSTG_info():
    def conduct_search_engine_discovery():
        print("Conducting search engine discovery reconnaissance for information leakage...")
        


    #################################################################
    def fingerprint_web_server(url):
        print("Fingerprinting web server...")
        def fingerprint_web_server(url):
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
            }

            # Make a HEAD request to the root of the website
            response = requests.head(url, headers=headers, allow_redirects=False)

            # Check the server header
            server_header = response.headers.get('Server')
            if server_header:
                print(f"Server: {server_header}")

            # Check the X-Powered-By header
            x_powered_by_header = response.headers.get('X-Powered-By')
            if x_powered_by_header:
                print(f"X-Powered-By: {x_powered_by_header}")

            # Check the set-cookie header
            set_cookie_header = response.headers.get('Set-Cookie')
            if set_cookie_header:
                print(f"Set-Cookie: {set_cookie_header}")

            # Check the date header
            date_header = response.headers.get('Date')
            if date_header:
                print(f"Date: {date_header}")

            # Check the content-length header
            content_length_header = response.headers.get('Content-Length')
            if content_length_header:
                print(f"Content-Length: {content_length_header}")

            # Check the content-type header
            content_type_header = response.headers.get('Content-Type')
            if content_type_header:
                print(f"Content-Type: {content_type_header}")

        def telnet_test(host, port):
            """
            Test the web server using telnet.
            """
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((host, port))
                sock.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
                response = sock.recv(4096)
                sock.close()

                # Check for the server banner in the response
                match = re.search(r"Server: (\w+/\S+)", response.decode())
                if match:
                    print(f"Server: {match.group(1)}")
                else:
                    print("Server: Not found")

                # Print the response for debugging purposes
                print(f"Telnet response:\n{response.decode()}")

            except Exception as e:
                print(f"Error: {e}")

        def openssl_test(host, port):
            """
            Test the web server using openssl.
            """
            try:
                cmd = f"echo | openssl s_client -servername example.com -connect {host}:{port} 2>/dev/null | openssl x509 -noout -text | grep -A 2 'Server Name Indication'"
                process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, error = process.communicate()
                if error:
                    print(f"Error: {error.decode()}")
                else:
                    match = re.search(r"Server name: (\w+)", output.decode())
                    if match:
                        print(f"Server: {match.group(1)}")
                    else:
                        print("Server: Not found")

                # Print the response for debugging purposes
                print(f"Openssl response:\n{output.decode()}")

            except Exception as e:
                print(f"Error: {e}")

        def SANTA_test(host, port):
            """
            Test the web server using a custom method SANTA.
            """
            try:
                req = "GET / SANTA CLAUS/1.1\r\n\r\n"
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((host, port))
                sock.send(req.encode())
                response = sock.recv(4096)
                sock.close()

                # Check for the server banner in the response
                match = re.search(r"Server: (\w+/\S+)", response.decode())
                if match:
                    print(f"Server: {match.group(1)}")
                else:
                    print("Server: Not found")

                # Print the response for debugging purposes
                print(f"SANTA response:\n{response.decode()}")

            except Exception as e:
                print(f"Error: {e}")

    #################################################################
    def review_webserver_metafiles(domain):
        print("Reviewing webserver metafiles for information leakage...")
        #exiftool for auto search metadat
        metafiles = [
                "robots.txt",
                "sitemap.xml",
                "crossdomain.xml",
                "clientaccesspolicy.xml",
                "human.txt",
                "humans.txt",
                "favicon.ico",
                "favicon.png",
                "apple-touch-icon.png",
                "manifest.json",
                "browserconfig.xml",
                "site.webmanifest"
            ]

        base_url = f"http://{domain}"
        results = []

        for metafile in metafiles:
                url = f"{base_url}/{metafile}"
                try:
                    response = requests.get(url, timeout=5)
                    if response.status_code == 200:
                        results.append((metafile, url, response.text))
                except requests.exceptions.RequestException:
                    pass

        print(results)

        # Example usage
        # domain = "https://digimoviez.com/"

        if results:
            print(f"Web server metafiles for {domain}:")
            for metafile, url, content in results:
                print(f"\n{metafile}:")
                print(f"URL: {url}")
                print(f"Content: {content}")
        else:
            print(f"No web server metafiles found for {domain}.")
        query = f"site:{domain} ext:pdf OR ext:xls OR ext:xlsx OR ext:doc OR ext:docx intext:metadata"
        url = f"https://www.google.com/search?q={query}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        print(response.text)



    #################################################################
    def enumerate_applications_on_webserver():
        print("Enumerating applications on webserver...")
        
        # Example usage
        url = "http://example.com"
        ip_address = socket.gethostbyname(url)

        # Web Server Banner Enumeration
        def web_server_banner_enumeration(url):
            response = requests.get(url)
            print(f"Web Server Banner Enumeration for {url}")
            print(f"Server: {response.headers.get('server')}")
            print(f"X-Powered-By: {response.headers.get('x-powered-by')}")

        # HTTP Method Enumeration
        def http_method_enumeration(url):
            response = requests.options(url)
            print(f"HTTP Method Enumeration for {url}")
            print(f"Supported HTTP methods: {response.headers.get('allow')}")

        # HTTP Headers Enumeration
        def http_headers_enumeration(url):
            response = requests.get(url)
            print(f"HTTP Headers Enumeration for {url}")
            print(f"Headers: {response.headers}")

        # Web Application Fingerprinting
        def web_application_fingerprinting(url):
            response = requests.get(url)
            print(f"Web Application Fingerprinting for {url}")
            print(f"Title: {response.text[:50]}")

        # Content Discovery
        def content_discovery(url):
            response = requests.get(url)
            print(f"Content Discovery for {url}")
            print(f"Links: {[link.get('href') for link in response.html.find_all('a')]}")

        # Directories and Files Enumeration
        def directories_and_files_enumeration(url, wordlist):
            print(f"Directories and Files Enumeration for {url}")
            subprocess.run(["gobuster", "dir", "-u", url, "-w", wordlist], capture_output=True, text=True)

        # Robots.txt Enumeration
        def robots_txt_enumeration(url):
            response = requests.get(f"{url}/robots.txt")
            print(f"Robots.txt Enumeration for {url}")
            print(f"Disallowed URLs: {re.findall(r'Disallow: (.*)', response.text)}")

        # Server Response Analysis
        def server_response_analysis(url):
            print(f"Server Response Analysis for {url}")
            subprocess.run(["whatweb", url], capture_output=True, text=True)

        # Banner Grabbing
        def banner_grabbing(ip, port):
            print(f"Banner Grabbing for {ip}:{port}")
            subprocess.run(["nmap", "-p", str(port), "--script", "banner", ip], capture_output=True, text=True)

        process_steps = {
            '2': web_server_banner_enumeration,
            '3': http_method_enumeration,
            '4': http_headers_enumeration,
            '5': web_application_fingerprinting,
            '6': content_discovery,
            '7': directories_and_files_enumeration,
            '8': robots_txt_enumeration,
            '9': server_response_analysis,
            '10': banner_grabbing
        }

        while True:
            print("\nMain Menu:")
            print("1. web_server_banner_enumeration")
            print("2. http_method_enumeration")
            print("3. http_headers_enumeration")
            print("4. web_application_fingerprinting")
            print("5. content_discovery")
            print("6. directories_and_files_enumeration")
            print("7. robots_txt_enumeration")
            print("8. server_response_analysis")
            print("9. banner_grabbing")

            option = input("Enter an option: ").strip()

            if option == 'E' or option == 'e':
                break

            if option in process_steps:
                print(process_steps[option].__name__)
                process_steps[option]()
            else:
                print("Invalid option. Please try again.")

    #################################################################
    def review_webpage_content(url):
        print("Reviewing webpage content for information leakage...")
        #check comment of web application 
        # Fetch the HTML content of the web application
        response = requests.get(url)
        html_content = response.text

        # Find all single-line comments
        single_line_comments = re.findall(r'<!--.*?-->', html_content, re.DOTALL)
        print("Single-line comments:")
        for comment in single_line_comments:
            print(comment)

        # Find all multi-line comments
        multi_line_comments = re.findall(r'/\*(.*?)\*/', html_content, re.DOTALL)
        print("\nMulti-line comments:")
        for comment in multi_line_comments:
            print(comment)


    #################################################################
    def identify_application_entry_points():
        print("Identifying application entry points...")

    #################################################################    

    def map_execution_paths_through_application():
        print("Mapping execution paths through application...")


    #################################################################    

    def fingerprint_web_application_framework():
        print("Fingerprinting web application framework...")


    #################################################################    

    def fingerprint_web_application():
        print("Fingerprinting web application...")


    #################################################################
    def map_application_architecture():
        print("Mapping application architecture...")


    #################################################################
    def passive_Scanning_and_Assessment():
        print("Mapping application architecture...")


    #################################################################
    def active_Scanning_and_testing():
        print("Mapping application architecture...")


    #################################################################    

    ###############4.1 Information Gathering###############
    process_steps = {
                '1': conduct_search_engine_discovery,
                '2': fingerprint_web_server,
                '3': review_webserver_metafiles,
                '4': enumerate_applications_on_webserver,
                '5': review_webpage_content,
                '6': identify_application_entry_points,
                '7': map_execution_paths_through_application,
                '8': fingerprint_web_application_framework,
                '9': fingerprint_web_application,
                '10': map_application_architecture,
                '11': passive_Scanning_and_Assessment,
                '12': active_Scanning_and_testing
        }

    while True:
        print("\nMain Menu:")
        print("1. Conduct Search Engine Discovery Reconnaissance for Information Leakage")
        print("2. Fingerprint Web Server")
        print("3. Review Webserver Metafiles for Information Leakage")
        print("4. Enumerate Applications on Webserver")
        print("5. Review Webpage Content for Information Leakage")
        print("6. Identify Application Entry Points")
        print("7. Map Execution Paths Through Application")
        print("8. Fingerprint Web Application Framework")
        print("9. Fingerprint Web Application")
        print("10. Map Application Architecture")
        print("11. Passive Scanning and Assessment") 
        print("12. Active Scanning and Testing")
        print("E. Exit")

        option = input("Enter an option: ").strip()

        if option == 'E' or option == 'e':
            break

        if option in process_steps:
            print(process_steps[option].__name__)
            process_steps[option]()
        else:
            print("Invalid option. Please try again.")

