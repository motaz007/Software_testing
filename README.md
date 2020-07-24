# Software_testing
This is directory contains the solution of the here [assignment](SW_and_HW_functional_verification_Home_assignment_v16.pdf)



## Installation

To download the necessary libraries for the python scripts

```bash
pip install -r requirements.txt
```

## Contents

  There are two folders:
  1. Q1: which contains the solution of the first task and it is written in C.
      The following [ReadMe file](Q1/ReadMe.md) contains a description of that solution
  1. Q2: which contains the solution of the second task and it is written in python
  The following [ReadMe file](Q2/ReadMe.md) contains a description of that solution

## Usage:

* To run the test for the C code in Q1:

 use the makefile which will generate the executable Unit_Tests

* To run the python scripts in Q2:


  - To run the test for python code in Q2:
  use the following command line interface:

  ```bash
  python Q2/parser_test.py [--path path]
  ```

  If no path is selected the default path will be the current

  - To run the python implementation of the xml_parser:
  use the following CLI:

  ```bash
  python Q2/xml_parser.py [--path path]
  ```

  If no path is selected the default path will be the current
