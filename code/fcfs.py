#CS4310 Programming Project #1 - Noah Ojeda
#First Come First Serve Algorithm 

from collections import deque

#Function
def fcfs(jobs):
    #sorting the jobs by arrival time
    jobs = sorted(jobs, key=lambda x: x['arrivalTime'])

    readyQueue = deque()
    currentTime = 0
    completed = 0
    n = len(jobs)
    i = 0 #index for arriving processes

    results = []

    while completed < n:
        while i < n and jobs[i]['arrivalTime'] <= currentTime:
            readyQueue.append(jobs[i])
            i = i + 1
        if readyQueue:
            job = readyQueue.popleft()
            start = max(currentTime, job['arrivalTime']) #picks the max out of the current time and the arrival time of the job
            finish = start + job['burstTime']

            results.append({
                'id': job.get('id'),
                'arrivalTime' : job['arrivalTime'],
                'startTime' : start,
                'completionTime' : finish,
                'waitingTime' : start - job['arrivalTime'],
                'turnaroundTime' : finish - job['arrivalTime']
            })
            currentTime = finish
            completed +=1

        else:
            #if no jobs are in the ready queue
            currentTime = jobs[i]['arrivalTime']
    
    return results