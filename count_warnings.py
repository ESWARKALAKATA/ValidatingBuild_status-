
import sys

count_old = 0
count_new = 0
old_log_file = open(sys.argv[1])
fd = old_log_file.read()
count_old = fd.count("warning")
print("old warning count : %d"%count_old)
old_log_file.close
new_log_file = open(sys.argv[2])
fd = new_log_file.read()
count_new = fd.count("warning")
print("current warning count : %d"%count_new)
new_log_file.close
if (count_old > count_new):
    print("Build Promoted")
else:
     print("Build CAN'T be promoted")


