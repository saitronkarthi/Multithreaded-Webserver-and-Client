#UTA Id: 1001267157
#Name: Karthikeyan Rajamani
##References
##1.Skeleton code provided for phyton
##2.https://docs.python.org/2/howto/sockets.html
##3.https://bedfordsarah.wordpress.com/2013/10/29/python-socket-programming-project-1-http-web-server/
##4.http://www.wellho.net/resources/ex.php4?item=y303/browser.py
##5.http://bytes.com/topic/python/answers/932033-help-message-splitting-code
##6.https://docs.python.org/2/library/socket.html
##------------------------Program starts--------------------------------------------
from socket import * #import the socket module
import time # for RTT
import sys  # forcommandline functions
import datetime
ClientSocket= socket(AF_INET, SOCK_STREAM) # IPV4 address, TCP stream
#print "The no of Args is:",len(sys.argv) #for debugging
if (len(sys.argv)==4): # if port no is provided
    IPaddress=str(sys.argv[1])
    Portno=int(sys.argv[2])
    filename=str(sys.argv[3])
if (len(sys.argv)==3):# if port no is not provided default it to 8080
    IPaddress=str(sys.argv[1])
    Portno=8080
    filename=str(sys.argv[2])
ServerPort=Portno
Host = IPaddress
endtime=0 # initialize to 0
#getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)
ClientSocket.connect((Host,ServerPort)) # connect to the Server ip with portno
print "TimeStamp",datetime.datetime.now(),"Request to", (gethostbyaddr(ClientSocket.getpeername()[0]))[0],(gethostbyaddr(ClientSocket.getpeername()[0]))[2]
print "Server Host Name:",(gethostbyaddr(ClientSocket.getpeername()[0]))[0]
print "Server Socket Family:",ClientSocket.family
print "Server Socket Type:",ClientSocket.type
print "Server Protocol:", ClientSocket.proto
print "Server Socket get Peer Name:", ClientSocket.getpeername()
print "Server Timeout:",ClientSocket.gettimeout()
output="" #initialize the o/p to be written as null
url_params=(IPaddress+str(ServerPort),('/'+filename))
url=" ".join(url_params)# form the URL similar to a browser request
#print "The URL is:", url # for debugging
starttime=time.time() # Start time for RTT
ClientSocket.send(url+"\n") # send the Url similar to the browser to the Server
print"Request sent to Server:", url
while True:
    response=ClientSocket.recv(2048) # receive the response from the server
    if (endtime==0): # capture time for the 1st response
        endtime=time.time()# end time for RTT
    if response=="":break # end of response
    sys.stdout.write(response) # write the response on console
RTT=endtime-starttime #RTT calculation
print "RTT is", RTT ,"Seconds"
ClientSocket.close   # close socket
