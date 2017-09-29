fh = open("1_gcd.py", "r")
contents = fh.readline()
print(contents)
fh.seek(70)
contents = fh.readline()
print(contents)
fh.close()

fh = open("newfile.py", "w")
line = fh.write("hello world")
print("Number of chars written = ", line)
s = ["this is a new line with newline\n", "this line has newline\n", "ok enough\n"]
fh.writelines(s)
fh.close()

fh = open("newfile.py", "r")
contents = fh.readlines()
for line in contents:
	print(line)
for line in contents:
	print(line, 'x', 'y', 'z', sep = "|")
fh.close()


