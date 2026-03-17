#CS4310 Programming Project #1 - Noah Ojeda
#Round Robin with Time Slice of 2 Algorithm

from collections import deque

#Function
def rr2(jobs):
    timeQuantum = 2
    currentTime = 0
    completed = 0
    n = len(jobs)

    #for this algorithm, remainingTime is set to the job's burstTime
    for job in jobs:
        job['remainingTime'] = job['burstTime']

    readyQueue = deque(jobs)
    
    results = []
    finished = set()

    #looping through the jobs
    while completed < n:
        job = readyQueue.popleft()

        if job['remainingTime'] <= 0:
            continue

        runtime = min(timeQuantum, job['remainingTime']) #minimum between the timeQuantum(2) and the remainingTime
        start = currentTime
        currentTime += runtime
        job['remainingTime'] -= runtime

        #if finished now, compute stats
        if job['remainingTime'] == 0:
            completion = currentTime
            turnaround = completion - job['arrivalTime']
            waiting = turnaround - job['burstTime']

            results.append({
                'id' : job['id'],
                'arrivalTime' : job['arrivalTime'],
                'burstTime' : job['burstTime'],
                'completionTime' : completion,
                'turnaroundTime' : turnaround,
                'waitingTime' : waiting
            })
            completed +=1
        
        else:
            #not finished put back at the end of the queue
            readyQueue.append(job)

    return results
