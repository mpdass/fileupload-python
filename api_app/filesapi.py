#!/usr/bin/python3

import sys
sys.path.append("..")
for path in sys.path:
    print (path)
from pathlib import Path
from files.files_api import FileAPI

if __name__ == '__main__':
   print("Argument passed: '%s'" % sys.argv[1])
   #fileName = Path("/mnt/c/PracticeProjects/api-tests/src/python-code")
   fileName = Path(sys.argv[1])
   print ("Upload file: '%s'" % fileName)
   fapp = FileAPI()
   fapp.uploadFile(fileName)
   #fapp.getFiles()
