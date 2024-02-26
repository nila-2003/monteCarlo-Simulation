**Monte Carlo Simulation**  function, models the probability of different outcomes in a process that involves random variables. 
For the given task, Monte Carlo Simulation is used to estimate completion time for a specified number of work items.
<br>
Here I have used the following parameters:
* Num_simulations = the number of times the simulation should be repeated to generate a distribution of possible outcomes.
* Num_items = The number of work items to simulate in each iteration of the monte carlo simulation.
<br>
Inside the function, the maximum completion time across all the sampled work items is recorded for each iteration. This represents an estimate of when the last work item is expected to be completed.
The function returns an array containing the recorded maximum completion times from each iteration.This represents a distribution of possible completion times for the specified
In short, the web application allows users to perform monte carlo simulations for a selected team and a specified number of work items.

The web page has a drop down to select a team from the available teams in the dataset.
Input field specifies the number of work items to stimulate.

Upon submitting, the monte carlo simulation is performed. The simulation is repeated 10,000 times to generate a distribution of possible completion time.
The histogram shows the distribution of maximum completion times across the simulated scenarios.
The red lines on the histogram represent confidence levels at 50%, 70%, and 85%.
 

**The problem statement was :**
* Determine items completion in 2 weeks
* Identify the time required for team A to complete 10 work items.
<br>
The monte-carlo simulation is utilized to generate a distribution of possible completion time for a specified number of work items based on the data.
The simulation is repeated multiple times and thus it captures the variability in completion times.
The application visualizes the Monte Carlo simulation results using histogram.
The histogram shows the distribution of maximum completion times for the number of work items.
The users can see the estimated completion times at different confidence levels, helping them understand the range of potential outcomes.
<br>                                             
For example, when prompted if i input the team as 2 and give the number of items as 8;
The application would filter the dataset to include only work items assigned to team 2.
The simulation is performed 10,000 times, simulating the completion times for 8 work items for team 2 in each iteration.
The visualization will show the distribution of maximum completion times for 8 work items in team 2.
The x-axis represents completion time and the y-axis represents the frequency of occurrences.
Thus, the histogram gives insight into the variability of the completion times for 8 work items in team 2, the confidence levels providing intervals within which the actual completion time is likely to fall.
