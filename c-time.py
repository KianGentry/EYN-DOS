import time

lt = time.localtime()
ctime = time.strftime("%H:%M:%S", lt)

print(ctime)
