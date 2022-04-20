# Jack Micher
# 10/15/2020
# CSIT 200

import priority_queue
import csv

class CPUJob:
    """ Class that stores Job time and name """
    
    def __init__(self, time, title):
        self._time = time
        self._title = title
    
    def get_time(self):
        """ Return current time of Job """
        return self._time
    
    def get_title(self):
        """ Return title of Job """
        return self._title
    
    def countdown(self):
        """ Countdown time of job by -1 """
        self._time -= 1

cpu_count = int(input("Enter number of CPUs: "))      # User inputs of CPU and file name
file_name = input("Enter filename: ")                 #

with open(file_name) as cpu_input:                    # normally is 'file-input.csv'
    csv_cpu = csv.reader(cpu_input, delimiter=",")
    cycle_count = 1                                   # Counter for the total amount of rows in the csv
    total_jobs = 0                                    # Total amount of jobs finished (starts at 0)
    
    active_jobs = ['-']*cpu_count                     # Empty list to store active jobs
    process_string = ['-']*cpu_count                  # List that will be joined later to make a string every loop
    queued_jobs = priority_queue.HeapPriorityQueue()  # Make a HeapPriorityQueue to store jobs 
    
    for job in csv_cpu: # If the program finds a job tuple, job[0] is the name, job[1] is the job length, job[2] is the priority key
        
        if job[0] != "No job":
            queued_jobs.add(int(job[2]),[job[0], job[1]]) # If a job is found in the csv, push it into the priority heap for later use
        
        for i in active_jobs:
            if i == '-' and not queued_jobs.is_empty(): # If there is an empty job slot and the queue has a job, place job in the empty slot
                                                        # (This could have been implemented in one combined loop with the next loop)
                empty_index = active_jobs.index('-')
                start_job = queued_jobs.remove_min()
                current = CPUJob(int(start_job[1][1]),start_job[1][0])
                active_jobs[empty_index] = current
            
        for i in range(len(active_jobs)):
            if active_jobs[i] != '-': # If there is a current job at this position of the active_jobs list
                if int(active_jobs[i].get_time()) <= 0: # If a job finishes up its job time, determine what to do
                    total_jobs += 1 # Increment completed jobs by 1
                    if queued_jobs.is_empty() is not True:                 # If the job queue is not empty, unqueue the job place it into the CPU slot
                        new_job = queued_jobs.remove_min()
                        current = CPUJob(int(new_job[1][1]),new_job[1][0])
                        active_jobs[i] = current
                        process_string[i] = active_jobs[i].get_title()
                    else:                                                  # If job queue is empty, make the CPU slot empty
                        process_string[i] = '-'
                        active_jobs[i] = '-'
                else:
                    process_string[i] = active_jobs[i].get_title()
        
        fullstr = str(cycle_count) + ': ' + ", ".join(process_string)      # Create the string to output
        print(fullstr)
        
        cycle_count += 1                                                   # row counter +1
        
        for i in range(len(active_jobs)):                                  # Every active jobs countdown by 1
            if active_jobs[i] != '-':
                active_jobs[i].countdown()
    
    print("Total number of jobs completed: " + str(total_jobs))            # At the end of loop, report total jobs finished in the program