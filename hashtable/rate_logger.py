class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}



    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if not(message in self.data):
            self.data[message] = timestamp + 10
            return True
        else:
            if timestamp >= self.data[message]:
                self.data[message] = timestamp + 10
                return True
        return False

if __name__ =="__main__":
    logger = Logger()
    print(logger.shouldPrintMessage(1, "foo"))
    print(logger.shouldPrintMessage(2, "bar"))
    print(logger.shouldPrintMessage(3, "foo"))
    print(logger.shouldPrintMessage(8, "bar"))
    print(logger.shouldPrintMessage(10, "foo"))
    print(logger.shouldPrintMessage(11, "foo"))
