import sys, glob, os
# the import statement imports modules sys, glob, and os.
# sys module: provides access to functions and variables that interact
#   with the Python runtime environment.
# glob module: search for files that match a specific pattern or name.
#   finds all the path names matching a specified pattern according
#   to the rules used by the Unix shell,
# os module: provides a portable way of interacting with the operating system.


# Get the directory name
# conditional if statement which checks if the script is running on a Windows OS.
# sys.platform contains a string that identifies the operating system on which the
#   Python interpreter is running.
# sys.platform values:
# The value of sys.platform differs based on the operating system:
# 	◦	'win32': Indicates the script is running on Windows (regardless of whether it's 32-bit or 64-bit).
# 	◦	'linux': Indicates the script is running on a Linux-based OS.
# 	◦	'darwin': Indicates the script is running on macOS.
# 	◦	Other platforms like 'aix', 'freebsd', or 'cygwin' might appear depending on the environment.

if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
    # hdir = os.path.join(os.environ['HOMEDRIVE'], os.environ['HOMEPATH'])
else:
    hdir = os.environ['HOME']
# os.environ is the pathway of your home directory.
# retrieves the value of the environment variable 'HOME' and assigns it to the variable hdir.
# A mapping object where keys and values are strings that represent the process environment.

# Construct a portable wildcard pattern
# os.path.join(hdir, '*') creates a file path that combines a base directory (hdir) with a
# wildcard (*) to match all files and directories in the hdir directory.
pattern = os.path.join(hdir,'*')
print(pattern)
print(hdir)

# TODO: Use the glob.glob() function to obtain the list of filenames
# this for loop loops through all the files in the base directory and return the files
#   and directories that match the wildcard pattern we created previously.
# glob.glob(pattern) returns a list of file paths that match the specified pattern using wildcards.
for file in glob.glob(pattern):
    print(file)

# TODO: use os.path.getsize to find each file's size
# os.path.getsize(file) retrieves the size of specified files in bytes.
for file in glob.glob(pattern):
    size = os.path.getsize(file)
    print(file, size, 'bytes')

# TODO: Add a test to only display files that are not zero length

for file in glob.glob(pattern):
    size = os.path.getsize(file)
    if size != 0:
        print(file, size, 'bytes')

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
for file in glob.glob(pattern):
    filename = os.path.basename(file)
    print(filename)

# Question 2:
password = "1234"
# The correct PIN code is stored as a string in the variable password.

attempt=1
# Define a variable to store the number of attempts.

supplied_pin = input("Enter your PIN: ")
# The input function prompts the user to give a password and stores it as a string in the supplied_pin variable.

# Use a while loop to prompt the user for input while the number of attempts is less than 3.
while attempt <4:
    # Using an if statement, we can check if the supplied pin equals the correct password.
    # if it does, then we print a suitable message and break out of the while loop.
    if supplied_pin == password:
        print("You can enjoy freedom for another day!")
        # "You may now enter the amount you would like to withdraw."
        break
        # If the attempts is between 1 and 3, ask the user to try again.
    elif 1<=attempt<3:
        print("Wrong password. Please try again if you don't want to go to jail.")
        print("Attempt #"+str(attempt)+" out of #3")
        # We increment (increase the size) the number of attempts.
        attempt += 1
        supplied_pin = input("Enter your PIN: ")
    # If the number of attempts is more than 3, then print a suitable message and exit the while loop.
    else:
        print("Police are coming for you!")
        # additional comment: "Your account has been locked."
        break
