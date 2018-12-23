#!/usr/bin/env python
import os
import sys

<<<<<<< HEAD
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basic.settings")
=======
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomms.settings')
>>>>>>> b7b1c4dbac4b6de4abf914242d9c4d5c0e71e3a7
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
