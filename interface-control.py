import subprocess
test = subprocess.Popen(["ifconfig","ppp0"], stdout=subprocess.PIPE)
#output = test.communicate()
#print type(output)
