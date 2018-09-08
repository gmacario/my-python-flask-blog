#!/usr/bin/env python

from blog import create_app
from flask_script import Manager

print("DEBUG: START manage.py")

app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()

print("DEBUG: END manage.py")

# EOF
