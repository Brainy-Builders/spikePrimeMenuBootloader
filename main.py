# This file is part of the Spike Prime Menu Bootloader which is released under BSL 1.0.
# See file LICENSE or go to https://www.boost.org/users/license.html for full license details.

import os
import random
import re
import glob
from tkinter import filedialog

# REGEX Matches
tab = "    "
newline = "\n"
python_variable_combinations = r"[^a-zA-Z0-9]"
python_import_statements = r"(from\s+\w+\s+)?import[A-z|\s|,]+"
runloop_statements = r"runloop\.run\((\w+)\((.*)\)\)"

directory = filedialog.askdirectory(
    title="Open The Python Folder")
output = os.path.join(".", 'output.py')

python_files = glob.glob(directory+'/*.py')

merged_file = ""
def get_imports(files: list[str]) -> list[tuple[str,list[str,str]]]:
    imports = []
    import_stripped_files = []
    for file in files:
        content = open(file).read()
        matches = [line for line in content.split("\n") if re.match(python_import_statements,line)]
        for match in matches:
            imports.append(match)
            content = content.replace(match, '')
        import_stripped_files.append([content,file])
    imports = list(set(imports))
    return imports, import_stripped_files
def format_file(file: str, filename: str) -> str:
    match = re.search(runloop_statements, file, re.MULTILINE)
    if match:
        # Extract the captured group if the pattern is found
        return_value = match.group(1) # get the run function name
        file = file.replace(match.group(0),"") # Remove the line from the file
        usesAsync=True
    else:
        return_value = ""
        usesAsync = False
    function = f"""def {re.sub(python_variable_combinations,"_",filename)}():
{newline.join([tab+i for i in file.split(newline)])}
{tab}return {return_value}
"""
    callname = re.sub(python_variable_combinations,"_",filename)
    return [function, callname, usesAsync]
def format_list_as_string(list,pretty=False):
     str_light = [str(x) for x in list]
     if pretty:
        return '[\n{}\n]'.format(",\n".join(str_light))
     return '[{}]'.format(",".join(str_light))

imports, new_files = get_imports(python_files)
merged_file = "\n".join(imports)
merged_file += "\n"

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
    )
merged_file += "\n"
merged_file += open(os.path.join(".","spike.py")).read()
open(output, 'w+').write(merged_file)


