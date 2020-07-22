import xml.etree.ElementTree as ET
import sys, os
from collections import namedtuple

Entry = namedtuple("Entry", ("test", "result"))
list =[]

class MyXmlParser(object):
# Different test statuses
    TEST_RES_PASS = 0
    TEST_RES_FAIL = 1
    TEST_RES_SKIP = 2
    def __init__(self, logs_extension):
        """
        Base class constructor.
        @param
        logs_extension Extension of log files to parse.
        """

        self._logs_ext = '.'+logs_extension


    def switch(self, x):
        """
        implementation of switch-expression
        Returns result types of a test TEST_RES_SKIP, TEST_RES_FAIL or TEST_RES_PASS
        @param
        x
        the test result from the log file
        """
        return {
         "PASS": self.TEST_RES_PASS,
         "SKIP": self.TEST_RES_SKIP,
         "FAIL": self.TEST_RES_FAIL,
        }[x]

    def get_result_by_type(self, result_type):
        """
        Returns number of passed, failed or skipped tests.
        @param
        result_type
        Type of results to return.
        """
        count = 0
        for i in list:
            if i[2] == result_type:
                count+=1
        return count
        # return -1


    def generate_detailed_report(self):
        """
        Generates detailed report on each test suite.
        """
        raise Exception("generate_detailed_report is not implemented")




    def process_logs(self, folder):
        """
        Parses all log files with target extension in the specified folder.
        @param
        folder
        Folder to look up for log files.
        """

        """
        This loop to go over all the files in the folders and sub-folders
        and find the files that ends with the logs_extension
        """
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(self._logs_ext):
                    print(os.path.join(root, file))
                    path = os.path.join(root, file)
                    doc = ET.parse(path)
                    root = doc.getroot()
                    for child in root:
                        if child.get('id'):
                            name = child.get('id')
                            result = child.get('result')
                            type = self.switch(result)
                            print(name, result, type)
                            data = Entry(test=name,result=result, result_type = type)
                            list.append(data)
        for i in list:
            print(i)

        raise Exception("process_logs is not implemented")

def main():
    my_parser = MyXmlParser("xml")
    my_parser.process_logs('.')

if __name__ == '__main__':
    main()
