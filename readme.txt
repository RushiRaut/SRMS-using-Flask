SRMS System devloped in python Flask and MySQL workbench

1] You need to install MySQL workbench and to create database by imprting "srms.sql" file in workbench.
	-Go to src/connection.py file and change username and password according to your database connection created in workbench.
	
2] In order to run the application you need to install flask library and Mysql connection library.
	use command given below to insatll flask and mysql connection host.
	
	-> pip install flask
	-> pip install mysqlclient
	
3] to start the server either run app.py manually using 

	-> set FLASK_APP=app.py
	-> flask run
	
	or 
	
	directly run the following command
		-> .\config.bat
