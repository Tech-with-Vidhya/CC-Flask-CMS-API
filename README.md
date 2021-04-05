# Python-Flask-PostgreSQL-Content-Management-Web-System-with-User-Registration - APIs Implementation

A. Application Overview:

This project repository includes a Web-based Content (Articles) Management System/Application related to Data Science Learning and Career Journey with User Registration, Login functionalities using Python, Flask Web Framework, HTML, PostgreSQL database and Heroku Cloud Server.

This application is implemented and deployed in Heroku Cloud Server.


B. Application Functionalities:

1. New User Registration (First Name, Last Name, Email Address, Gender, Language, Password)
2. Existing User Login
3. User Management (Modify/Edit Existing User Details and Delete Existing User)
3. New Article/Content Creation
4. View and Retrieve list of Users and the Articles
5. References - covering various public website links
6. External References - covering mathematical functions for quick references


C. Application Implementation:

This application includes REST APIs implementation and cloud based functionalities covering below:
1. Application includes  GET, POST, PUT, DELETE methods implemented with relevant response codes 200(SUCCESS), 302(FOUND), 400(BAD REQUEST), 500(INTERNAL SERVER ERROR) adhering to the REST standards
2. Application includes External APIs named "Newton" to utilise and retrieve the outcomes of various mathematical functions, operations supporting this application's functionality needs
3. Application is served and secured over https using SSL Certificates
4. Application uses a cloud-based postgreSQL database for accessing persisted information about the users and the articles created by the users  
5. Hash-based User's Password Authentication
6. PostgreSQL Database with role-based policies and privileges added


D. Repository Source Code Package Contents

a. Refer "README.md" (this file) for detailed information about the application and it's functionalities, technology stack, python packages, application implementation, application repository source code package and other instructions to execute, run the application.


b. Refer "Pipfile" for required python packages to be installed in the virtual environment to run this project as listed below:
1. flask 			-----> (for creating Python based Web Framework or Application)
2. psycopg2-binary 	-----> (for heroku deployment and implementation)
3. flask-sqlalchemy 	-----> (for postgreSQL database access and managing persisted data)
4. gunicorn 		-----> (for heroku deployment and implementation)
5. flask-migrate 		-----> (for creating database models and tables in postgreSQL database)
6. flask_bcrypt 		-----> (for hash-based user's password authentication)
7. OpenSSL 		-----> (for securing the application over https using SSL Certificates)


c. Refer "cert.pem" file for the SSL Certificate and "key.pem" file for the key related information of the SSL Certificate for securing application over https.


d. Refer folder named "templates" which includes all .html templates rendering various front-end pages of the web application implemented for APIs.


e. Refer "app.py" file which is the main application python file to run the application. 
This includes all python import packages, environment (development, production), postgreSQL database configuration details, database models and various methods supporting REST APIs functionalities.


E. Application Run/Execution

Steps to be followed are:

Step-1:
Download the application repository in to the local machine.

Step-2:
Open a terminal and navigate to the folder of the application repository downloaded in above Step-1.

Step-3:
Install Python Virtual Environment using the command "pip3 install pipenv" in the terminal. Then move to Step-6 as Step-4 and Step-5 are not mandatory.

Step-4:
Create a directory in Python Virtual Environment using the command "mkdir python-virtual-environments && cd python-virtual-environments" in the terminal.

Step-5:
Create a new Virtual Environment using the command "python3 -m venv env" in the terminal.

Step-6:
Access and navigate to the Virtual Environment using the command "pipenv shell" in the terminal.

Step-7:
Download and install all given python packages in the Virtual Environment as below using given commands:
"pipenv install flask"
"pipenv install psycopg2"
"pipenv install psycopg2-binary"
"pipenv install flask-sqlalchemy"
"pipenv install gunicorn"

Step-8:
Run the application using the command "flask run --cert=cert.pem --key=key.pem" in the command prompt. 
NOTE: This command includes the details about the SSL Certificate and the key details for securing and accessing the application as https instead of http.

Application URL: https://127.0.0.1:5000














