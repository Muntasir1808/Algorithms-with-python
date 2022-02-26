from pathlib import Path
# now we need to create a path object reference to a file or directory to a path object
# two ways we can do it
# Absolute path it starts from the root of out hard disk
# Relative path which is a path starting from the current directory if we want to reference "ecommerce"
# directory in out project we can use the relative path..so we start from the current directory and go to somewhere else
path = Path("ecommerce")
print(path.exists())
# we can also create new directory
path2 = Path("emails")
# path2.mkdir()

# we can also remove the directory
# path2.rmdir()

# we can also find all the files and directory in a given path open them and process them
# using the globe method we can search for files and directory in the current path within globe parameter we can search
# "*" means all files and all directories
# to get only the files not the directory we have to pass "*.*"
# we can also search for all the py files or xls like "*.py"
path = Path()
# print(path.glob('*.py'))
# for file in path.glob('*.py'):
# print(file)

# to get all the files and directories in the current path
for file in path.glob('*'):
    print(file)



