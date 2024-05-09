# spikePrimeMenuBootloader
Compile various Spike Prime program files into a menu
# Installation
1. Install [Python](https://www.python.org/downloads/)
<br>1.5. Make sure ```tkinter``` is installed with python
2. Clone this repository
3. Copy all your python Spike program files into one directory

# Usage
1. Run this program
2. Select the directory where you store your Spike Prime files
3. Find the ```output.py``` in the directory of this repository
4. Edit the ```output.py``` so that each function in ```LOADED_FILES_LIST``` has a icon as the third index of the list otherwise it will all be one shade
### Drawing example
This:
```python
LOADED_FILES_LIST = [
    directory__file__function, True, 
    [
        100,000,000,000,100,
        000,100,100,100,000,
        000,100,100,100,000,
        000,100,100,100,000,
        100,000,000,000,100,
    ] # this is the light list, also note you do not have to pad the zeros
]
```
Looks like this:
<div style="display: flex;width:25px;flex-wrap:wrap">
    <div style="width: 5px;height: 5px;background-color:yellow"></div>
    <div style="width: 5px;height: 5px;background-color:grey"></div>
    <div style="width: 5px;height: 5px;background-color:grey"></div>
    <div style="width: 5px;height: 5px;background-color:grey"></div>
    <div style="width: 5px;height: 5px;background-color:yellow"></div>
    <div style="width: 5px;height: 5px;background-color:grey"></div>
    <div style="width: 5px;height: 5px;background-color:yellow"></div>
    <div style="width: 5px;height: 5px;background-color:yellow"></div>
    <div style="width: 5px;height: 5px;background-color:yellow"></div>
    <div style="width: 5px;height: 5px;background-color:grey"></div>
    <div style="width: 5px;height: 5px;background-color:grey"></div>
    <div style="width: 5px;height: 5px;background-color:yellow"></div>
    <div style="width: 5px;height: 5px;background-color:yellow"></div>
    <div style="width: 5px;height: 5px;background-color:yellow"></div>
    <div style="width: 5px;height: 5px;background-color:grey"></div>
    <div style="width: 5px;height: 5px;background-color:grey"></div>
    <div style="width: 5px;height: 5px;background-color:yellow"></div>
    <div style="width: 5px;height: 5px;background-color:yellow"></div>
    <div style="width: 5px;height: 5px;background-color:yellow"></div>
    <div style="width: 5px;height: 5px;background-color:grey"></div>
    <div style="width: 5px;height: 5px;background-color:yellow"></div>
    <div style="width: 5px;height: 5px;background-color:grey"></div>
    <div style="width: 5px;height: 5px;background-color:grey"></div>
    <div style="width: 5px;height: 5px;background-color:grey"></div>
    <div style="width: 5px;height: 5px;background-color:yellow"></div>

</div>

# Running

Left+Right Press | Left Press | Right Press
---|---|---|
Run mission | decrement selection | increment selection


## Licensed under the Boost Software License Agreement Version 1.0 


**SPIKE	is a registered trademark of LEGO Juris A/S**