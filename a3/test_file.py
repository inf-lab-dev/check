import importlib

spec = importlib.util.spec_from_file_location('root_test_file', '../a2/test_file.py')
mod = importlib.util.module_from_spec(spec)
root_test_file = spec.loader.exec_module(mod)

from root_test_file import *