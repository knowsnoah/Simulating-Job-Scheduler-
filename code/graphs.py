import matplotlib.pyplot as plt

# data from your experimental results
input_sizes = [5, 10, 15]

fcfs_avg = [2.27, 3.25, 2.81]
sjf_avg = [1.94, 2.55, 2.45]
rr2_avg = [3.12, 4.37, 4.02]
rr5_avg = [2.88, 4.27, 3.65]

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