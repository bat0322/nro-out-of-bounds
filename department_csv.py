import sys
import os

# FOUND METHOD: https://www.novixys.com/blog/python-check-file-can-read-write/https://www.novixys.com/blog/python-check-file-can-read-write/#3_Checking_if_file_can_be_written
def check_file_writable(fnm):
    if os.path.exists(fnm):
        # path exists
        if os.path.isfile(fnm): # is it a file or a dir?
            # also works when file is a link and the target is writable
            return os.access(fnm, os.W_OK)
        else:
            return False # path is a dir, so cannot write as a file
    # target does not exist, check perms on parent dir
    pdir = os.path.dirname(fnm)
    if not pdir: pdir = '.'
    # target is creatable if parent dir is writable
    return os.access(pdir, os.W_OK)

if len(sys.argv) < 3:
	sys.exit('Insufficient arguments: python3 department_csv.py raw_textfile_path output_csv_path')

if not os.access(sys.argv[1], os.R_OK):
	sys.exit('Could not access file: ', sys.argv[1])

if not check_file_writable(sys.argv[2]):
	sys.exit('Could not write to file: ', sys.argv[2])

in_file = open(sys.argv[1], 'r')
out_file = open(sys.argv[2], 'w')
line = in_file.readline()
while line:
	line = line.strip(') \n')
	tokens = line.split('(')
	line = in_file.readline()
	out_file.write(tokens[0] + ',' + tokens[1] + '\n')
