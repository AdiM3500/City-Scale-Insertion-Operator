# All baseline C++ code made by Gong et. al. Repo link: https://github.com/gzyhkust/Insertion-Operator

# Guide to running code:

## Baseline:

- cd into code Directory
- make clean
- make n
- use linux command:time ./n <requests_path> <workers_path>
  - example: time ./n ../Data/Cainiao/requests_baseline.txt ../Data/Cainiao/LogisticWorkers.txt (for running the baseline insertion operator on the Cainiao requests and worker datasets)

- If you wish to change the number of workers or requests
  - Go to /Data/<Dataset>/requests_baseline.txt and change the top line to signify the number of requests
    - The individual request data is in the form <Requests appearance time, Start Node, End Node, Capacity, Deadline, time-dependent Shortest Path> for **Logistics** and <Request appearance time, start node, end node, capacity, time-dependent Shortest Path> for **Ridesharing**
  - Go to /Data/<Dataset>/LogisticWorkers.txt and change the first number in the first line (the first line signifies: NumofWorkers, Capacity of each worker, GridL (not relevant), alpha (not relevant)
 
  
