import os 
import struct
import ipaddress

ua_file_path = r"C:\Users\Pavel Pablo\Desktop\UA1.txt"
log_file = r"C:\Users\Pavel Pablo\Desktop\dataset-1.log"

ua1 = open(ua_file_path) 
ua_cont = ua1.readlines()
ua1.close()

found_ips = open('found-ips.csv', 'w')

ips = set()

with open(log_file) as log:
    for line in log:
        for ua in ua_cont:
            if ua in line:
                # found = True
                ip_address = line[0:line.find(' ')]
                ip_packed = ipaddress.IPv4Address(ip_address).packed
                ip = struct.unpack('<L', ip_packed)[0]

                if ip not in ips:
                    ips.add(ip)
                    found_ips.write(ip_address + ',' + ua + '\n')

found_ips.close()                
