import shutil
import time
import config

""" mode: 
0 : Naive Approach
1 : A*
2 : A* algorithm with own approach to avoid obstacle with whole linkage reflecting elbows
3 : A* with adjusting starting position
4 : A* inspired by Tang with PF for linkage
5 : PF
6 : PF Linkage
7 : PF Starting Position
8 : PF Starting Position and Linkage
"""
test_runner = "test_runner.py"
#test_runner = "test_runner_CloserDistance.py"

config.wrapper_mode = 5
exec(open("config.py").read())
exec(open(test_runner).read())
timestamp = time.strftime("%Y%m%d_%H%M%S")
shutil.copyfile("testresults.txt", f"./Test_Results/Wrapper_mode_{config.wrapper_mode}_{timestamp}.txt")

config.wrapper_mode = 6
exec(open("config.py").read())
exec(open(test_runner).read())
timestamp = time.strftime("%Y%m%d_%H%M%S")
shutil.copyfile("testresults.txt", f"./Test_Results/Wrapper_mode_{config.wrapper_mode}_{timestamp}.txt")

config.wrapper_mode = 7
exec(open("config.py").read())
exec(open(test_runner).read())
timestamp = time.strftime("%Y%m%d_%H%M%S")
shutil.copyfile("testresults.txt", f"./Test_Results/Wrapper_mode_{config.wrapper_mode}_{timestamp}.txt")

config.wrapper_mode = 8
exec(open("config.py").read())
exec(open(test_runner).read())
timestamp = time.strftime("%Y%m%d_%H%M%S")
shutil.copyfile("testresults.txt", f"./Test_Results/Wrapper_mode_{config.wrapper_mode}_{timestamp}.txt")

test_runner = "test_runner_CloserDistance.py"

config.wrapper_mode = 5
exec(open("config.py").read())
exec(open(test_runner).read())
timestamp = time.strftime("%Y%m%d_%H%M%S")
shutil.copyfile("testresults.txt", f"./Test_Results/Wrapper_mode_{config.wrapper_mode}_{timestamp}.txt")

config.wrapper_mode = 6
exec(open("config.py").read())
exec(open(test_runner).read())
timestamp = time.strftime("%Y%m%d_%H%M%S")
shutil.copyfile("testresults.txt", f"./Test_Results/Wrapper_mode_{config.wrapper_mode}_{timestamp}.txt")

config.wrapper_mode = 7
exec(open("config.py").read())
exec(open(test_runner).read())
timestamp = time.strftime("%Y%m%d_%H%M%S")
shutil.copyfile("testresults.txt", f"./Test_Results/Wrapper_mode_{config.wrapper_mode}_{timestamp}.txt")

config.wrapper_mode = 8
exec(open("config.py").read())
exec(open(test_runner).read())
timestamp = time.strftime("%Y%m%d_%H%M%S")
shutil.copyfile("testresults.txt", f"./Test_Results/Wrapper_mode_{config.wrapper_mode}_{timestamp}.txt")
