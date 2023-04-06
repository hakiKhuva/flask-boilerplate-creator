# flask boilerplate creator
create boilerplate for flask web application

run the boilerplate.py in command line

```cmd
> python boilerplate.py
```

After running above command it will ask for other modules to be installed, if not leave it blank
```cmd
Select modules to install
[0] flask-sqlalchemy
[1] flask-migrate
[2] flask-admin
[3] flask-wtf
[4] flask-session
Enter module index numbers separated by comma to add:
```

Enter pip command if default command is not working, in some os value for it may be `python3 -m pip install`
```cmd
Enter pip command (default is 'python -m pip install'):
```

All ok, it will install the module now
After installing all modules it will create files and folders on your system
This operation will remove any file content or delete folder if exists
```cmd
Installing modules: flask
using command python -m pip install
*Installing flask
Requirement already satisfied: flask in d:\practice\passbook-app\env\lib\site-packages (2.2.3)
Requirement already satisfied: click>=8.0 in d:\practice\passbook-app\env\lib\site-packages (from flask) (8.1.3)
Requirement already satisfied: Werkzeug>=2.2.2 in d:\practice\passbook-app\env\lib\site-packages (from flask) (2.2.3)
Requirement already satisfied: Jinja2>=3.0 in d:\practice\passbook-app\env\lib\site-packages (from flask) (3.1.2)
Requirement already satisfied: itsdangerous>=2.0 in d:\practice\passbook-app\env\lib\site-packages (from flask) (2.1.2)
Requirement already satisfied: colorama in d:\practice\passbook-app\env\lib\site-packages (from click>=8.0->flask) (0.4.6)
Requirement already satisfied: MarkupSafe>=2.0 in d:\practice\passbook-app\env\lib\site-packages (from Jinja2>=3.0->flask) (2.1.2)
WARNING: You are using pip version 21.2.4; however, version 23.0.1 is available.
You should consider upgrading via the 'D:\Practice\passbook-app\env\Scripts\python.exe -m pip install --upgrade pip' command.
*structure created successfully.
```

Done - structure is created.
