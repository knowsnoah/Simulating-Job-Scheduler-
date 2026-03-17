# CS4310 Programming Project #1 - Noah Ojeda
# Part 2 (c) - Testing the data c. Test your program using the designed testing input data given in the table in Part
# 1(b), Make sure each program generates the correct answer by marking a “√” if it is correct#
# for each testing case for each program column in the table. Repeat the process of debugging if
# necessary.

#necessary imports from other files
import random
from fcfs import fcfs
from sjf import sjf
from rr2 import rr2
from rr5 import rr5
from main import generate_jobs
from main import average_turnaround
import copy

#fucntion for reading from a text file 
def read_jobs_from_file(filename : str):
    '''
    The file must be formatted in:
    Job1
    7
    Job2
    10
    etc.
    '''
    with open(filename, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    if len(lines) % 2 != 0:
        raise ValueError(f"{filename} has an odd number of non-empty lines. Expected job/burst pairs.")

    jobs = []
    for i in range(0, len(lines), 2):
        job_name = lines[i]          # ex "Job1"
        burst = int(lines[i + 1])    # ex "7"
        jobs.append({
            "id": job_name,          #"Job1"(string)
            "arrivalTime": 0,
            "burstTime": burst,
            "remainingTime": burst,  #RR needs this
            "startTime": -1,
            "completionTime": -1,
            "turnaroundTime": -1,
            "waitingTime": -1
        })
    return jobs


#function that runs all the algorithm and returns the results
def run_algorithms(jobs):
    fcfs_results = fcfs(copy.deepcopy(jobs))
    sjf_results = sjf(copy.deepcopy(jobs))
    rr2_results = rr2(copy.deepcopy(jobs))
    rr5_results = rr5(copy.deepcopy(jobs))

    return { #returning the average turnaround for each algorithm
        "fcfs" : average_turnaround(fcfs_results),
        "sjf" : average_turnaround(sjf_results),
        "rr2" : average_turnaround(rr2_results),
        "rr5" : average_turnaround(rr5_results)
    }

#function to run the test cases
def run_test_case(filename, expected=None):
    #methods previously defined
    jobs = read_jobs_from_file(filename)
    avgs = run_algorithms(jobs)

    #printing the results
    print(f"\n=== Results for {filename} ===")
    for k in ["fcfs", "sjf", "rr2", "rr5"]:
        val = avgs[k]
        if expected and k in expected:
            ok = "√" if round(val, 1) == round(expected[k], 1) else "X" #using rounding because expected results are only to one decimal spot
            print(f"{k}: {val:.1f}  (expected {expected[k]:.1f})  {ok}")
        else:
            print(f"{k}: {val:.1f}")

    return avgs



#running all the test cases in main and comparing them to the expected outcome already 
#calculated in 1(b)
if __name__ == "__main__":

    #these are the results from Part 1(b)
    expected_5 = {
        "fcfs": 31.4,
        "sjf":  24.0,
        "rr2": 36.4,
        "rr5": 36.0
    }

    expected_10 = {
        "fcfs": 52.9,
        "sjf":  38.8,
        "rr2": 65.9,
        "rr5": 63.7
    }

    expected_15 = {
        "fcfs": 71.4,
        "sjf":  46.9,
        "rr2": 82.1,
        "rr5": 81.5
    }

    #check
    run_test_case("test5.txt", expected=expected_5)
    run_test_case("test10.txt", expected=expected_10)
    run_test_case("test15.txt", expected=expected_15)