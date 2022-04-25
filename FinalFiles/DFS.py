# from pyMaze import maze,agent,COLOR,textLabel
from pyamaze import maze,agent,textLabel,COLOR

def DFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    dSeacrh=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        dSeacrh.append(currCell)
        if currCell==m._goal:
            break
        poss=0
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                poss+=1
                explored.append(child)
                frontier.append(child)
                dfsPath[child]=currCell
        if poss>1:
            m.markCells.append(currCell)
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dSeacrh,dfsPath,fwdPath

if __name__=='__main__':
    m = maze(5, 5)
    m.CreateMaze(theme='light')

    dSeacrh,dfsPath,fwdPath=DFS(m) # (5,1) is Start Cell, Change that to any other valid cell

    a = agent(m, footprints=True, color=COLOR.yellow, shape='square', filled=True)
    b = agent(m, footprints=True, color=COLOR.red, shape='square', filled=False)
    # c=agent(m,5,4,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
    #c = agent(m, footprints=True, color=COLOR.cyan, shape='square', filled=False)
    m.tracePath({a: dSeacrh}, delay=100)
    m.tracePath({b: fwdPath}, delay=100)
    textLabel(m, 'DFS Path Length', len(fwdPath) + 1)
    l = textLabel(m, 'DFS Star Search Length', len(dSeacrh)+1)
    m.run()
