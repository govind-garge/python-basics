######################## File input output ###############################

# syntax for the open file e. g. open("file name", "mode")

# Write in the file
# w will remove all previous data and add the new content (file create if not exist)
f = open("demo-file-io.txt", "w")
f.write("Content added by code\n")
f.close()

# a will append the data at the end of the file (file create if not exist)
f = open("demo-file-io.txt", "a")
f.write("Content appended by code\n")
f.close()

# a+ will append the data at the end and you can also read the file as + is added (file create if not exist)
f = open("demo-file-io.txt", "a+")
f.write("Content appended by code\n")
data = f.read()
print("File I/O a+ read all content:", data)
f.close()

#read all content
f = open("demo-file-io.txt", "r")
data = f.read()
print("File I/O content all content:", data)
f.close()

# You can also use following to open the file f.close() not needed for this
with open("demo-file-io.txt", "r") as f:
    data = f.read()
    print("File I/O with and alias all content:", data)

# read 5 charactor
f = open("demo-file-io.txt", "r")
data = f.read(5)
print("File I/O content read 5 charactor:", data)
f.close()

# read single line
f = open("demo-file-io.txt", "r")
line1 = f.readline()
print("File I/O content read single line:", line1)
# if you use readline again it will give second line, as the pointer move once you read the data
line2 = f.readline()
print("File I/O content read single line:", line2)
f.close()

# file IO functions

# open(filename, mode) : The primary function used to open a file. It returns a file object.
# file.close() : Closes the file object and saves any changes. It's crucial for releasing resources.

# file.read(size) : Reads at most 'size' bytes/characters from the file and returns them as a string. If 'size' is omitted, it reads the entire file.
# file.readline() : Reads a single line from the file and returns it as a string.
# file.readlines() : Reads all lines from the file and returns them as a list of strings.

# file.write(string) : Writes the given 'string' to the file. Returns the number of characters written.
# file.writelines(list_of_strings) : Writes a list of strings to the file without adding line terminators.

# file.seek(offset, whence) : Changes the file position (cursor) to a new byte 'offset'. 'whence' (0=start, 1=current, 2=end) is optional.
# file.tell() : Returns the current file position (cursor location) in bytes.

# File IO modes

# 'r' : Read mode (default). Error if the file does not exist.
# 'w' : Write mode. Creates file if it doesn't exist, TRUNCATES (erases) content if it does.
# 'a' : Append mode. Creates file if it doesn't exist. Writes added to the end.
# 'x' : Exclusive creation mode. Fails if the file already exists.

# 'r+' : Read and Write mode. File pointer at the beginning.
# 'w+' : Write and Read mode. TRUNCATES the file.
# 'a+' : Append and Read mode. Writes added to the end.

# 't' : Text mode (default). Used for strings.
# 'b' : Binary mode. Used for bytes (e.g., 'rb', 'wb').

"""
To delete any file we have to import os module on top of the file so use following code

import os

os.remove("file name")
"""

