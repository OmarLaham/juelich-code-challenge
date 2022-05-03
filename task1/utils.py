# Python file that contains multiple helper functions

import sys

def exitWithCode(error_message, code=1) -> None:
	""" Prints error message to stdout and exits with error code. Default exit code is 1 """

	print(error_message)
	sys.exit(code)
