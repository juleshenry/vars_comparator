import subprocess, datetime, os

STUB_VARS_GET = f'\nprint("{str(datetime.datetime.now())}",vars())'


def add_vars_stub(code_path: str) -> None:
    with open(code_path, "a") as cp:
        cp.write(STUB_VARS_GET)


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
    print(dir(codeproc))
    print(codeproc.stdout)
    # out = codeproc.communicate()[0]
    # print(out)
    return str(codeproc)


if __name__ == "__main__":
    rm_vars_stub("./a.py")
# print(obtain_std_out('./a.py'))
# with open('a.py') as a_file, open('b.py') as b:
# 	a_code = str(a_file.read())
# 	std_out = obtain_std_out(a_code+STUB_VARS_GET)
# 	print(a_code+STUB_VARS_GET)
# 	print(std_out)
# try:
# 	exec(str(a_file.read()))
# except:
# 	raise Exception("First file threw an error")
# try:
# 	exec(str(b_file.read())+';print("###",vars()')
# except:
# 	raise Exception("Second file threw an error")
