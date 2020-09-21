import socket 
import re
import httplib2

class Status:
    


    def get_ip(self,host):
        try:
            ip = socket.gethostbyname(host)
            print(f'IP address is {ip}')

        except socket.gaierror:
            return f'< The website is not online currently>'

        else:
            return f'< The website is online>'


    def page_information(self,host,path="/"):
        try:
            conn = httplib2.HTTPSConnectionWithTimeout(host)
            conn.request("HEAD",path)

            if re.match("^[23]\d\d$",str(conn.getresponse().status)):
                return f' Website pages are available '

        except:
            return None


    

    