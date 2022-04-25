from aStar import aStar
from aStarMan import aStarMan
from BFS import BFS
from DFS import DFS
from midBid import mid1, mid2
from midBidMan import mid1Man, mid2Man
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit

# myMaze=maze(30,40)
# myMaze.CreateMaze(loopPercent=100)
# searchPath,aPath,fwdPath=aStar(myMaze)
# searchPath2,aPath2,fwdPath2=aStar2(myMaze)

# l=textLabel(myMaze,'Manhattan',len(fwdPath)+1)
# l=textLabel(myMaze,'Euclidean',len(fwdPath2)+1)
# l=textLabel(myMaze,'Manhattan',len(searchPath)+1)
# l=textLabel(myMaze,'Euclidean',len(searchPath2)+1)

# a=agent(myMaze,footprints=True,color=COLOR.cyan,filled=True)
# b=agent(myMaze,footprints=True,color=COLOR.yellow)
# myMaze.tracePath({a:fwdPath},delay=50)
# myMaze.tracePath({b:fwdPath2},delay=50)

# t1=timeit(stmt='aStar(myMaze)',number=100,globals=globals())
# t2=timeit(stmt='aStar2(myMaze)',number=100,globals=globals())

# textLabel(myMaze,'Manhattan Time',t1)
# textLabel(myMaze,'Euclidean Time',t2)


# myMaze.run()
sunmspatha=0
sumpatha=0

sumspatham=0
sumpatham=0


sumspathmid=0
sumpathmid=0

sumspathmidman=0
sumpathmidman=0

sumspathb=0
sumpathb=0

sumspathd=0
sumpathd=0


for _ in range(1000):
    m=maze(25,25)
    m.CreateMaze()
    searchPath,aPath,fwdPath=aStar(m)
    patha=len(fwdPath) + 1
    spatha=len(searchPath)

    msearchPath, maPath, mfwdPath = aStarMan(m)
    patham=len(mfwdPath) + 1
    spatham=len(msearchPath)

    spath, path = mid1(m)
    spath2, path2 = mid2(m)
    spathmid=len(spath) + len(spath2) - 1
    pathmid=len(path) + len(path2) + 1

    mspath, mpath=mid1Man(m)
    mspath2,mpath2=mid2Man(m)
    spathmidman = len(mspath) + len(mspath2) - 1
    pathmidman = len(mpath) + len(mpath2) + 1


    bSearch, bfsPath, fwdPathb = BFS(m)
    pathb=len(fwdPathb) + 1
    if (len(bSearch) == 7 * 7 - 2):
        spathb=len(bSearch) + 2
    else:
        spathb=len(bSearch)


    dSeacrh, dfsPath, fwdPathd = DFS(m)
    spathd=len(dSeacrh) + 1
    pathd=len(fwdPathd) + 1

    sunmspatha = spatha+sunmspatha
    sumpatha = patha+sumpatha

    sumspatham = spatham + sumspatham
    sumpatham = patham + sumpatham

    sumspathmid = spathmid + sumspathmid
    sumpathmid = pathmid+sumpathmid

    sumspathmidman = sumspathmidman + spathmidman
    sumpathmidman = sumpathmidman + pathmidman

    sumspathb = spathb + sumspathb
    sumpathb = pathb+sumpathb

    sumspathd = spathd+sumspathd
    sumpathd = pathd+sumpathd


print('Final Path Comparison Result')
print('Search Path for Astar Euclidian ', sunmspatha/1000)
print('Final Path for Astar Euclidian ', (sumpatha/1000))
print('')

print('Search Path for Astar Manhattan ', sumspatham/1000)
print('Final Path for Astar Manhattan ', (sumpatham/1000))
print('')

print('Search Path for Bidirectional Midpoint Euclidian ', sumspathmid/1000)
print('Final Path for Bidirectional Midpoint Euclidian ', (sumpathmid/1000))
print('')

print('Search Path for Bidirectional Midpoint Manhattan ', sumspathmidman/1000)
print('Final Path for Bidirectional Midpoint Manhattan ', (sumpathmidman/1000))
print('')

print('Search Path for BFS ', sumspathb/1000)
print('Final Path for BFS', (sumpathb/1000))
print('')

print('Search Path for DFS ', sumspathd/1000)
print('Final Path for DFS ', (sumpathd/1000))
print('')


