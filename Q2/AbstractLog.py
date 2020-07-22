class AbstractLogsParser(object):
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
    def get_result_by_type(self, result_type):
        """
        Returns number of passed, failed or skipped tests.
        @param
        result_type
        Type of results to return.
        """
        return -1
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
        raise Exception("process_logs is not implemented")
