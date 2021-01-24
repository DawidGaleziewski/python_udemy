# import function from file
# from <file_name> import <func_name>
from my_module import my_func

my_func()

# in order to make python understand the subfolder is a package folder we need to create __init__.py in subdirectory. They can be empty but need to be there

# import from package
# from <folder_name> import <file_name>
from my_package import main_script
main_script.report_main()

# import sub package
# from <folder_name>.<sub_folder_name> import <file_name>
from my_package.sub_package import sub_script
sub_script.sub_report()