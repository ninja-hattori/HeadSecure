import requests



#header for the script
def header():
    #go to https://fsymbols.com/generators/tarty/ and get the name of the tool in this font
    print("""
    ██╗░░██╗███████╗░█████╗░██████╗░░██████╗███████╗░█████╗░██╗░░░██╗██████╗░███████╗
    ██║░░██║██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔════╝
    ███████║█████╗░░███████║██║░░██║╚█████╗░█████╗░░██║░░╚═╝██║░░░██║██████╔╝█████╗░░
    ██╔══██║██╔══╝░░██╔══██║██║░░██║░╚═══██╗██╔══╝░░██║░░██╗██║░░░██║██╔══██╗██╔══╝░░
    ██║░░██║███████╗██║░░██║██████╔╝██████╔╝███████╗╚█████╔╝╚██████╔╝██║░░██║███████╗
    ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝""")
    print("""
    █▄▄ █▄█   █▄░█ █ █▄░█ ░░█ ▄▀█   █░█ ▄▀█ ▀█▀ ▀█▀ █▀█ █▀█ █
    █▄█ ░█░   █░▀█ █ █░▀█ █▄█ █▀█   █▀█ █▀█ ░█░ ░█░ █▄█ █▀▄ █""")


def header_check():
    url = 'https://github.com'

    # Send a request to the URL
    response = requests.get(url)

    # Get the headers from the response
    headers = response.headers
    # security_headers = ['X-Frame-Options', 'X-XSS-Protection', 'Strict-Transport-Security',
    #                 'X-Content-Type-Options', 'Content-Security-Policy']
    for header in headers:
        if header in headers:
            print(f"{header}: {headers[header]}")
        else:
            print(f"{header} header not found.")
    # for header in headers:
    #     print(header)

    # # Check if security headers are present
    # security_headers = []
    # for header in headers:
    #     if header.startswith('X-Frame-Options') or \
    #     header.startswith('X-XSS-Protection') or \
    #     header.startswith('Strict-Transport-Security') or \
    #     header.startswith('X-Content-Type-Options') or \
    #     header.startswith('Referrer-Policy') or \
    #     header.startswith('Content-Type') or \
    #     header.startswith('Set-Cookie') or \
    #     header.startswith('Strict-Transport-Security') or \
    #     header.startswith('Access-Control-Allow-Origin') or \
    #     header.startswith('Cross-Origin-Opener-Policy') or \
    #     header.startswith('Cross-Origin-Embedder-Policy') or \
    #     header.startswith('Content-Security-Policy'):
    #         security_headers.append(header)

    # # Print the security headers, if present
    # if security_headers:
    #     print('Security headers found:')
    #     for header in security_headers:
    #         print(header)
    # else:
    #     print('No security headers found.')

#main function
if __name__ == "__main__":
    # header()
    print("\n\n")
    try:
        # url=host=str(input("Enter URL: "))
        header_check()
    except KeyboardInterrupt:
            done=True
            print("\r!!KEYBOARD INTERRUPT!!")