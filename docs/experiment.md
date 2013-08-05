# Experiments

Would you like to be able to run a simple experiment using a novel scenario
to gather data to test your hypothesis?

Create a scenario, allow users to interact with the scenario, then collect
the results and process them. You potenially have a way to run a series 
of mini experiment asking yourself, 'what-if' type questions, then seeing 
the results. 

Instead of a guessing you can test to see if your hypothosis matches the results? 
The feedback look should allow you to improve individual or team output.


## Testing

Quantitative. 

Independent of scenario messaging is the idea of testing messages received. 
The idea is to put a number or value to a response or set of responses.


    "There are still ways to handle the test scenario, 
    good way of evaluating skillsets for sourcing accurate, timely
    information." [0]
    

Some simple things that I'd like to be able to test:

### Time 

Each message has a timestamp. Each message can also be tracked in relation to 
scenario checkpoints. [1]

* Q What is the time taken for any message to be posted once controller has issued a message
* Q What is the frequency of messages with known workload over given exercise 


### Count

Count instances of some variable to be tested. Result is an integer.

* Q: How many times is the same message repeated?
* Q: How many URL's are posted?


### Boolean

Test the truth of a variable. Results in True or False.

    "some resources from 4 years ago changed or not available, 
    so updating latest resources comes into play." [2]

* Q: Are resouces shown still relevant?
* Q: URL posted valid?
* Q: URL posted current?


### Collection

A message may consist of a number of different combinations of information.
A collection could represent different parts that make up a message.

* Q: Does the message contain > 50% of what is required for a valid message?


## Resources

[0] [@geehall1](https://twitter.com/geehall1)
<https://twitter.com/geehall1/status/364146712455024640>

[1] A scenario is made up of a series of events. A checkpoint is an event 
that we have some particular interest in. We might want to measure the time
between an important bit of information was transmitted and received.

[2] @geehall1
<https://twitter.com/geehall1/status/364146230932152320>


vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
