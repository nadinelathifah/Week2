import sys, glob, os
# The import statement imports modules sys, glob, and os.
# sys module: provides access to functions and variables that interact with the Python runtime environment.
# glob module: searches for files that match a specific pattern or name.
#              Finds all the path names matching a specified pattern according to the rules used by the Unix shell (command line interpreter),
# os module: provides a portable way of interacting with the operating system.


# 1) Get the directory name
# Conditional 'if' statement which checks if the script is running on a Windows OS.
# sys.platform contains a string that identifies the operating system on which the Python interpreter is running.
# sys.platform values:
# The value of sys.platform differs based on the operating system:
# 	◦	'win32': Indicates the script is running on Windows (regardless of whether it's 32-bit or 64-bit).
# 	◦	'linux': Indicates the script is running on a Linux-based OS.
# 	◦	'darwin': Indicates the script is running on macOS.
# 	◦	Other platforms like 'aix', 'freebsd', or 'cygwin' might appear depending on the environment.

if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
    # hdir = os.path.join(os.environ['HOMEDRIVE'], os.environ['HOMEPATH']) for Windows
else:
    hdir = os.environ['HOME']
# os.environ is the pathway of your home directory.
# hdir home/base directory i.e. C: or /User/
# Retrieves the value of the environment variable 'HOME' and assigns it to the variable hdir.
# A mapping object where keys and values are strings that represent the process environment.

# 2) Construct a portable wildcard pattern
# os.path.join(hdir, '*') creates a file path that combines a base directory (hdir) with a wildcard (*)
#   to match all files and directories in the hdir directory.
pattern = os.path.join(hdir,'*')
print(pattern)
print(hdir)

# TODO: Use the glob.glob() function to obtain the list of filenames
# This 'for' loop loops through all the files in the base directory and return the files
#   and directories that match the wildcard pattern we created previously.
# glob.glob(pattern) is a function that returns a list of file paths that match the specified pattern using wildcards.
for file in glob.glob(pattern):
    print(file)

# TODO: use os.path.getsize to find each file's size
# os.path.getsize(file) is a function that retrieves the size of specified files in bytes.
for file in glob.glob(pattern):
    size = os.path.getsize(file)
    print(file, size, 'bytes')

# TODO: Add a test to only display files that are not zero length

for file in glob.glob(pattern):
    size = os.path.getsize(file)
    if size != 0:
    # Conditional 'if' statement instructs the interpreter to output files that are not zero length.
        print(file, size, 'bytes')

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename(), the interpreter outputs names of files in my directory without the leading directory names.
for file in glob.glob(pattern):
    filename = os.path.basename(file)
    print(filename)

