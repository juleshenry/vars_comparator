import subprocess, datetime, os,json,ast

VARS_DEFAULT_NAMESPACE = ['__name__',
'__doc__',
'__package__',
'__loader__',
'__spec__',
'__annotations__',
'__builtins__',
'__file__',
'__cached__',]
def yield_vars_stub():
	class VS:
		def __init__(s):
			s.unique_id = '$$$' #str(datetime.datetime.now())
			s.stub = f'\nprint("{s.unique_id}");vars())'
	return VS()


def add_vars_stub(code_path: str) -> None:
    with open(code_path, "a") as cp:
        cp.write(yield_vars_stub().stub)


def rm_vars_stub(code_path: str) -> None:
    with open(code_path, "rb+") as file:
        # Move the pointer (similar to a cursor in a text editor) to the end of the file
        file.seek(0, os.SEEK_END)
        # This code means the following code skips the very last character in the file -
        # i.e. in the case the last line is null we delete the last line
        # and the penultimate one
        pos = file.tell() - 1
        # Read characters one at a time going backwards, searching for a newline character
        while pos > 0 and file.read(1) != b"\n":
            pos -= 1
            file.seek(pos, os.SEEK_SET)
        # If not at start of the file, delete all the characters ahead
        if pos > 0:
            file.seek(pos, os.SEEK_SET)
            file.truncate()


def obtain_std_out(code_path: str) -> str:
    add_vars_stub(code_path)
    codeproc = subprocess.run(["python3", f"{code_path}"], capture_output=True)
    rm_vars_stub(code_path)
    return codeproc


if __name__ == "__main__":
	# x = obtain_std_out('./a.py')
	# SUPER BRITTLE
	# y = str(x.stdout).split('$$$')[1][1:-3]
	y = 5
	x = 'aasdf'
	"""
	>>> import a
	>>> type(a)
	<class 'module'>
	"""
	print([(o[0],type(o[1]),) for o in vars().items() if (o[0] not in VARS_DEFAULT_NAMESPACE) and o[1] not in type()])
	# print(y)
	# y = ast.literal_eval(y)
	# print(y)
