#!/usr/bin/python3
#
#  This module implements all the REST APIs related to file handling.
#
import os
import traceback
import requests
from files.data.test_data import testdata as td
import json

class FileAPI():
    bUrl = ""
    apiKey = ""

    def __init__(self):
        self.bUrl = "%sapi/v2/files/" % td['endpoint'].strip("'")
        self.apiKey = td['apikey'].strip("'")
        print ("Base URL for Files RestAPI is: %s" % self.bUrl)

    def getFiles(self):
        url = '%s' % self.bUrl
        headers = {'Authorization': 'Token: %s' % self.apiKey}
        response = requests.get(url, headers=headers)
        print("Retrieved files: Headers sent: %s" % (response.request.headers))
        print("Response body: '%s'" % response.text)

    def uploadFile(self, filename):
        fdir, fname = os.path.split(filename)
        print("Upload file: '%s' from directory: '%s'" % (fname, fdir))
        url = "%scontents/" % self.bUrl
        print ("File upload API: '%s'" % url)
        #header = {'Content-Type': 'application/json', 'Authorization': 'token %s' % self.apiKey}
        header = {'Authorization': 'Token %s' % self.apiKey}
        print ("Updated Headers: %s" % json.dumps(header))
        
        #  Initial Implementation
        try:
           with open(filename, 'rb') as file:
              files = {'file': file}
              response = requests.post(url, files=files, headers=header)
              print ("Successfully opened and attempted to be processed")
        except:
           traceback.StackSummary.format()

        #  2nd approach - using 'files' data
        #files = {'file': (fname, open(filename, 'rb'))}
        #response = requests.post(url, files=files, headers=header)

        #  Print the response data
        print("\n\n\n")
        print(response.request.headers)
        print("\n\n\n")
        print("%s" % response.request.body)

        #  using 'curl' command
        #curlCmd = '''curl -v -k -X POST -H 'Content-Type:multipart/form-data' -H 'Authorization: Token %s' -F 'file=@%s' %s''' % (self.apiKey, filename, url)        
        #print("Running curl command: \n%s" % curlCmd)
        #os.popen(curlCmd)
        #args = shlex.split(curlCmd)
        #process = Popen(args, stdout=PIPE, stderr=PIPE)
        #stdout, stderr = process.communicate()        
        #print("Output from curl command: %s" % stdout)
        #print("Output from curl command: %s" % stderr)
        if response.ok:
           print ("File: '%s' has been uploaded successfully" % filename)
        else:
           response.raise_for_status()
