from xml_parser import MyXmlParser, path
import unittest

class TestStringMethods(unittest.TestCase):
    parser = None

    def setUp(self):
        self.parser = MyXmlParser("xml")
        self.parser.T_ID = []
        self.parser.T_RES = []
        self.parser.T_PATH = []
        self.parser.T_RES_TYPE = []


    def test_init(self):
        """
        initlization function test
        it checks for the creation of MyXmlParser object
        @param
        self the testing framwork object
        """
        self.assertIsNotNone(self.parser)


    def test_switch(self):
        """
        switch function test
        it tests the correctness of the switch function behaviour
        with its differnt arguments (PASS, SKIP,FAIL)
        @param
        self the testing framwork object
        """

        switch_pass = self.parser.switch("PASS")
        switch_fail = self.parser.switch("FAIL")
        switch_skip = self.parser.switch("SKIP")

        self.assertEqual(switch_pass,self.parser.TEST_RES_PASS)
        self.assertEqual(switch_fail,self.parser.TEST_RES_FAIL)
        self.assertEqual(switch_skip,self.parser.TEST_RES_SKIP)


    def test_get_result_by_type(self):
        """
        get_result_by_type function test
        It tests that the function returns the correct number for
        different result_type (TEST_RES_FAIL,TEST_RES_PASS, TEST_RES_SKIP)
        @param
        self the testing framwork object
        """
        self.parser = self.parser.__del__()
        self.parser = MyXmlParser("xml")
        test_path = './Q2/gap/conn'
        self.parser.process_logs(test_path)

        result_pass = self.parser.get_result_by_type(self.parser.TEST_RES_PASS)
        result_fail = self.parser.get_result_by_type(self.parser.TEST_RES_FAIL)
        result_skip = self.parser.get_result_by_type(self.parser.TEST_RES_SKIP)

        self.assertEqual(result_pass,2)
        self.assertEqual(result_fail,1)
        self.assertEqual(result_skip,1)



    def test_None_object(self):
        """
        Destructor test
        It tests that when the behaviour of __del__ function of the object
        @param
        self the testing framwork object
        """
        self.parser = self.parser.__del__()
        self.assertIsNone(self.parser)

    def test_process_logs(self):
        """
        Test for process_logs function
        @param
        self the testing framwork object
        """
        Return = self.parser.process_logs(path)

        # The lists have the same number of elements
        self.assertEqual(len(self.parser.T_ID),len(self.parser.T_RES))
        self.assertEqual(len(self.parser.T_ID),len(self.parser.T_RES_TYPE))
        self.assertEqual(len(self.parser.T_ID),len(self.parser.T_PATH))

        #Within the length of the lists, tests that all the values are not None
        for i in range (len(self.parser.T_ID)):
            if i :
                self.assertIsNotNone(self.parser.T_ID[i])
                self.assertIsNotNone(self.parser.T_RES[i])
                self.assertIsNotNone(self.parser.T_RES_TYPE[i])
                self.assertIsNotNone(self.parser.T_PATH[i])

        #Test the return value of the function when there is/n't xml files
        if len(self.parser.T_ID):
            self.assertEqual(Return,0)
        else:
            self.assertEqual(Return,-1)



    def test_generate_detailed_report(self):
        """
        Test for generate_detailed_report function
        Tests the behaviourof generate_detailed_report by checking its returned
        value
        @param
        self the testing framwork object
        """
        self.parser.process_logs(path)

        #Test the return value of the function when there is/n't xml files
        if len(self.parser.T_ID):
            self.assertEqual(self.parser.generate_detailed_report(),0)
        else:
            self.assertEqual(self.parser.generate_detailed_report(),-1)



if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
