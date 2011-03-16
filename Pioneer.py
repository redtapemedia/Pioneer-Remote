import telnetlib

HOST = "192.168.1.30"

tn = telnetlib.Telnet(HOST,8102)
tn.write("VU\r\n")

#tn.close()
