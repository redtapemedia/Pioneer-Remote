import sys
import telnetlib

HOST = "192.168.1.30"
PORT = "8102"

class Main:

    def _parse_argv( self ):
        try:
            self.PARAMS = sys.argv[1]
            print "some params"
        except:
            sys.exit("no params")

    def _send_command( self ):
        try:
            tn = telnetlib.Telnet(HOST,PORT)
            tn.write(self.PARAMS + "\r\n")
            tn.read_some()
            tn.close()
            print self.PARAMS
        except:
            print "Command Failed"

    def __init__( self ):
        self._parse_argv()
        self._send_command()

if ( __name__ == "__main__" ):
    Main()
