import os
import shutil                                            # daily file and directory management tasks

print(os.getcwd())                                       # return current workign dir
print(os.chdir('/home/zermatt/Documents/python'))        # Change current working directory
print(os.system('mkdir today'))                          # Run the command mkdir in the system shell
print(os.chdir('/standard_lib_i'))

print(dir(os))                                            # <returns a list of all module functions>
print(help(os))                                           # <returns an extensive manual page created from the module's docstrings>



shutil.copyfile('data.db', 'archive.db')          # daily file and directory management tasks
shutil.move('/build/executables', 'installdir')