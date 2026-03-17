#cs4310 project - Noah Ojedaa
#four job scheduling algorithms: FCFS, SJF, RR-2, and PR-5

#imports to get algorithm from their respective files
import random
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

#generate jobs for testing
