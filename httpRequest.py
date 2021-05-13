#!/bin/python3

import socket
import sys
import ssl


def http_request():

    target_domain = sys.argv[1]
    choose_verb = sys.argv[2]
    port = sys.argv[3]
    port_integer = int(port)
    encoded_target_domain = target_domain.encode('utf-8')
    encoded_choose_verb = choose_verb.upper().encode('utf-8'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        if port_integer == 80:
            try:
                s.connect((target_domain, 80))
                try:
                    s.sendall(b"%s / HTTP/1.1\r\nHost: " % encoded_choose_verb + encoded_target_domain +
                              b"\r\n\r\n")
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
                    s_sock.sendall(b"%s / HTTP/1.1\r\nHost: " % encoded_choose_verb + encoded_target_domain +
                                   b"\r\n\r\n")
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


if __name__ == "__main__":
                                                     
    print("\n[+] Preparing to send HTTP request...\n")
    http_request()
