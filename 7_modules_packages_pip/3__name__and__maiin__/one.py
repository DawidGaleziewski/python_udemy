# in python wgen we run a script all code that is at indentation 0 is runned
print('Hello')

# __name__ is build in variable
# dependeing on the way the script is run it is assigned a value
# when we run script by python one.py, name will be assigned __name__ = "__main__"

# thererefore we can check


print('TOP level in ONE.py')

if __name__ == "__main__":
    print('do something if this is main script')
else:
    print('ONE.py has been imported')