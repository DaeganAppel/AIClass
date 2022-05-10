# To run - first download all files
# Then ensure you have the pyamaze library https://github.com/MAN1986/pyamaze installed or working on your machine.
## This code was demonstrated to be working on Pyamaze Python 3.7
### You can run any one file by itself to produce a visualization by pressing the run button on the specific file in PyCharm. 
### Alternatively you can run the comparison file of them all to see compariosn of results but not a visualization

# Sample Output
![Sample Novel Bidirectional Graph](https://github.com/DaeganAppel/AIClass/blob/main/Images/MidBid.PNG)

## In this case the Big colored squares are the seach path and the small squares are the final path *Note this may differ per file so check the setting on the file you are running

![Sample Comparison Output for 5x5 (loopPercent=0)](https://github.com/DaeganAppel/AIClass/blob/main/Images/ComparisonOutput.PNG)
## Sample Comparison Output
# FAQs
## How do I change the maze size?
### Edit the line shown below.
### The first value is rows then the second value is columns.
```
m=maze(11,11)
```
## How do I save a randomly generated maze?
### This will save the created maze into a csv named to the Time and Date it was created
```
m.CreateMaze(saveMaze=True, theme='light')
```
## How do I load a maze?
### After saving a maze you may load it as shown below
```
 m.CreateMaze(loadMaze='maze--2022-04-17--15-44-17.csv', theme='light')
 ```
 
 
