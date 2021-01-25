import os
import subprocess
import shutil
import time

total_time = 0
pypy_override = [15,19,23]
for day in range(1,25+1):
    #copy file
    src_path = f"../day{day}/day{day}.py"
    f_path = f"day{day}.py"
    shutil.copyfile(src_path,f_path)
    if(day in pypy_override):
        tstart = time.time()
        s = subprocess.check_output(f"pypy3 {f_path}",shell=True).decode("utf-8")
    else:
        tstart = time.time()
        s = subprocess.check_output(f"python3 {f_path}",shell=True).decode("utf-8")
    taken = time.time() - tstart
    silver = s.split("silver: ")[1].split("\n")[0]
    gold = s.split("\n")[1].split("gold: ")[1].strip()
    #print("%10s: %10f %35s %35s" % (f"Day {day}",taken,silver,gold))
    
    if(day in pypy_override):
        print("%10s: %10f (pypy3)" % (f"Day {day}",taken))
    else:
        print("%10s: %10f" % (f"Day {day}",taken))
    total_time += taken
print("Total time:",total_time)
