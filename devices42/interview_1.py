import base64
import json
import os
import requests

from typing import List


API_ENDPOINT = "https://demo1.device42.com/"
DEVICE_DISCOVERY = "'device_id':"
DEVICE_ID_START= "'device_id':"
ERROR_TEXT = "Error:"
LOG_FILE = ".log"
PASSWORD = "d42test"
USER = "dev_test2548_api"


class ErrorMessage:
    def __init__(self,device_name:str,device_id:str,error:str):
        self.device_name = device_name
        self.device_id = device_id
        self.error = error
        self.existed = False

    def print(self):
        print("Device " +self.device_name+ " partially failed to import due to error: "+self.error)
    def get_error(self):
        return "Device " +self.device_name+ " partially failed to import due to error: "+self.error

class LogFilter:
    # method that builds the log discovery takes a path for the log file directory
    def __init__(self, directory: str, api_url:str):
        self.files = []
        self.num_errors = 0
        self.misses = 0
        self.updates = 0
        # parse valid files
        for file in os.listdir():
            if file.endswith(".log"):
                self.files.append(file)

        self.api_url = api_url
        self.error_messages = []

    # loop through files and read them
    def read_files(self):
        # spawn off threads in this method to conduct work simulatenouesly
        for file in self.files:
            self.parse_file(file)

    # parse the files for device line and error line
    def parse_file(self,filepath:str):
        # open/read file
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                # parse that file for a valid error
                if ERROR_TEXT in line:
                    self.num_errors += 1
                    this_error = self.get_error(line)
                    device_line = fp.readline()

                    # iterate until we find the decive id
                    while device_line:
                        if DEVICE_DISCOVERY in device_line:
                            device_id = self.get_device_id(device_line)
                            # device_name = self.get_device_name(device_id)
                            device_name = ""
                            break
                        device_line = fp.readline()
                    self.error_messages.append(ErrorMessage(device_id,device_name,this_error))

                line = fp.readline()
                cnt += 1

    # parses device ID from the given string
    def get_device_id(self,inputString)-> str:
        # should be able to decode the json here
        first_index = inputString.rfind(DEVICE_ID_START)
        second_index = inputString[first_index:].find("}")

        device_id = inputString[first_index+13:first_index+second_index]

        return device_id
    # parses the error from the given string
    def get_error(self,inputString)->str:
        first_index = inputString.find("]")
        return inputString[first_index+2:]

    # makes a request to the API given the device id and returns the device name
    def get_device_name(self,device_id):
        url = self.api_url+device_id+"/"
        userpass = USER + ':' + PASSWORD

        response=requests.get(url,
                headers={"Authorization": "Basic %s" % base64.b64encode(userpass.encode()).decode(),'Content-Type': 'application/x-www-form-urlencoded'})
        print("---response from get_device_name")
        json_res = response.json()

        # need to try/catch here to first see if request completed and also if the name exists
        print("device name: ",json_res["name"])
        return json_res["name"]

    # attempts to update the device notes given the error object that contains the device id, name and message
    def update_device_notes(self,error:ErrorMessage):
        url = "https://demo.device42.com/api/1.0/device/"

        userpass = USER + ':' + PASSWORD
        print(url)
        notes = error.get_error()
        payload = {"notes":notes, "device_id":error.device_id}
        print("----PAYLOAD:",payload)
        response = requests.put(url,
                headers={"Authorization": "Basic %s" % base64.b64encode(userpass.encode()).decode(),'Content-Type': 'application/x-www-form-urlencoded'},data=payload)

        json_res = response.json()
        print("---response from update_device_notes")
        print(json_res)

    # prints all the errors encountered for the current run
    def print_errors(self):
        print("number of errors: ",self.num_errors)
        for error in self.error_messages:
            error.print()

    # prints the summary at the end of the code segment
    def print_summary(self):
        print("------------------------------ Summary ------------------------------")
        print("Total number of errors: ",self.num_errors)
        print("Average errors across files: ",self.num_errors/len(self.files))
        print("Total misses: ",self.misses)
        print("Total number of updated: ",self.updates)

if __name__ == "__main__":

    myLogger = LogFilter("","https://demo.device42.com/api/1.0/devices/id/")
    myLogger.read_files()
    myLogger.print_errors()
    myLogger.print_summary()

    myLogger.get_device_name("656")
    # print(myLogger.get_device_name("656"))
    # myLogger.get_error("Line 44: [2019-03-08 10:52:02,395: WARNING/Worker-26] ValidationError: {'__all__': [u'this device_id']}")

    myError = ErrorMessage("something","656","AppError: Another port with different mac exists.")
    myLogger.update_device_notes(myError)
    # myError.print()
