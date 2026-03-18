#CS4310 Programming Project #1 - Noah Ojeda
#First Come First Serve Algorithm 

from collections import deque

#Function for the first come first serve algorithm 
def fcfs(jobs):
    #sorting the jobs by arrival time
    jobs = sorted(jobs, key=lambda x: x['arrivalTime'])

    readyQueue = deque()
    currentTime = 0
    completed = 0
    n = len(jobs)
    i = 0 #index for arriving processes

    results = []

    #loop until all of the jobs are completed
    while completed < n:
        #adding all of the jobs that have the arrival time by the current time into the queue
        while i < n and jobs[i]['arrivalTime'] <= currentTime:
            readyQueue.append(jobs[i])
            i = i + 1
        #whille there are jobs in the queue
        if readyQueue:
            job = readyQueue.popleft()
            start = max(currentTime, job['arrivalTime']) #picks the max out of the current time and the arrival time of the job
            finish = start + job['burstTime']

            #appending the result along with its updated waitingTime and turnaroundTime 
            results.append({
                'id': job.get('id'),
                'arrivalTime' : job['arrivalTime'],
                'startTime' : start,
                'completionTime' : finish,
                'waitingTime' : start - job['arrivalTime'],
                'turnaroundTime' : finish - job['arrivalTime']
            })
            #updating the current time
            currentTime = finish
            #adding to number of jobs completed 
            completed +=1

        else:
            #if no jobs are in the ready queue
            currentTime = jobs[i]['arrivalTime']
    
    return results