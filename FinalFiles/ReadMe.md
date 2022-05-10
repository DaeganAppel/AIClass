# To run - first download all files
# Then ensure you have the pyamaze library installed or working on your machine.
## This code was demonstrated to be working on Pyamaze Python 3.7
### You can run any one file by itself to produce a visualization by pressing the run button on the specific file in PyCharm. 
### Alternatively you can run the comparison file of them all to see compariosn of results but not a visualization


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
