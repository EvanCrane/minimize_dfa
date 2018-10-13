Minimization of DFAs for Theory of Computation | CSCI 3500
This program will take in a .dfa file with specific syntax.
It will then parse it, minimize it, and output another DFA in the same format as the input.

################
# INSTRUCTIONS #
################

Step 1)
    This project runs on python3 and specifically developed with python 3.7.0 64 bit in mind. 
    Make sure that your computer is up to date with these libraries using apt-get or homebrew or download it for windows.

Step 2)
    Pull the project. This project is working in master branch. Other branches with more output details can be seen such as release or develop. Running it in the master branch will do.

Step 3)
    All dfa files that the program reads will be read from the ecrane/test/ folder. There are already some test cases in there that I have worked with there in other branches. Place any files you wish to read in there with one dfa per file. Files will only read in as a .dfa extension. 

Step 4)
    This project is best run in the command line or terminal. In order to run it direct or 'cd' to the project directory. (This should be already done when pulling from gitlab). Specifically direct into the 'ecrane' directory so that the main.py can be seen when using 'ls' or 'dir'.
    Using the command "python3 main.py" in terminal will start the program.

Step 5) 
    The program will ask you to specify a file from the /test/ folder to use. Input will need to be a correct filename with extension. (Example input: "Test1.dfa")

Step 6)
    The program will then run until it has finished its scripts, print out its result, and once complete it will exit. To run it again use the up arrow for terminal or command line or use the "python3 main.py" command again.