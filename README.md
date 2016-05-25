# Multithreaded-Webserver-and-Client
Environment
1.	Python 2.7.10
2.	Mozilla firefox 41.0.2
3.	Windows command prompt
4.	8080 is the default port
Files
1.	webserver.py (Server code)
2.	client.py(Client side code)
3.	test.html (used as the test file)
4.	All the files are in the same folder
Running webserver.py on command prompt
1.	webserver.py  <port_no>  (In the localhost ip creates the <port_no> & listens for clients)
2.	webserver.py   (In the localhost ip creates the 8080 as default port & listens for clients)
Running webserver.py on phyton IDE
1.	On Python 2.7.10 IDE -> open module->f5 or run
Testing in browser
1.	http://127.0.0.1:8080/test.html
2.	http://localhost:8080/test.html
3.	If file name is different 404 is sent
Running client.py on command prompt
1.	client.py 127.0.0.1 test.html
2.	client.py localhost test.html
3.	client.py localhost <port no> test.html
4.	wrong file name gives a 404
5.	wrong port number raises an error
