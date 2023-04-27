from print_color import print
import requests
import os


# header for the script
def header():
    # go to https://fsymbols.com/generators/tarty/ and get the name of the tool in this font
    print("""
    ██╗░░██╗███████╗░█████╗░██████╗░░██████╗███████╗░█████╗░██╗░░░██╗██████╗░███████╗
    ██║░░██║██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔════╝
    ███████║█████╗░░███████║██║░░██║╚█████╗░█████╗░░██║░░╚═╝██║░░░██║██████╔╝█████╗░░
    ██╔══██║██╔══╝░░██╔══██║██║░░██║░╚═══██╗██╔══╝░░██║░░██╗██║░░░██║██╔══██╗██╔══╝░░
    ██║░░██║███████╗██║░░██║██████╔╝██████╔╝███████╗╚█████╔╝╚██████╔╝██║░░██║███████╗
    ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝""", color='blue')
    print("""
                █▄▄ █▄█   █▄░█ █ █▄░█ ░░█ ▄▀█   █░█ ▄▀█ ▀█▀ ▀█▀ █▀█ █▀█ █
                █▄█ ░█░   █░▀█ █ █░▀█ █▄█ █▀█   █▀█ █▀█ ░█░ ░█░ █▄█ █▀▄ █""")


def header_check(url):
    # url = 'https://github.com'

    # Send a request to the URL
    response = requests.get(url)

    # Get the headers from the response
    headers = response.headers

    # List of all possible headers
    security_headers = ['X-Frame-Options', 'X-XSS-Protection', 'X-Content-Type-Options',
                        'Referrer-Policy', 'Content-Type', 'Set-Cookie', 'Strict-Transport-Security (HSTS)', 'Expect-CT',
                        'Content-Security-Policy', 'Access-Control-Allow-Origin', 'Cross-Origin-Opener-Policy', 'Cross-Origin-Embedder-Policy',
                        'Cross-Origin-Resource-Policy (CORP)', 'Permissions-Policy', 'Server', 'X-Powered-By', 'X-AspNet-Version', 'X-AspNetMvc-Version',
                        'X-DNS-Prefetch-Control', 'Public-Key-Pins (HPKP)']

    # Recommendations for security headers
    header_recom = {
        'X-Frame-Options': """Recommendations:
Use Content Security Policy (CSP) frame-ancestors directive if possible.
Do not allow displaying of the page in a frame.

\033[3m\033[4mX-Frame-Options: DENY\033[0m
""",
        'X-XSS-Protection': """Recommendations:
Use a Content Security Policy (CSP) that disables the use of inline JavaScript.
Do not set this header or explicitly turn it off.

\033[3m\033[4mX-XSS-Protection: 0\033[0m

Please see Mozilla X-XSS-Protection(https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection) for details.
""",
        'X-Content-Type-Options': """Recommendations:
Set the Content-Type header correctly throughout the site.

\033[3m\033[4mX-Content-Type-Options: nosniff\033[0m
""",
        'Referrer-Policy': """Recommendations:
Referrer policy has been supported by browsers since 2014. Today, the default behavior in modern browsers is to no longer send all referrer information (origin, path, and query string) to the same site but to only send the origin to other sites. However, since not all users may be using the latest browsers we suggest forcing this behavior by sending this header on all requests.

\033[3m\033[4mReferrer-Policy: strict-origin-when-cross-origin\033[0m

NOTE: For more information on configuring this header please see Mozilla Referrer-Policy(https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy).
""",
        'Content-Type': """Recommendations:
\033[3m\033[4mContent-Type: text/html; charset=UTF-8\033[0m

NOTE: the charset attribute is necessary to prevent XSS in HTML pages
NOTE: the text/html can be any of the possible MIME types(https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)
""",
        'Set-Cookie': """Recommendations:
Please read Session Management Cheat Sheet(https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#cookies) for a detailed explanation on cookie configuration options.
""",
        'Strict-Transport-Security (HSTS)': """Recommendations:
\033[3m\033[4mStrict-Transport-Security: max-age=63072000; includeSubDomains; preload\033[0m

NOTE: Read carefully how this header works before using it. If the HSTS header is misconfigured or if there is a problem with the SSL/TLS certificate being used, legitimate users might be unable to access the website. For example, if the HSTS header is set to a very long duration and the SSL/TLS certificate expires or is revoked, legitimate users might be unable to access the website until the HSTS header duration has expired.

Please checkout HTTP Strict Transport Security Cheat Sheet(https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html) for more information.
""",
        'Expect-CT': """Recommendations: 
Do not use it. Mozilla recommends(https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expect-CT) avoiding it, and removing it from existing code if possible.
""",
        'Content-Security-Policy': """Recommendations:
Content Security Policy is complex to configure and maintain. For an explanation on customization options, please read Content Security Policy Cheat Sheet(https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
""",
        'Access-Control-Allow-Origin': """Recommendations:
If you use it, set specific origins(https://developer.mozilla.org/en-US/docs/Glossary/Origin) instead of *. Checkout Access-Control-Allow-Origin(https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) for details.

\033[3m\033[4mAccess-Control-Allow-Origin: https://yoursite.com\033[0m

NOTE: The use '' might be necessary depending on your needs. For example, for a public API that should be accessible from any origin, it might be necessary to allow ''.
""",
        'Cross-Origin-Opener-Policy': """Recommendations:
Isolates the browsing context exclusively to same-origin documents.

\033[3m\033[4mHTTP Cross-Origin-Opener-Policy: same-origin\033[0m
""",
        'Cross-Origin-Embedder-Policy': """Recommendations:
A document can only load resources from the same origin, or resources explicitly marked as loadable from another origin.

\033[3m\033[4mCross-Origin-Embedder-Policy: require-corp\033[0m

NOTE: you can bypass it for specific resources by adding the crossorigin attribute:
<img src="https://thirdparty.com/img.png" crossorigin>
""",
        'Cross-Origin-Resource-Policy (CORP)': """Recommendations:
Limit current resource loading to the site and sub-domains only.

\033[3m\033[4mCross-Origin-Resource-Policy: same-site\033[0m
""",
        'Permissions-Policy': """Recommendations:
Set it and disable all the features that your site does not need or allow them only to the authorized domains:

\033[3m\033[4mPermissions-Policy: geolocation=() camera=(), microphone=()\033[0m

NOTE: This example is disabling geolocation, camera, and microphone for all domains.
""",
        'Server': """Recommendations:
Remove this header or set non-informative values.

\033[3m\033[4mServer: webserver\033[0m

NOTE: Remember that attackers have other means of fingerprinting the server technology.
""",
        'X-Powered-By': """Recommendations:
Remove all X-Powered-By headers.

NOTE: Remember that attackers have other means of fingerprinting your tech stack.
""",
        'X-AspNet-Version': """Recommendations:
Disable sending this header. Add the following line in your web.config in the <system.web> section to remove it.

\033[3m\033[4m<httpRuntime enableVersionHeader="false" />\033[0m

NOTE: Remember that attackers have other means of fingerprinting your tech stack.
""",
        'X-AspNetMvc-Version': """Recommendations:
Disable sending this header. To remove the X-AspNetMvc-Version header, add the below line in Global.asax file.

\033[3m\033[4mMvcHandler.DisableMvcResponseHeader = true;\033[0m

NOTE: Remember that attackers have other means of fingerprinting your tech stack.
""",
        'X-DNS-Prefetch-Control': """Recommendations:
The default behavior of browsers is to perform DNS caching which is good for most websites. If you do not control links on your website, you might want to set off as a value to disable DNS prefetch to avoid leaking information to those domains.

\033[3m\033[4mX-DNS-Prefetch-Control: off\033[0m

NOTE: Do not rely in this functionality for anything production sensitive: it is not standard or fully supported and implementation may vary among browsers.
""",
        'Public-Key-Pins (HPKP)': """Recommendations:
This header is deprecated and should not be used anymore.
"""
    }

    for header in security_headers:
        if header in headers:
            print(f"{header}: {headers[header]}", color="red", format="bold")
            print(f"{header_recom[header]}", color="green", format="bold")
        else:
            print(f"{header} header not found.", color="red", format="bold")
            print(f"{header_recom[header]}", color="green", format="bold")


# main function
if __name__ == "__main__":
    os.system("")
    header()
    print("\n\n")
    try:
        url = host = str(input("Enter URL: "))
        header_check(url)
    except KeyboardInterrupt:
        done = True
        print("\r!!KEYBOARD INTERRUPT!!")
