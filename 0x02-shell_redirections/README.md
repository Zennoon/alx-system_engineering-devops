This directory was created to hold my answers / submissions for the project 0x02 Shell I/O Redirections and Filters

0-hello_world: The script uses echo to print "Hello, world" followed by a new line (default behavior) to standard output

1-confused_smiley: The script uses echo to print a confused smiley face to standard output

2-hellofile: The script uses cat to display the content of the etc/passwd file

3-twofiles: The script uses cat and lists two files separated by white space to concatenate their content and display

4-lastlines: The script uses tail with out number of lines specified (default is 10) to display the last 10 lines of the given file

5-firstlines: The script uses head with out number of lines specified (default is 10) to display the first 10 lines of the given file

6-third_line: The script first uses head to display first 3 lines of the file, then it passes it to tail which displays the last line (3rd line) of those 3 lines

7-file: The script uses the echo command with the > redirection operator. And then, the file name, basically each character is escaped with the backward slash (\) except the single quote (''), which is escaped by a surrounding double quote ("").

8-cwd_state: The script uses the ls command with the > redirection operator to either create a new file, or overwrite an existing one

9-duplicate_last_line: The script uses tail to grab the last line of the file, then it uses the >> redirection operator to duplicate it on the same file

10-no_more_js: The script uses find to locate js files, and then utilizes the xargs to command to delete them

11-directories: The script first uses the find command to locate directories, and then counts them using the wc command

12-newest_files: The script uses ls with the -t option to list sorted by modification time (newest first) then uses head to list the 10 newest files

13-unique: The script uses uniq with the -u option to only display unique lines, and then uses sort to sort the lines

14-findthatword: The script uses grep to find the root pattern in the file

15-countthatword: The script uses grep to display the lines containing the bin pattern, then it uses wc with the -l option to count the number of lines

16-whatsnext: The script uses grep to find the lines containing the root pattern, the -A 3 option makes it display 3 lines found after each match

17-hidethisword: The script uses grep with the -v option to invert the search and display lines not containing the pattern bin

18-letteronly: The script uses the grep command with a regular expression to match all lines beginning with a letter

19-AZ: The script uses the tr command with the set to be replaced and the set to replace it with given

20-hiago: The script uses the tr command with the -d option to delete the given characters, in this case c and C from the input

21-reverse: The script uses the rev command to reverse the input string

22-users_and_homes: The script uses cat to read the file, then uses cut to remove the unneeded sections, and finally uses sort to sort the output
