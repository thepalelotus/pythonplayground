import socket
import sys
import ssl


def http_request():

    target_domain = sys.argv[1]  # Get target domain using cli parameter, ex: <./getHEADRequest.py www.google.com HEAD>
    choose_verb = sys.argv[2]  # Choose HTTP verb to use. Consider using OPTIONS or HEAD.
    port = sys.argv[3]
    res = sys.argv[4]
    port_integer = int(port)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        if port_integer == 80:
            try:
                s.connect((target_domain, 80))
                try:
                    request = "%s %s HTTP/1.1\r\nHost:%s\r\n\r\n" % (choose_verb.upper(), res, target_domain)
                    s.sendall(request.encode('utf-8'))
                    try:
                        print("[+] Response received...\n")
                        print("\n", s.recv(2048).decode())
                    except socket.error as e:
                        print("[!] Failed to receive response: %s " % e, "\n")
                except socket.error as e:
                    print("[!] Failed to send HTTP data: %s " % e, "\n")
            except socket.gaierror as e:
                print("[!] Client could not connect: %s " % e, "\n")

        elif port_integer == 443:
            print("[!] Establishing an SSL socket.\n")
            wrapper = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            s_sock = wrapper.wrap_socket(s, server_hostname=target_domain)
            print("[*] SSL socket established. \n")
            try:
                s_sock.connect((target_domain, 443))
                try:
                    request = "%s %s HTTP/1.1\r\nHost:%s\r\n\r\n" % (choose_verb.upper(), res, target_domain)
                    s_sock.sendall(request.encode('utf-8'))
                    try:
                        print("[+] Response received...\n")
                        print("\n", s_sock.recv(2048).decode())
                    except socket.error as e:
                        print("[!] Failed to receive response: %s" % e, "\n")
                except socket.error as e:
                    print("[!] Failed to send HTTP data: %s" % e, "\n")
            except socket.gaierror as e:
                print("[!] Client could not connect: %s" % e, "\n")
        else:
            print("[?] No port specified. Try 80 or 443")

def main():
    print("\n[+] Preparing to send HTTP request...\n")
    http_request()
    print("\n[*] Finished with request.\n[-] Closed socket.\n")

if __name__ == "__main__":
    main()

