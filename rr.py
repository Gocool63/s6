def findWaitingTime(processes, n, bt,wt, quantum):
	rem_bt = [0] * n
	for i in range(n):
		rem_bt[i] = bt[i]
	t = 0
	while(1):
		done = True
		for i in range(n):
			if (rem_bt[i] > 0) :
				done = False
				if (rem_bt[i] > quantum) :

					t += quantum
					rem_bt[i] -= quantum
				else:
					t = t + rem_bt[i]
					wt[i] = t - bt[i]
					rem_bt[i] = 0
		if (done == True):

			break
def findTurnAroundTime(processes, n, bt, wt, tat):
	for i in range(n):
		tat[i] = bt[i] + wt[i]
def findavgTime(processes, n, bt, quantum,at):
	wt = [0] * n
	tat = [0] * n
	findWaitingTime(processes, n, bt,
wt, quantum)
	findTurnAroundTime(processes, n, bt,
wt, tat)
	print("Process\t\tAT\t\tBT\t\tCT\t\tWT\t\tTAT")
	total_wt = 0
	total_tat = 0
	for i in range(n):
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		ct = at[i]+tat[i]
		print(" ","P", i + 1, "\t\t",at[i], "\t\t",bt[i],"\t\t",ct,
"\t\t", wt[i], "\t\t", tat[i])
	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = %.5f "% (total_tat / n))
if __name__ =="__main__":
	proc = [1, 2, 3, 4]
	n = 4
	burst_time = [21, 3, 6,2]
	a_t=[0,0,0,0]
	quantum = 5;
	findavgTime(proc, n, burst_time, quantum,a_t)