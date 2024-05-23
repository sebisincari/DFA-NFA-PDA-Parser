def createGraph(fct):
    graph = {}
    for (st,op) in fct:
        dr = int(fct[(st,op)])
        if int(st) not in graph and st!=dr:
            graph[int(st)] = [dr]
        elif st!=dr:
            graph[int(st)].append(int(dr))
    # graph = dict(sorted(graph.items(), key=lambda item: -len(item[1])))
    
    return graph
    
def dfs(i,graph,h):
    global viz
    global maxH
    if h > maxH:
        maxH = h
    viz[i] = 1
    for j in graph[i]:
        if viz[j] == 0:
            dfs(j, graph, h+1)
            
def dfsForRoad (graph ,H ,i ,h):
    global viz
    global maxH
    global stack
    global st
    if h == H:
        stack = st.copy()
    viz[i] = 1
    # print("HERE")
    for j in graph[i]:
        if viz[j] == 0:
            st.append(j)
            # print(st)
            dfsForRoad(graph,H,j,h+1)
            st.pop()
    
    
def maxLen(graph):
    global viz
    global maxH
    H=0
    for i in graph:
        viz = [0]*len(graph)
        maxH = -1
        dfs(i,graph,1)
        if maxH > H:
            H = maxH
            imax = i
    # print(imax)
    return (H,imax)


def mainRoad(graph):
    global stack
    global st
    global viz
    
    (heigh,start) = maxLen(graph)
    # print(heigh)
    st = [start]
    viz = [0]*len(graph)
    dfsForRoad(graph,heigh,start,1)
    return stack
    
# def updateGraph(graph):
    
def find_element(matrix, element):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == element:
                return (i, j)
    return None
    
def createMap(graph):
    map = []
    mainR= mainRoad(graph)
    map.append(mainR)
    lenght = len(mainR) 
    for i in range(1,lenght-1):
        j=i-1
        if mainR[i] in graph and mainR[j] in graph[mainR[i]]:
            graph[mainR[i]].remove(mainR[j])
        if mainR[j] in graph and mainR[i] in graph[mainR[j]]:
            graph[mainR[j]].remove(mainR[i])
            
    graph = {key: val for key, val in graph.items() if val}
    
    graph = dict(sorted(graph.items(), key=lambda item: -len(item[1])))

    #cat timp mai sunt noduri ne asezate pe harta
    #punem deasupra mai intai sau dedesubtul drumului principal in cazul in care nu se poate pune deasupra
    while graph:
        print(graph)
        newLine = [-1]*lenght
        nrlines = len(map)
        for i in graph:
            (lin,col) = find_element(map,i)
            if (lin,col) != None:
                if lin == 0:
                    newLine[col] = graph[i][0]
                    if i in graph and graph[i][0] in graph[i]:
                        graph[i].remove(graph[i][0])
                    if graph[i][0] in graph and graph[i] in graph[graph[i][0]]:
                        graph[graph[i][0]].remove(graph[i])
                    map.insert(0,newLine)
                    graph = {key: val for key, val in graph.items() if val}
                elif map[lin-1][col] == -1:
                    map[lin-1][col] = graph[i][0]
                    if i in graph and graph[i][0] in graph[i]:
                        graph[i].remove(graph[i][0])
                    if graph[i][0] in graph and graph[i] in graph[graph[i][0]]:
                        graph[graph[i][0]].remove(graph[i])
                    graph = {key: val for key, val in graph.items() if val}
                elif map[lin-1][col] != -1:
                    newLine[col] = graph[i][0]
                    if i in graph and graph[i][0] in graph[i]:
                        graph[i].remove(graph[i][0])
                    if graph[i][0] in graph and graph[i] in graph[graph[i][0]]:
                        graph[graph[i][0]].remove(graph[i])
                    map.append(newLine)
                    graph = {key: val for key, val in graph.items() if val}
                
        
            
    print(graph)
    print(map)