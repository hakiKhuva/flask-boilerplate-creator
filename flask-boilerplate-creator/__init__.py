"""
Generate boilerplate structure for flask web app

author: Harkishan Khuva <harkishankhuva.pythonanywhere.com>
created date: 07/04/2023 IST
version: 0.0.1
"""

# :: IMPORTS
import os
import sys
import shutil
import typing
import importlib.metadata


FOLDER = 1
FILE = 2


def _folder(*name:str) -> dict[str, typing.Union[str, int]]:
    """returns folder dictionary"""
    return {
        "type": FOLDER,
        "name": os.path.join(*name)
    }

def _file(*name:str) -> dict[str, typing.Union[str, int]]:
    """returns file dictionary"""
    return {
        "type": FILE,
        "name": os.path.join(*name)
    }


def _is_file(obj:dict) -> bool:
    """check if dictionary contains file type using `type` key of `obj`"""
    return obj["type"] == FILE


def _is_folder(obj:dict):
    """check if dictionary contains folder type using `type` key of `obj`"""
    return obj["type"] == FOLDER


# MODULES DIRECTORY AND FILE STRUCTURES
MODULES_WITH_DIRECTORIES = {
    "flask": [
        _folder("app"),
        _file("app","__init__.py"),
        _file("app","helpers.py"),
        _folder("app","views"),
        _folder("app","static"),
        _folder("app","static","css"),
        _folder("app","static","media"),
        _folder("app","static","js"),
        _folder("app","templates"),
        _file("app","templates", "base.html"),
        _file("app","settings.py"),
        _file("main.py")
    ],
    "flask-sqlalchemy": [
        _folder("app","models"),
        _file("app","models", "db.py")
    ],
    "flask-wtf": [
        _folder("app","forms")
    ]
}

# DATA TO BE INSERTED INTO FILES
FILES_INPUT = {
    os.path.join("app","__init__.py"): (
        "from flask import Flask\n"
        "# from flask_migrate import Migrate # uncomment if need\n"
        "# from flask_session import Session # uncomment if need\n\n"
        "# from .models import db # uncomment if need\n"
        "from .settings import APP_SETTINGS\n\n"
        "# migrate = Migrate() # uncomment if need \n"
        "# session = Session() # uncomment if need \n\n"
        "def create_app():\n"
        "    app = Flask(__name__)\n"
        "    app.config.update(APP_SETTINGS)\n\n"
        "    # db.init_app(app) # uncomment is need \n"
        "    # migrate.init_app(app, db) # uncomment if need \n\n"
        "    # session.init_app(app) # uncomment is need \n"
        "    return app\n"
        ),

    os.path.join("app","settings.py"): (
        "import datetime\n"
        "\n"
        "APP_SETTINGS = {\n"
        "    \"SECRET_KEY\": \"YOUR_SECRET_KEY_HERE\",\n"
        "    # \"SQLALCHEMY_DATABASE_URI\": \"sqlite:///master.sqlite3\", # uncomment this line if need \n"
        "    \"PERMANENT_SESSION_LIFETIME\": datetime.timedelta(days=7),\n"
        "    # \"SESSION_PERMANENT\": False, # uncomment this line if need \n"
        "    # \"SESSION_TYPE\": \"filesystem\", # uncomment this line if need \n"
        "}\n"
        "\n"
        "TIMEZONE = datetime.timezone.utc\n"
        "DEBUG = True\n"
    ),

    os.path.join("main.py"): (
        "from app import create_app\n"
        "from app.settings import DEBUG\n\n"
        "current_app = create_app()\n\n"
        "if __name__ == \"__main__\":\n"
        "    current_app.run(\n"
        "        debug=DEBUG\n"
        "    )\n"
    ),

    os.path.join("app", "helpers.py"): (
        "import datetime\n"
        "from .settings import TIMEZONE\n\n"
        "def get_datetime():\n"
        "    return datetime.datetime.now().astimezone(TIMEZONE)\n"
    ),

    os.path.join("app", "models", "db.py"): (
        "from flask_sqlalchemy import SQLAlchemy\n"
        "from ..helpers import get_datetime\n"
        "\n"
        "db = SQLAlchemy()\n"
        "\n"
        "class Base:\n"
        "    __abstract__ = True\n"
        "    id = db.Column(db.Integer(), primary_key=True)\n"
        "    created_date = db.Column(db.DateTime(), default=get_datetime)\n"
    ),

    os.path.join("app", "templates", "base.html"): (
        "<!DOCTYPE html>\n"
        "<html lang=\"en\">\n"
        "<head>\n"
        "    <meta charset=\"UTF-8\">\n"
        "    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n"
        "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        "    <title>{{title}}</title>\n"
        "    {% block head %}{% endblock %}\n"
        "</head>\n"
        "<body>\n"
        "    {% block body %}{% endblock %}\n"
        "</body>\n"
        "</html>\n"
    )
}


def _get_modules_to_be_installed():
    """returns user selected modules that need to install"""
    modules = [
        "flask-sqlalchemy",
        "flask-migrate",
        "flask-admin",
        "flask-wtf",
        "flask-session",
    ]

    modules_to_be_installed = [
        "flask"
    ]

    print("Select modules to install")

    # printing the module name with index
    for i in range(len(modules)):
        print(f"[{i}] {modules[i]}")
    nums = input("Enter module index numbers separated by comma to add: ").strip()
    numbers = nums.split(",")
    
    # checking for the value contains integer value or not
    errors = False
    for number in numbers:
        # checking number
        if number:
            number = number.strip()
            if number.isnumeric() is True:
                number = int(number)
                # checking for value if less than 0 or it's greater than length of the modules list
                if number < 0 or number > len(modules):
                    errors = True
            else:
                errors = True

            # if error value is True
            # then print the message and exit
            if errors is True:
                print("Number must be an integer and it must be greater than or equal to 0(zero) and must be less than {}".format(len(modules)))
                sys.exit(1)

            # else append the module name
            modules_to_be_installed.append(modules[int(number)])
    # final return
    return modules_to_be_installed


def main():
    """main function of the script"""
    custom_directory_structure = []

    # getting modules that to be installed
    include_modules = _get_modules_to_be_installed()
    
    # getting directory structure for the modules
    # and adding in `custom_directory_structure`
    for module in include_modules:
        if module in MODULES_WITH_DIRECTORIES:
            custom_directory_structure.append(MODULES_WITH_DIRECTORIES[module])
    
    # asking for pip command
    pip_command = input("Enter pip command (default is 'python -m pip install'): ") or "python -m pip install"

    # printing messages
    print("\nInstalling modules:",", ".join(include_modules))
    print("using command {}".format(pip_command))

    # creating requirements.txt file data
    requirements_file_data = ""

    # installing one by one module
    for module_name in include_modules:
        print(f"*Installing {module_name}")
        # running system command
        command_return = os.system(f"{pip_command} {module_name}")

        # if command return code is not 0(zero)
        # then print error messages
        # and exit
        if command_return != 0:
            print(f"error: {module_name} could not be installed!")
            print("error: pip command returns {}".format(command_return))
            sys.exit(1)

        # adding data to requirements
        try:
            requirements_file_data += f"{module_name}=={importlib.metadata.version(module_name.replace('-', '_'))}\n"
        # if metadata of module not found or package not found or not installed
        except importlib.metadata.PackageNotFoundError:
            requirements_file_data += f"{module_name}\n"

    # creating structure on local system
    for objects in custom_directory_structure:
        for obj in objects:
            if _is_folder(obj) is True:
                if os.path.exists(obj["name"]) is True:
                    shutil.rmtree(obj["name"])
                os.mkdir(obj["name"])
            elif _is_file(obj) is True:
                with open(obj["name"], "w") as f:
                    if obj["name"] in FILES_INPUT:
                        f.write(FILES_INPUT[obj["name"]])
    
    # writing requirements
    with open("requirements.txt", "w") as f:
        f.write(requirements_file_data)

    # done message
    print("\n*Structure created successfully.")
    print(f"If you get error like module not found, run `{pip_command} -r requirements.txt` command.")
