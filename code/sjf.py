#CS4310 Programming Project #1 - Noah Ojeda
#Shortest Job First Algorithm

from collections import deque

#Function  
def sjf(jobs):
    #sort the jobs by shortest burst time first
    jobs = sorted(jobs, key=lambda x: x['burstTime'])
    currentTime = 0
    results = []

    #loop through the jobs
    for job in jobs:
        start = currentTime
        finish = start + job['burstTime']

        results.append({
            'id' : job.get('id'),
            'arrivalTime' : job['arrivalTime'],
            'startTime' : start,
            'completionTime' : finish,
            'waitingTime' : start - job['arrivalTime'],
            'turnaroundTime' : finish - job['arrivalTime']
        })

        currentTime = finish

    return results
