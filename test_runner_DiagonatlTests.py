import config
import numpy as np
import PrintStatistics as ps


PI = np.pi
#config.wrapper_mode = 4
rho_0 = 7
k = 30

algorithm = ["WrapperNaive.py", "WrapperAStar.py", "WrapperAStarElbow.py", "WrapperAStarStartPosition.py", 
             "WrapperAStarTang.py", "WrapperPF.py", "WrapperPFLinkage.py", "WrapperPFStartingPosition.py",
             "WrapperPFLinkageStartingPosition.py"]

""" config.wrapper_mode: (in config)
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


print("1.,2.: PI/4, PI, PI")
config.theta_coxa = PI/4
config.theta_femur = PI
config.theta_tibia = PI
config.target_x, config.target_y = -12,12
config.center = (-6, 6)
config.radius = 2
exec(open(algorithm[config.wrapper_mode]).read())

config.theta_coxa = 5/4*PI
exec(open(algorithm[config.wrapper_mode]).read())

config.theta_coxa = 7/4*PI
exec(open(algorithm[config.wrapper_mode]).read())

print("3.4.: PI/4, PI, PI")
config.theta_coxa = PI/4
config.theta_femur = PI
config.theta_tibia = PI
config.target_x, config.target_y = 12,-12
config.center = (6, -6)
config.radius = 2
exec(open(algorithm[config.wrapper_mode]).read())

config.theta_coxa = 5/4*PI
exec(open(algorithm[config.wrapper_mode]).read())

config.theta_coxa = 3/4*PI
exec(open(algorithm[config.wrapper_mode]).read())

print("5.6..: PI/4, PI, PI")
config.theta_coxa = 3*PI/4
config.theta_femur = PI
config.theta_tibia = PI
config.target_x, config.target_y = 12,12
config.center = (6, 6)
config.radius = 2
exec(open(algorithm[config.wrapper_mode]).read())

config.theta_coxa = 7/4*PI
exec(open(algorithm[config.wrapper_mode]).read())

config.theta_coxa = 5/4*PI
exec(open(algorithm[config.wrapper_mode]).read())

print("7.8.: PI/4, PI, PI")
config.theta_coxa = 3*PI/4
config.theta_femur = PI
config.theta_tibia = PI
config.target_x, config.target_y = -12,-12
config.center = (-6, -6)
config.radius = 2
exec(open(algorithm[config.wrapper_mode]).read())

config.theta_coxa = 7/4*PI
exec(open(algorithm[config.wrapper_mode]).read())

config.theta_coxa = 1/4*PI
exec(open(algorithm[config.wrapper_mode]).read())

ps.statistics_a_star()
ps.statistics_a_star_elbow()
ps.statistics_a_star_start_position()
ps.statistics_astar_tang
ps.statistics_naive()
ps.statistics_pf()
ps.statistics_pf_linkage()
ps.statistics_pf_sp()
ps.statistics_pf_linkage_sp()
