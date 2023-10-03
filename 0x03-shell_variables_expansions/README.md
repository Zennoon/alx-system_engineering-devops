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

11-binary_to_decimal: The script uses arithmetic expansion with the form base#number to convert the number to decimal

12-combinations: The script first uses brace expansion to produce the combinations, then the tr command inserts a new line after each combination, finally it uses grep -v to display everything except 'oo'

13-print_float: The script uses the printf command to round the number to 2 digits


100-decimal_to_hexadecimal: The script uses the printf command / function to print the converted number to the standard output

101-rot13: The script uses the tr command to translate the characters 13 times forward

102-odd: The script uses the cat -n command to first display the line numbers, then grep displays only the odd numbered lines, finally, cut is used to remove any whitespace and the line numbers

103-water_and_stir: The script uses the printf command and a whole lot of parameter expansion