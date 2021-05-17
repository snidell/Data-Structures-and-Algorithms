# Design a logger system that receives a stream of messages along with their
# timestamps. Each unique message should only be printed at most every
# 10 seconds (i.e. a message printed at timestamp t will prevent other identical
#             messages from being printed until timestamp t + 10).
#
# All messages will come in chronological order. Several messages may arrive at
# the same timestamp.
#
# Implement the Logger class:
#
# Logger() Initializes the logger object.
# bool shouldPrintMessage(int timestamp, string message) Returns true if the
# message should be printed in the given timestamp, otherwise returns false.

class Logger():
    def __init__(self):
        self.log_stamp = {}

    def shouldPrintMessage(self,timestamp,message):
        if message in self.log_stamp:
            if self.log_stamp[message] <= timestamp:
                self.log_stamp = timestamp + 10
                return True
        else:
            self.log_stamp[message] = timestamp + 10
            return True
        return False


if __name__ =="__main__":
    mySolution = Logger()

    print(mySolution.shouldPrintMessage(1,"foo"))
    print(mySolution.shouldPrintMessage(2,"bar"))
    print(mySolution.shouldPrintMessage(3,"foo"))
    print(mySolution.shouldPrintMessage(8,"bar"))
    print(mySolution.shouldPrintMessage(10,"foo"))
    print(mySolution.shouldPrintMessage(11,"foo"))
