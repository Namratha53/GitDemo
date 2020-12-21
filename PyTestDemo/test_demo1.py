#to run the testcases in cmd following are the different commands used
#copy the file path from pycharm and go to the path in cmd using CD command
#it considers 1 method as 1 test case
#py.test runs all the test cases present inside the package
#py.test -v gives logs as well'
#py.test -v -s gives logs and prints output as well
#py.test filename. runs specific file
#py.test -k card -v -s (runs specific methods which have card in their names
#mark it as smoke and run in cmd by py.test -m -v -s
#you can skip test with pytest.mark.skip
#@pytest.mark.xfail executes the method but doesnt provide us the results
#fixtures are used fr setup and tear down methods for test cases conftest file to genaralize foxtures
#and make it available to all test cases

import pytest

@pytest.mark.xfail
def test_firstprogram():
    print("Hello")

@pytest.mark.smoke
def test_cardprogram(setup):
    print('Hey!')


@pytest.mark.usefixtures
def test_crossBrowser(crossBrowser):
    print(crossBrowser)


