import os
from nose.tools import *

_globals = {"filePath": None}
def my_setup():
	_globals["filePath"] = "/home/adam-d/"

def my_teardown():
	_globals["filePath"] = None

@with_setup(my_setup, my_teardown)
def test_filePath():
	print _globals["filePath"]
	if not os.path.exists(_globals["filePath"]):
		assert False