import socket
from requests import get
#Check If Port Is Open
def isOpen(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
                s.connect((ip, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                file=open("rzlt.txt", "a+")
                file.write(ip)
                file.write("\n +++++++++++++++++++++++++++++ Mamoun Benhafsa +++++++++++++++++++++++++++++\n")
                #return True
                print(ip[0],"Is up")
        except:
                #return False
                print("Is Down")
        finally:
                s.close()
##Range Ip Function ipRange
def ipRange(start_ip, end_ip):
   start = list(map(int, start_ip.split(".")))
   end = list(map(int, end_ip.split(".")))
   temp = start
   ip_range = []

   ip_range.append(start_ip)
   while temp != end:
      start[3] += 1
      for i in (3, 2, 1):
         if temp[i] == 256:
            temp[i] = 0
            temp[i-1] += 1
      ip_range.append(".".join(map(str, temp)))

   return ip_range
   pass
#main Start
Exteral_IP = get('https://api.ipify.org').text #get External Ip
From = raw_input("Put Start From Range>>")
To = raw_input("Put End Of Range>>")
ip_range = ipRange(From, To)
port = raw_input("Put Port To Check  in If It is Up >>")
print("Stating :) From",From,"To",To)
print("Your External Ip ",Exteral_IP)
ok = raw_input("press any Key To Start CTRL+C To Exit>>>")
for ip in ip_range:
        print("Check For ",ip)
        isOpen(ip,port)
