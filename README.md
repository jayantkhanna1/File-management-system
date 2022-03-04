# File management system using watchdog 

First please run the following command to get the module
```
pip install -r requirements.txt

```
Then you can run the program by typing following command :
```
python FMS.py

```
# Explaination

This program accepts a path from user path should be a <b> 'path to a directory' </b> Then start monitoring the directory for any event changes in its insider files or any subdirectories. Program exits with key board interrupt that is pressing <b> 'ctrl + c' </b> in terminal. You can get the watchdog documentation <a href="https://python-watchdog.readthedocs.io/_/downloads/en/latest/pdf/"> here </a>
# Function details

<ul>
<li>On_created function tells us when a file is created inside a directory</li>
<li>On_modified function tells us when a file is modified inside a directory</li>
<li>On_deleted function tells us when a file is deleted inside a directory</li>
<li>On_any_event function tells us when any event occurs inside a directory</li>
<li>On_moved function tells us when a file is moved inside a directory</li>
<li>On_closed function tells us when a file is closed inside a directory</li>
</ul>