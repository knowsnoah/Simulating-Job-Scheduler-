import matplotlib.pyplot as plt

# data from your experimental results
input_sizes = [5, 10, 15]

fcfs_avg = [33.72, 58.63, 85.55]
sjf_avg = [26.99, 44.44, 59.44]
rr2_avg = [41.35, 75.08, 105.09]
rr5_avg = [40.71, 73.66, 104.75]

# FCFS graph
plt.figure()
plt.plot(input_sizes, fcfs_avg, marker='o')
plt.title("FCFS: Average Turnaround Time vs Input Size")
plt.xlabel("Input Size (# of jobs)")
plt.ylabel("Average Turnaround Time")
plt.grid(True)
plt.show()

# SJF graph
plt.figure()
plt.plot(input_sizes, sjf_avg, marker='o')
plt.title("SJF: Average Turnaround Time vs Input Size")
plt.xlabel("Input Size (# of jobs)")
plt.ylabel("Average Turnaround Time")
plt.grid(True)
plt.show()

# RR-2 graph
plt.figure()
plt.plot(input_sizes, rr2_avg, marker='o')
plt.title("RR-2: Average Turnaround Time vs Input Size")
plt.xlabel("Input Size (# of jobs)")
plt.ylabel("Average Turnaround Time")
plt.grid(True)
plt.show()

# RR-5 graph
plt.figure()
plt.plot(input_sizes, rr5_avg, marker='o')
plt.title("RR-5: Average Turnaround Time vs Input Size")
plt.xlabel("Input Size (# of jobs)")
plt.ylabel("Average Turnaround Time")
plt.grid(True)
plt.show()

#This graph graphs all the lines on the same graph to be able to compare them 
plt.figure()
plt.plot(input_sizes, fcfs_avg, marker='o', label='FCFS')
plt.plot(input_sizes, sjf_avg, marker='o', label='SJF')
plt.plot(input_sizes, rr2_avg, marker='o', label='RR-2')
plt.plot(input_sizes, rr5_avg, marker='o', label='RR-5')

plt.title("Average Turnaround Time vs Input Size")
plt.xlabel("Input Size (# of jobs)")
plt.ylabel("Average Turnaround Time")

plt.legend()   # shows which line is which
plt.grid(True)

plt.show()