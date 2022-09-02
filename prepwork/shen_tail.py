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