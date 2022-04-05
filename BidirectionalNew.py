from math import ceil
from pyamaze import maze, agent, textLabel, COLOR
from pyamaze import maze,agent,textLabel
from queue import PriorityQueue
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)

def aStar(m):
    start=(ceil(m.rows/2),ceil(m.cols/2))
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))

    open=PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    aPath={}
    searchPath = [start]
    while not open.empty():
        currCell=open.get()[2]
        searchPath.append(currCell)
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,(1,1))

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,(1,1)),childCell))
                    aPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return searchPath, fwdPath

def aStar2(m):
    start=(ceil(m.rows/2),ceil(m.cols/2))
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(m.rows,m.cols))

    open=PriorityQueue()
    open.put((h(start,(m.rows,m.cols)),h(start,(m.rows,m.cols)),start))
    aPath={}
    searchPath = [start]
    while not open.empty():
        currCell=open.get()[2]
        searchPath.append(currCell)
        if currCell==(m.rows,m.cols):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,(m.rows,m.cols))

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,(m.rows,m.cols)),childCell))
                    aPath[childCell]=currCell
    fwdPath={}
    cell=(m.rows,m.cols)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return searchPath,fwdPath

if __name__=='__main__':
    m=maze(11,11)
    m.CreateMaze()

    spath, path=aStar(m)
    spath2,path2=aStar2(m)
    Mode = 0 #If Mode = 0 prints search path if Mode = 1 prints finished path
    if(Mode==0):
        af=agent(m, x=ceil(m.rows/2), y=ceil(m.cols/2), filled=True, footprints=True)
        bf = agent(m, x=ceil(m.rows / 2), y=ceil(m.cols / 2), filled=True, color=COLOR.yellow, footprints=True)
        m.tracePath({af: spath},delay=100)
        m.tracePath({bf: spath2}, delay=100)
    if(Mode==1):
        a = agent(m, x=ceil(m.rows / 2), y=ceil(m.cols / 2), footprints=True)
        b = agent(m, x=ceil(m.rows / 2), y=ceil(m.cols / 2), color=COLOR.yellow, footprints=True)
        m.tracePath({a: path}, delay=100)
        m.tracePath({b: path2}, delay=100)


    l=textLabel(m,'A Star Path Length',len(path)+len(path2)+1)#would be + 2 since they both start at a value 0 but they overlap the same middle square so plus one
    print(path2)
    m.run()