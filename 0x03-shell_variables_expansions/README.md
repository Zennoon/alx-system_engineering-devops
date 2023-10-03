This directory was created to hold my answers / submissions for the project '0x03. Shell, init files, variables, and expansion' of ALX SE foundations.

0-alias: The script uses the alias command to create an alias named ls executing the command 'rm *'

1-hello_you: The script uses the echo command with the USER reserved variable to print the name of the current user

2-path: The script uses the existing reserved variable PATH and appends :/action to it using double quoting which does not suppress parameter expansion

3-paths: The script uses the tr command to replace every ':' in PATH with a new line, then it uses the wc -l command to count how many lines there are

4-global_variables: The script uses the printenv command to print the global variables

5-local_variables: The script uses the set command, which with out options, prints local, and global variables along with functions

6-create_local_variable: The script uses the assignment operator '=' with out exporting to create a local variable

7-create_global_variable: The script uses the assignment operator '=' and the export command to create a global variable

8-true_knowledge: The script uses arithmetic expansion to calculate the sum. The TRUEKNOWLEDGE variable doesn't need the parameter expansion symbol ($) within an expression

9-divide_and_rule: The script uses arithmetic expansion to perform integer division. The POWER and DIVIDE variables don't need the parameter expansion symbol ($) within an expression.

10-love_exponent_breath: The script uses arithmetic expansion to calculate the result. The LOVE and BREATH variables don't need the parameter expansion symbol ($) within an expression.