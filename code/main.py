#cs4310 project - Noah Ojedaa
#four job scheduling algorithms: FCFS, SJF, RR-2, and RR-5

#imports to get algorithm from their respective files
import random
import copy
from fcfs import fcfs
from sjf import sjf
from rr2 import rr2
from rr5 import rr5

#function for generating the number of jobs (num_jobs) with the random burst time between 1 and 20
def generate_jobs(num_jobs):
    jobs = []
    for i in range(num_jobs):
        burstTime = random.randint(1, 20) #1-20 random burst time
        jobs.append({
            'id' : i+1,
            'arrivalTime' : 0,
            'burstTime' : burstTime,
            'remainingTime' : burstTime, 
            'startTime' : -1,
            'completionTime' : -1,
            'turnaroundTime' : -1,
            'waitingTime' : -1
        })

    return jobs

#function to find the averege turnaround time 
def average_turnaround(results):
    total = 0
    for job in results:
        total += job['turnaroundTime']
    return total / len(results)  #total turnaround time / # of jobs

#function to write the jobs randomly generated into the "jobs.txt" file
def write_jobs_to_file(jobs, filename="jobs.txt"):
    with open(filename, "w") as f:
        for job in jobs:
            f.write(f"Job{job['id']}\n")
            f.write(f"{job['burstTime']}\n")



#GENERATING JOBS FOR TESTING - PART 3
def run_experiment():
    #number of trials
    trial_size = 20
    job_sizes = [5, 10, 15]

    for size in job_sizes:
        #variable to hold the results
        fcfs_total = 0
        sjf_total = 0
        rr2_total = 0 
        rr5_total = 0

        #20 trails for each job size and schedule algorithm 
        for trial in range(trial_size):
            jobs = generate_jobs(size) #generating 5, 10, and 15 jobs 

            #using deepcopy to make sure each one gets the same input of jobs
            fcfs_results = fcfs(copy.deepcopy(jobs))
            sjf_results = sjf(copy.deepcopy(jobs))
            rr2_results = rr2(copy.deepcopy(jobs))
            rr5_results = rr5(copy.deepcopy(jobs))

            fcfs_total += average_turnaround(fcfs_results)
            sjf_total += average_turnaround(sjf_results)
            rr2_total += average_turnaround(rr2_results)
            rr5_total += average_turnaround(rr5_results)

        #computing the average of the averages after 20 trials
        fcfs_avg = fcfs_total / trial
        sjf_avg = sjf_total / trial
        rr2_avg = rr2_total / trial
        rr5_avg = rr5_total / trial

        #returning the averages of each job size[5, 10, 15] for each schedule algorithm 
        print("Input Size | FCFS Avg TAT | SJF Avg TAT | RR-2 Avg TAT | RR-5 Avg TAT")
        print(f"{size:^10} | {fcfs_avg:^12.2f} | {sjf_avg:^11.2f} | {rr2_avg:^12.2f} | {rr5_avg:^12.2f}")


#RUNNING run_experiment
if __name__ == "__main__":
    run_experiment()



            




