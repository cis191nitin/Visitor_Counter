Visitor_Counter
===============
Description of Scripts:

index.php

The main script that executes the other scripts on the page
This page displays the number of visits that have occurred, they are simply visits, not unique visits. Then it also informs the user what type of Operating system they are on. Finally it displays the counts of how many visitors have had each of the big three OS's, Mac, Windows, and Linux. The way this script works is twofold. The visitor count is handled by the display_count.py and update_count.py scripts which are explained later. The Operating system information is gathered by getting the HTTP_USER_AGENT info in php, and then pattern matching it using regex to identify which OS is present. Then through a series of if statements, the appropriate actions are taken to update the counts for the OS, which is handled by the os_war.py script. Finally all the counts are displayed by calling the os_pull.py script (actually called at the beginning of the index.php file, but displayed at the end), and displaying the counts. Every time a user refreshses the page, the count goes up. The visitor and os counting mechanisms don't keep track of the same user revisiting the page.

update_count.py

This script updates the total count of visits on the site. The way it does this is rather rudimentary. It accesses a txt file that starts out with only one line, which is 0. For every subsequent site visit, it pulls this last line of the txt file, adds one to it, and then appends the number to the txt file, therefore storing the count for the next time it needs to be updated. A regex could be used here to make it so that the previous count is replaced, as opposed to appending a new line, but since this isn't a web app about to be used by millions, this method will suffice. The script basically opens the file, pulls the last line, converts it to an int, adds one, then converts it back to a string, and re updates the txt file. The txt file here is somewhat like memory, it remembers the state of the visitor count.

display_count.py

This script is very simple, all it does is open the previously mentioned txt file that has the counts, pulls the last line of the file which represents the current count, and then displays it to the user, the display part is done in the index.php file.

os_war.py

This script essentially is just a bigger version of the update_count.py file. When the index.php file recognizes which OS is being used through a regex pattern match, it passes off a string of either "mac", "windows", or "linux" to this script. This is done using the sys.argv array in the python script. Now this string that is passed to the python script is put through a conditianal block where it is decided which os count needs to be updated. The method of updating here is the exact same as for the visitor counter. A txt file is maintained for each os count, and when it gets updated, the last line is pulled, converted to an int, then converted back to a string and appended to the txt file. A good way to factor this code down would be to generalize the update_count.py script to take an argument that would then do this for the given txt file, here the code is slightly redundant in that the workings of update_count.py are just repeated three times. In any case, this script updates the counts for each os by taking in an argument from the index.php script.

os_pull.py

This script works basically the same as display_count.py, it opens each of the three os count txt files and pulls the last line which represents the current count of os's that have visited the sight. Here however, it joins the three counts into one string separated by white space. This is then returned to the index.php script. What index.php script does with this is to split the string by white space into an array, and then it has access to each of the counts separately and can display them however it chooses. So again, this script is pretty similar to the display_count.py script, and has some room for code refactorization.

In general the use of the python scripts mainly handles the grunt work of updating counts, while the index.php file does all of the display, as well as handle's the logic of which counts get updated.
