import xml.etree.ElementTree as ET
import sys, os
from collections import namedtuple
from AbstractLog import AbstractLogsParser

import pandas as pd
from fpdf import FPDF

import argparse


"""
CLI implementation
"""
par = argparse.ArgumentParser(description='Read the input path.')
par.add_argument("path",help="Enter the address of the root folder")
args = par.parse_args()
path = args.path

class MyXmlParser(AbstractLogsParser):

    Entry = namedtuple("Entry", ("test","path", "result", "result_type"))
    list =[]

    def __init__(self, logs_extension):
        """
        Base class constructor.
        @param
        logs_extension Extension of log files to parse.
        """
        AbstractLogsParser.__init__(self,logs_extension)
        #self._logs_ext = '.'+logs_extension


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
        for i in self.list:
            if i[3] == result_type:
                count+=1
        return count


    def generate_detailed_report(self):
        """
        Generates detailed report on each test suite.
        """
        T_pass = self.get_result_by_type(self.TEST_RES_PASS)
        T_skip = self.get_result_by_type(self.TEST_RES_SKIP)
        T_fail = self.get_result_by_type(self.TEST_RES_FAIL)
        T_total = T_pass + T_fail + T_skip

        df = pd.DataFrame()
        ID = []
        res =[]
        add =[]

        for i in self.list:
            ID.append(i[0])
            res.append(i[2])
            add.append(i[1])
        df['Test ID'] = ID
        df['Test path'] = add
        df['Test result'] = res
        pdf = FPDF()
        pdf.add_page()
        pdf.set_xy(0, 0)
        pdf.set_font('arial', 'B', 16)
        pdf.cell(60)
        pdf.cell(75, 10, "Results of the tested software", 0, 2, 'C')
        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.cell(-30)
        pdf.cell(50, 10, 'Test ID', 1, 0, 'C')
        pdf.cell(70, 10, 'Test path', 1, 0, 'C')
        pdf.cell(40, 10, 'Test results', 1, 2, 'C')
        pdf.cell(-120)
        pdf.set_font('arial', '', 12)

        for i in range(0, len(df)):
            pdf.cell(50, 10, '%s' % (df['Test ID'].iloc[i]), 1, 0, 'C')
            pdf.cell(70, 10, '%s' % (str(df['Test path'].iloc[i])), 1, 0, 'C')
            pdf.cell(40, 10, '%s' % (str(df['Test result'].iloc[i])), 1, 2, 'C')
            pdf.cell(-120)

        pdf.cell(90, 10, " ", 0, 2, 'C')
        pdf.cell(2)
        pdf.cell(50, 10, 'Result type', 1, 0, 'C')
        pdf.cell(40, 10, 'Number', 1, 0, 'C')
        pdf.cell(40, 10, 'Percentage %', 1, 2, 'C')
        pdf.cell(-90)
        pdf.set_font('arial', '', 12)
        pdf.cell(50, 10, 'Passed', 1, 0, 'C')
        pdf.cell(40, 10, '%s' % (str(T_pass)), 1, 0, 'C')
        pdf.cell(40, 10, '%s' % (str(round(T_pass*100.0/T_total,2))), 1, 2, 'C')
        pdf.cell(-90)
        pdf.cell(50, 10, 'Skipped', 1, 0, 'C')
        pdf.cell(40, 10, '%s' % (str(T_skip)), 1, 0, 'C')
        pdf.cell(40, 10, '%s' % (str(round(T_skip*100.0/T_total,2))), 1, 2, 'C')
        pdf.cell(-90)
        pdf.cell(50, 10, 'Failed', 1, 0, 'C')
        pdf.cell(40, 10, '%s' % (str(T_fail)), 1, 0, 'C')
        pdf.cell(40, 10, '%s' % (str(round(T_fail*100.0/T_total,2))), 1, 2, 'C')

        pdf.output('test.pdf', 'F')

        print(df)
        # raise Exception("generate_detailed_report is not implemented")


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
                            # df['Test ID'].append(name)
                            # df['Test result'].append(result)
                            data = self.Entry(test=name,path = path,result=result, result_type = type)
                            self.list.append(data)
        for i in self.list:
            print(i)
        return list;


def main():
    my_parser = MyXmlParser("xml")
    my_parser.process_logs(path)
    a = my_parser.get_result_by_type(my_parser.TEST_RES_PASS)
    b = my_parser.get_result_by_type(my_parser.TEST_RES_SKIP)
    c = my_parser.get_result_by_type(my_parser.TEST_RES_FAIL)
    print "number of passed test is: " ,a,  "\n"
    print "number of skipped test is: " ,b,  "\n"
    print "number of failed test is: " ,c,  "\n"
    my_parser.generate_detailed_report()
if __name__ == '__main__':
    main()
