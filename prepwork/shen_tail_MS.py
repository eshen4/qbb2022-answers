import sys
filename = sys.argv[1]
if len(sys.argv)>2:
    n_lines = int(sys.argv[2])
else:
    n_lines = 10
mylist = []
for i, line in enumerate(open(filename)):
    mylist.append(line.strip('\r\n'))
mylist.sort(reverse = True)
line_count = 0
for line in mylist:
    if line_count < n_lines:
        print(line.strip('\r\n'))
    line_count += 1

# This script is really well written. Just a couple of comments for making
# it even better. COMMENTS!!! Comments are really useful when you write 
# anything more than a basic script, both for other readers and for you if
# you take a break and come back to work on it later. Also, putting blank
# lines in your script to break up the code can help make it more readable.
# The one way that your script differs from the "tail" command is that your
# script reverses the order of the lines when it prints them out. It's
# clear why you do this. However, think about how you would print the same
# lines out but in the original order. Overall, great job! - Mike

#From discussion in class:
    #You can reverse twice to get rid of the issue with the script printing out from the last line (-Yijun)'
    #Using a negative variable will also run from the end/reverse it n_lines = -10 (?) (-Paul)
        #Expected solution, doesn't have the issue of reversing order
