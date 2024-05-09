# This file is part of the Spike Prime Menu Bootloader which is released under BSL 1.0.
# See file LICENSE or go to https://www.boost.org/users/license.html for full license details.

import os
import random
import re
import glob
from tkinter import filedialog#universal file prompter

# REGEX Matches
tab = "    " # Change to \t if you get Indentation error.
newline = "\n"
python_variable_combinations = r"[^a-zA-Z0-9]"
python_import_statements = r"(from\s+\w+\s+)?import[A-z|\s|,]+"# Search for the regex of import statements
runloop_statements = r"runloop\.run\((\w+)\((.*)\)\)" #runloop function

directory = filedialog.askdirectory(
    title="Open The Python Folder # Prompt for the directory
    ")
output = os.path.join(".", 'output.py') #output in the repo directory

python_files = glob.glob(directory+'/*.py')#Find all files in the directory file

merged_file = "" # Store the file as a string
def get_imports(files: list[str]) -> list[tuple[str,list[str,str]]]:
    '''
    get_imports()
    Parameters: 
    - files: a list of file locations
    Returns:
    - a tuple containing a list of all inputs in the list of files, and the list of file content without the import statments
    '''
    imports = [] # List of import statements
    import_stripped_files = []
    for file in files:
        content = open(file).read()
        matches = [line for line in content.split("\n") if re.match(python_import_statements,line)]
        for match in matches:
            imports.append(match) # add the import to a list
            content = content.replace(match, '') # remove import from the file
        import_stripped_files.append([content,file])
    imports = list(set(imports)) # make the list unique
    return imports, import_stripped_files
def format_file(file: str, filename: str) -> str:
    '''
    format_file()
    Parameters:
    - file: the content of the file
    - filename: the file path that will be converted to the function name
    Returns:
    - function: the file converted to a function
    '''
    match = re.search(runloop_statements, file, re.MULTILINE) # Find where there is an import statement
    if match:
        # Intercept the runloop and return it from the function
        return_value = match.group(1) # get the run function name
        file = file.replace(match.group(0),"") # Remove the line from the file
        usesAsync=True
    else:
        return_value = ""
        usesAsync = False
    function = f"""def {re.sub(python_variable_combinations,"_",filename)}():
{newline.join([tab+i for i in file.split(newline)])}
{tab}return {return_value}
""" #add function definition, add tabs, and return the main function, if it is async
    callname = re.sub(python_variable_combinations,"_",filename)#Function name
    return [function, callname, usesAsync]
def format_list_as_string(list,pretty=False):
    '''format_list_as_string()
    Parameters:
    - list: a list of anything really
    - pretty: weather or not to pretty print the list
    Returns:
    - A string version of the python list
    '''
     str_list = [str(x) for x in list]
     if pretty:
        return '[\n{}\n]'.format(",\n".join(str_list)) # Pretty print the list
     return '[{}]'.format(",".join(str_list)) # Normal list

imports, new_files = get_imports(python_files)
merged_file = "\n".join(imports)
merged_file += "\n" # Seperator

files = []
for  file in new_files:
        function, name, usesAsync = format_file(file[0],file[1])
        merged_file += function
        files.append([name,usesAsync,
                      [random.randint(0,100)]*25 # You can make your own icons in a 25 index array with light intensities, replace this within output.py
                      ])


merged_file += "LOADED_FILES_LIST = {}".format(
    format_list_as_string(
        [format_list_as_string(i) for i in files], # Get each sublist formatted
        True) # Pretty print the big list
    ) # add a list of functions to the file
merged_file += "\n"
merged_file += open(os.path.join(".","spike.py")).read() # Add the spike prime menu to the file to auto run
open(output, 'w+').write(merged_file) # Write the output file


