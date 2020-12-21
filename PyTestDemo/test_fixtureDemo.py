import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_runfixtureDemo(self):
        print("I will excecute as soon as the setup funtion is excecuted")

    def test_runfixtureDemo1(self):
        print("demo1: I will excecute as soon as the setup funtion is excecuted")

    def test_runfixtureDemo2(self):
        print("demo2: I will excecute as soon as the setup funtion is excecuted")

    def test_runfixtureDemo3(self):
        print("demo3: I will excecute as soon as the setup funtion is excecuted")