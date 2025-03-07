import config

def statistics_a_star():
    """Prints all tracked statistics for the conventional A* algorithm to testresults.txt
    """
    number_tests = config.astar_number_success + config.astar_number_error_tibia + config.astar_number_error_femur + config.astar_number_error_coxa + config.astar_number_error_no_path
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
        file.write(f"#Error tibia = {config.astar_number_error_tibia}, #Error femur = {config.astar_number_error_femur}, #Error coxa = {config.astar_number_error_coxa}")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}")
        mean_time_needed_calculation = sum(config.astar_time_needed_calculation)/len(config.astar_time_needed_calculation)
        file.write(f"Median time needed for calculation = {mean_time_needed_calculation}\n")

def statistics_pf():
    """Prints all tracked statistics for the conventional Potential Field method
    """
    number_tests = config.pf_number_success + config.pf_number_error_tibia + config.pf_number_error_femur + config.pf_number_error_coxa + config.pf_number_timeout
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
        file.write(f"#Error tibia = {config.pf_number_error_tibia}, #Error femur = {config.pf_number_error_femur}, #Error coxa = {config.pf_number_error_coxa}, #TIMEOUT = {config.pf_number_timeout}")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}\n")
     
def statistics_a_star_elbow():
    """Prints all tracked statistics for the A* algorithm with changing elbow posture
    """
    number_tests = config.elbow_start_position_number_success + config.elbow_start_position_number_timeout + config.elbow_start_position_number_error_tibia + config.elbow_start_position_number_error_femur + config.elbow_start_position_number_error_coxa
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
        file.write(f"#Error tibia = {config.elbow_start_position_number_error_tibia}, #Error femur = {config.elbow_start_position_number_error_femur}, #Error coxa = {config.elbow_start_position_number_error_coxa}, #TIMEOUT = {config.elbow_start_position_number_timeout}")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}")
        mean_time_needed_calculation = sum(config.elbow_start_position_time_needed_calculation)/len(config.elbow_start_position_time_needed_calculation)
        file.write(f"Median time needed for calculation = {mean_time_needed_calculation}\n")

def statistics_naive():
    """Prints the tracked statistics of the naive approach to testresults.txt
    """
    number_tests = config.naive_number_success + config.naive_number_error_tibia + config.naive_number_error_femur + config.naive_number_error_coxa
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
        number_tests = config.naive_number_success + config.naive_number_error_tibia + config.naive_number_error_femur + config.naive_number_error_coxa
        file.write(f"Naive: \nTotal number of tests: {number_tests}, #SUCCESS: {config.naive_number_success}, in percent: {config.pf_number_success/(number_tests)}\n")
        file.write(f"#Error tibia = {config.naive_number_error_tibia}, #Error femur = {config.naive_number_error_femur}, #Error coxa = {config.naive_number_error_coxa}")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}\n")
     
# Statistics: mode 4 : PF applied to all links
def statistics_pf_linkage():
    """Prints the tracked statistics of pf applied to all links to testresults.txt
    """
    number_tests = config.pf_all_links_number_success + config.pf_all_links_number_timeout + config.pf_all_links_number_error_tibia + config.pf_all_links_number_error_femur + config.pf_all_links_number_error_coxa
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
        file.write(f"#Error tibia = {config.pf_all_links_number_error_tibia}, #Error femur = {config.pf_all_links_number_error_femur}, #Error coxa = {config.pf_all_links_number_error_coxa}, #TIMEOUT = {config.pf_all_links_number_timeout}")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}\n")
     
# Statistics: mode 5/A* with specific start position
def statistics_a_star_start_position():
    """Prints the tracked statistics of A* with start position to testresults.txt
    """
    number_tests = config.astar_start_position_number_success + config.astar_start_position_number_timeout + config.astar_start_position_number_error_tibia + config.astar_start_position_number_error_femur + config.astar_start_position_number_error_coxa
    if(number_tests == 0):
        with open("testresults.txt", "a") as file:
            file.write(f"A* start position: \n Total number of tests: {number_tests}\n")
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
        file.write(f"#Error tibia = {config.astar_start_position_number_error_tibia}, #Error femur = {config.astar_start_position_number_error_femur}, #Error coxa = {config.astar_start_position_number_error_coxa}, #TIMEOUT = {config.astar_start_position_number_timeout}")
        file.write(f"Median covered distance = {mean_covered_distance}, median time needed = {mean_time_needed}\n")
        mean_time_needed_calculation = sum(config.astar_start_position_time_needed_calculation)/len(config.astar_start_position_time_needed_calculation)
        file.write(f"Median time needed for calculation = {mean_time_needed_calculation}")
