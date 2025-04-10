import config

def statistics_a_star():
    """Prints all tracked statistics for the conventional A* algorithm to testresults.txt
    """
    number_tests = config.astar_number_success + config.astar_number_error_tibia + config.astar_number_error_femur + config.astar_number_error_coxa + config.astar_number_error_no_path + config.astar_number_error_ee + config.astar_timeout
    if(number_tests == 0):
        with open("testresults.txt", "a") as file:
            file.write(f"A* algorithm : \n Total number of tests: {number_tests}\n")
        return

    if(len(config.astar_list_covered_distance) > 0):
        mean_covered_distance = sum(config.astar_list_covered_distance) / len(config.astar_list_covered_distance)
    else:
        mean_covered_distance = -1
    if(len(config.astar_time_needed) > 0):
        mean_time_needed = sum(config.astar_time_needed) / len(config.astar_time_needed)
    else:
        mean_time_needed = -1
    with open("testresults.txt", "a") as file:
        file.write(f"A* algorithm : \n Total number of tests: {number_tests}, #SUCCESS: {config.astar_number_success}, in percent: {config.astar_number_success/(number_tests)}\n")
        file.write(f"config.runner_mode = {config.runner_mode}")
        file.write(f"#Error End Effector = {config.astar_number_error_ee}, #Error Timeout = {config.astar_timeout} \n")
        file.write(f"#Error tibia = {config.astar_number_error_tibia}, #Error femur = {config.astar_number_error_femur}, #Error coxa = {config.astar_number_error_coxa}\n")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}")
        mean_time_needed_calculation = sum(config.astar_time_needed_calculation)/len(config.astar_time_needed_calculation)
        file.write(f"Median time needed for calculation = {mean_time_needed_calculation}\n\n\n")

def statistics_pf():
    """Prints all tracked statistics for the conventional Potential Field method
    """
    number_tests = config.pf_number_success + config.pf_number_error_tibia + config.pf_number_error_femur + config.pf_number_error_coxa + config.pf_number_timeout + config.pf_number_error_ee
    if(number_tests == 0):
        with open("testresults.txt", "a") as file:
            file.write(f"PF : \n Total number of tests: {number_tests}\n")
        return
    if(len(config.pf_list_covered_distance) > 0):
        mean_covered_distance = sum(config.pf_list_covered_distance) / len(config.pf_list_covered_distance)
    else:
        mean_covered_distance = -1
    if(len(config.pf_time_needed) > 0):
        mean_time_needed = sum(config.pf_time_needed) / len(config.pf_time_needed)
    else:
        mean_time_needed = -1
    with open("testresults.txt", "a") as file:
        file.write(f"PF: \nTotal number of tests: {number_tests}, #SUCCESS: {config.pf_number_success}, in percent: {config.pf_number_success/(number_tests)}\n")
        file.write(f"config.runner_mode = {config.runner_mode}")
        file.write(f"#Error end effector = {config.pf_number_error_ee}\n")
        file.write(f"#Error tibia = {config.pf_number_error_tibia}, #Error femur = {config.pf_number_error_femur}, #Error coxa = {config.pf_number_error_coxa}, #TIMEOUT = {config.pf_number_timeout}\n")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}\n\n\n")
     
def statistics_a_star_elbow():
    """Prints all tracked statistics for the A* algorithm with changing elbow posture
    """
    number_tests = config.elbow_start_position_number_success + config.elbow_start_position_number_timeout + config.elbow_start_position_number_error_tibia + config.elbow_start_position_number_error_femur + config.elbow_start_position_number_error_coxa + config.elbow_start_position_number_error_ee
    if(number_tests == 0):
        with open("testresults.txt", "a") as file:
            file.write(f"A* Elbow : \n Total number of tests: {number_tests}\n")
        return
    if(len(config.elbow_start_position_list_covered_distance) > 0):
        mean_covered_distance = sum(config.elbow_start_position_list_covered_distance) / len(config.elbow_start_position_list_covered_distance)
    else:
        mean_covered_distance = -1
    if(len(config.elbow_start_position_time_needed) > 0):
        mean_time_needed = sum(config.elbow_start_position_time_needed) / len(config.elbow_start_position_time_needed)
    else:
        mean_time_needed = -1
    with open("testresults.txt", "a") as file:
        file.write(f"A* Elbow: \n Total number of tests: {number_tests}, #SUCCESS: {config.elbow_start_position_number_success}, in percent: {config.elbow_start_position_number_success/(number_tests)}\n")
        file.write(f"config.runner_mode = {config.runner_mode}")
        file.write(f"#Error end effector = {config.elbow_start_position_number_error_ee}\n")
        file.write(f"#Error tibia = {config.elbow_start_position_number_error_tibia}, #Error femur = {config.elbow_start_position_number_error_femur}, #Error coxa = {config.elbow_start_position_number_error_coxa}, #TIMEOUT = {config.elbow_start_position_number_timeout}\n")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}")
        mean_time_needed_calculation = sum(config.elbow_start_position_time_needed_calculation)/len(config.elbow_start_position_time_needed_calculation)
        file.write(f"Median time needed for calculation = {mean_time_needed_calculation}\n\n\n")

def statistics_naive():
    """Prints the tracked statistics of the naive approach to testresults.txt
    """
    number_tests = config.naive_number_success + config.naive_number_error_tibia + config.naive_number_error_femur + config.naive_number_error_coxa + config.naive_number_error_ee
    if(number_tests == 0):
        with open("testresults.txt", "a") as file:
            file.write(f"Naive : \n Total number of tests: {number_tests}\n")
        return
    if(len(config.naive_list_covered_distance) > 0):
        mean_covered_distance = sum(config.naive_list_covered_distance) / len(config.naive_list_covered_distance)
    else:
        mean_covered_distance = -1
    if(len(config.naive_list_time_needed) > 0):
        mean_time_needed = sum(config.naive_list_time_needed) / len(config.naive_list_time_needed)
    else:
        mean_time_needed = -1
    with open("testresults.txt", "a") as file:
        #number_tests = config.naive_number_success + config.naive_number_error_tibia + config.naive_number_error_femur + config.naive_number_error_coxa
        file.write(f"Naive: \nTotal number of tests: {number_tests}, #SUCCESS: {config.naive_number_success}\n")
        file.write(f"config.runner_mode = {config.runner_mode}")
        file.write(f"#Error end effector = {config.naive_number_error_ee}\n")
        file.write(f"#Error tibia = {config.naive_number_error_tibia}, #Error femur = {config.naive_number_error_femur}, #Error coxa = {config.naive_number_error_coxa}")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}\n\n\n")
     
# Statistics: mode 4 : PF applied to all links
def statistics_pf_linkage():
    """Prints the tracked statistics of pf applied to all links to testresults.txt
    """
    number_tests = config.pf_all_links_number_success + config.pf_all_links_number_timeout + config.pf_all_links_number_error_tibia + config.pf_all_links_number_error_femur + config.pf_all_links_number_error_coxa + config.pf_all_links_number_error_ee
    if(number_tests == 0):
        with open("testresults.txt", "a") as file:
            file.write(f"PF all links : \n Total number of tests: {number_tests}\n")
        return
    if(len(config.pf_all_links_list_covered_distance) > 0):
        mean_covered_distance = sum(config.pf_all_links_list_covered_distance) / len(config.pf_all_links_list_covered_distance)
    else:
        mean_covered_distance = -1
    if(len(config.pf_all_links_time_needed) > 0):
        mean_time_needed = sum(config.pf_all_links_time_needed) / len(config.pf_all_links_time_needed)
    else:
        mean_time_needed = -1
    with open("testresults.txt", "a") as file:
        file.write(f"PF all links: \nTotal number of tests: {number_tests}, #SUCCESS: {config.pf_all_links_number_success}, in percent: {config.pf_all_links_number_success/(number_tests)}\n")
        file.write(f"config.runner_mode = {config.runner_mode}")
        file.write(f"#Error end effector = {config.pf_all_links_number_error_ee}\n")
        file.write(f"#Error tibia = {config.pf_all_links_number_error_tibia}, #Error femur = {config.pf_all_links_number_error_femur}, #Error coxa = {config.pf_all_links_number_error_coxa}, #TIMEOUT = {config.pf_all_links_number_timeout}\n")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}\n\n\n")
     
# Statistics: mode 5/A* with specific start position
def statistics_a_star_start_position():
    """Prints the tracked statistics of A* with start position to testresults.txt
    """
    number_tests = config.astar_start_position_number_success + config.astar_start_position_number_timeout + config.astar_start_position_number_error_tibia + config.astar_start_position_number_error_femur + config.astar_start_position_number_error_coxa + config.astar_start_position_number_error_ee
    if(number_tests == 0):
        with open("testresults.txt", "a") as file:
            file.write(f"A* starting position: \n Total number of tests: {number_tests}\n")
        return
    if(len(config.astar_start_position_list_covered_distance) > 0):
        mean_covered_distance = sum(config.astar_start_position_list_covered_distance) / len(config.astar_start_position_list_covered_distance)
    else:
        mean_covered_distance = -1
    if(len(config.astar_start_position_time_needed) > 0):
        mean_time_needed = sum(config.astar_start_position_time_needed) / len(config.astar_start_position_time_needed)
    else:
        mean_time_needed = -1
    with open("testresults.txt", "a") as file:
        file.write(f"A* start position:\nTotal number of tests: {number_tests}, #SUCCESS: {config.astar_start_position_number_success}, in percent: {config.astar_start_position_number_success/(number_tests)}\n")
        file.write(f"config.runner_mode = {config.runner_mode}")
        file.write(f"#Error end effector = {config.astar_start_position_number_error_ee}\n")
        file.write(f"#Error tibia = {config.astar_start_position_number_error_tibia}, #Error femur = {config.astar_start_position_number_error_femur}, #Error coxa = {config.astar_start_position_number_error_coxa}, #TIMEOUT = {config.astar_start_position_number_timeout}\n")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}\n")
        mean_time_needed_calculation = sum(config.astar_start_position_time_needed_calculation)/len(config.astar_start_position_time_needed_calculation)
        file.write(f"Median time needed for calculation = {mean_time_needed_calculation}\n\n\n")

def statistics_pf_linkage_sp():
    """Prints all tracked statistics for the Potential Field method with linkage extension
    """
    number_tests = config.pf_sp_linkage_number_success + config.pf_sp_linkage_number_error_tibia + config.pf_sp_linkage_number_error_femur + config.pf_sp_linkage_number_error_coxa + config.pf_sp_linkage_number_timeout + config.pf_sp_linkage_number_error_ee
    if(number_tests == 0):
        with open("testresults.txt", "a") as file:
            file.write(f"PF : \n Total number of tests: {number_tests}\n")
        return
    if(len(config.pf_sp_linkage_list_covered_distance) > 0):
        mean_covered_distance = sum(config.pf_sp_linkage_list_covered_distance) / len(config.pf_sp_linkage_list_covered_distance)
    else:
        mean_covered_distance = -1
    if(len(config.pf_sp_linkage_time_needed) > 0):
        mean_time_needed = sum(config.pf_sp_linkage_time_needed) / len(config.pf_sp_linkage_time_needed)
    else:
        mean_time_needed = -1
    with open("testresults.txt", "a") as file:
        file.write(f"PF Starting Position Linkage: \nTotal number of tests: {number_tests}, #SUCCESS: {config.pf_sp_linkage_number_success}, in percent: {config.pf_sp_linkage_number_success/(number_tests)}\n")
        file.write(f"config.runner_mode = {config.runner_mode}")
        file.write(f"#Error end effector = {config.pf_sp_linkage_number_error_ee}\n")
        file.write(f"#Error tibia = {config.pf_sp_linkage_number_error_tibia}, #Error femur = {config.pf_sp_linkage_number_error_femur}, #Error coxa = {config.pf_sp_linkage_number_error_coxa}, #TIMEOUT = {config.pf_sp_linkage_number_timeout}\n")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}\n\n\n")

def statistics_pf_sp():
    """Prints all tracked statistics for the Potential Field method with starting position extension
    """
    number_tests = config.pf_sp_number_success + config.pf_sp_number_error_tibia + config.pf_sp_number_error_femur + config.pf_sp_number_error_coxa + config.pf_sp_number_timeout + config.pf_sp_number_error_ee
    if(number_tests == 0):
        with open("testresults.txt", "a") as file:
            file.write(f"PF : \n Total number of tests: {number_tests}\n")
        return
    if(len(config.pf_sp_list_covered_distance) > 0):
        mean_covered_distance = sum(config.pf_sp_list_covered_distance) / len(config.pf_sp_list_covered_distance)
    else:
        mean_covered_distance = -1
    if(len(config.pf_sp_time_needed) > 0):
        mean_time_needed = sum(config.pf_sp_time_needed) / len(config.pf_sp_time_needed)
    else:
        mean_time_needed = -1
    with open("testresults.txt", "a") as file:
        file.write(f"PF Starting Position: \nTotal number of tests: {number_tests}, #SUCCESS: {config.pf_sp_number_success}, in percent: {config.pf_sp_number_success/(number_tests)}\n")
        file.write(f"config.runner_mode = {config.runner_mode}")
        file.write(f"#Error end effector = {config.pf_sp_number_error_ee}\n")
        file.write(f"#Error tibia = {config.pf_sp_number_error_tibia}, #Error femur = {config.pf_sp_number_error_femur}, #Error coxa = {config.pf_sp_number_error_coxa}, #TIMEOUT = {config.pf_sp_number_timeout}\n")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}\n\n\n")

def statistics_astar_tang():
    """Prints all tracked statistics for the A* algorithm with extension inspired by Tang to testresults.txt
    """
    number_tests = config.astar_tang_number_success + config.astar_tang_number_error_tibia + config.astar_tang_number_error_femur + config.astar_tang_number_error_coxa + config.astar_tang_number_error_no_path + config.astar_number_error_ee + config.astar_tang_number_timeout
    if(number_tests == 0):
        with open("testresults.txt", "a") as file:
            file.write(f"A* algorithm Tang : \n Total number of tests: {number_tests}\n")
        return

    if(len(config.astar_tang_list_covered_distance) > 0):
        mean_covered_distance = sum(config.astar_tang_list_covered_distance) / len(config.astar_tang_list_covered_distance)
    else:
        mean_covered_distance = -1
    if(len(config.astar_tang_time_needed) > 0):
        mean_time_needed = sum(config.astar_tang_time_needed) / len(config.astar_tang_time_needed)
    else:
        mean_time_needed = -1
    with open("testresults.txt", "a") as file:
        file.write(f"A* algorithm Tang: \n Total number of tests: {number_tests}, #SUCCESS: {config.astar_tang_number_success}, in percent: {config.astar_tang_number_success/(number_tests)}\n")
        file.write(f"config.runner_mode = {config.runner_mode}")
        file.write(f"#Error end effector = {config.astar_tang_number_error_ee}, #Error timeout = {config.astar_tang_number_timeout}, #Error no path = {config.astar_tang_number_error_no_path}\n")
        file.write(f"#Error tibia = {config.astar_tang_number_error_tibia}, #Error femur = {config.astar_tang_number_error_femur}, #Error coxa = {config.astar_tang_number_error_coxa}\n")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}")
        mean_time_needed_calculation = sum(config.astar_tang_time_needed_calculation)/len(config.astar_tang_time_needed_calculation)
        file.write(f"Median time needed for calculation = {mean_time_needed_calculation}\n\n\n")
