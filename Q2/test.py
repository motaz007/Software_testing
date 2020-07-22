import xml.etree.ElementTree as ET
import sys, os
from collections import namedtuple
import click



Entry = namedtuple("Entry", ("test", "result", "result_type"))
list =[]

class MyXmlParser(object):
    TEST_RES_PASS = 0
    TEST_RES_FAIL = 1
    TEST_RES_SKIP = 2

    # @click.command()
    # @click.option('--ext', default="xml", help='Log files extension')
    # @click.option('--name', prompt='Your name',
                  # help='The person to greet.')
    @click.command()
    @pass_repo
    def __init__(self, logs_extension):
        # self.doc  = ET.parse(xml_file_name)
        # self.root = doc.getroot()
        self._logs_ext = '.'+logs_extension


    def switch(self, x):
        return {
         "PASS": self.TEST_RES_PASS,
         "SKIP": self.TEST_RES_SKIP,
         "FAIL": self.TEST_RES_FAIL,
        }[x]

    def do_something(self, folder):

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
            print(i[2])
        return list;
        """
        root_new  = ET.Element("users")
        for child in self.root:
            username             = child.attrib['username']
            password             = child.attrib['password']
            # create "user" here
            user    = ET.SubElement(root_new, "user")
            user.set("username",username)
            user.set("password",password)
            # checking attribute - skip KeyError
            try:
                remote_access   = child.attrib['remote_access']
                user.set("remote_access", remote_access)
            except KeyError:
                pass

            for g in child.findall("group"):
                # create "group" here
                group     = ET.SubElement(user,"group")
                if g.text != "lion":
                    group.text = g.text
        tree = ET.ElementTree(root_new)
        tree.write(output)
        """

    def count(self, result_type):
        count = 0
        for i in list:
            if i[2] == result_type:
                count+=1
        return count


def main():
    my_parser = MyXmlParser("xml")
    my_parser.do_something('.')
    c = my_parser.count(my_parser.TEST_RES_PASS)
    print(c)

if __name__ == '__main__':
    main()