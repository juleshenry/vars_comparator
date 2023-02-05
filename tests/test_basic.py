# import sys
# from io import StringIO
# def obtain_std_out(code:str)->str:
# 	old_stdout = sys.stdout
# 	redirected_output = sys.stdout = StringIO()
# 	exec(a_code)
# 	sys.stdout = old_stdout
# 	return redirected_output.getvalue()
import subprocess
def obtain_std_out(code_path:str)->str:
	codeproc = subprocess.run(['python3',f'{code_path}'], capture_output=True)
	return str(dir(codeproc))

STUB_VARS_GET = ';print("###",vars()'
print(obtain_std_out('./a.py'))
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