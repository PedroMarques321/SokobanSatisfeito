from collections import deque

def restrict(X, a, Y, b):
    return a!=b
    
def csp_possivel_solucao(caixas,goals_alcancaveis):
    dominios = {}
    neighbours = {}
    if len(caixas) > 1:
        for v in caixas:
            neighbours[v] = [x for x in caixas if x != v]

    for v in caixas :
        if v in goals_alcancaveis.keys():
            dominios[v] = goals_alcancaveis[v]
        else:
            dominios[v] = []
    
    return CSP(caixas, dominios, neighbours, restrict)

def can_reach_goal(start):

    if start == sokoban_goal:
        return True

    queue = deque([start])
    visited = set([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        current = queue.popleft()
        
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if neighbor in sokoban.navegaveis and neighbor not in sokoban.proibidas and neighbor not in visited and (current[0] - dx, current[1] - dy) in sokoban.navegaveis:

                if neighbor == sokoban_goal:
                    return True

                visited.add(neighbor)
                queue.append(neighbor)
    
    return False

def constraints(A, a, B, b):
    
    if a == 0 and b == 0:
        return not can_reach_goal(A) and not can_reach_goal(B)
    if a == 1 and b == 0:
        return can_reach_goal(A) and not can_reach_goal(B)
    if a == 0 and b == 1:
        return not can_reach_goal(A) and can_reach_goal(B)
    if a == 1 and b == 1:
        return can_reach_goal(A) and can_reach_goal(B)
   
def csp_find_alcancaveis_1goal(s, goal):

    global sokoban  
    global sokoban_goal
    sokoban_goal = goal

    sokoban = s 
    variables = list(s.navegaveis) + list(s.proibidas)
    variables = sorted(set(variables), key=lambda x: (x[0], x[1]))
    
    buffer = []
    neighbours = {}
    dominio = {}
    traps = {}
    no_neighbours = []
    dict_actions = [(-1,0), (0,-1), (0,1), (1,0)]
    
    for x in variables:
        if x in s.calc_traps():
            dominio[x] = [0]
            traps[x] = 0
        else:
            dominio[x] = [0, 1]
    
    for x in variables:
        if x not in traps:
            buffer = []
            for y in dict_actions:

                nx, ny = x[0] + y[0], x[1] + y[1]
                if (nx, ny) in variables and (nx, ny) not in traps:
                    buffer.append((nx, ny))
            
            if buffer:
                neighbours[x] = buffer
            else:
                no_neighbours.append(x)
                neighbours[x] = []
    
    for i in no_neighbours:
        dominio[i] = [0]
        for k in neighbours.keys():
            if i in neighbours[k]:
                neighbours[k].remove(i)
    
    dominio[goal] = [1]

    return CSP(variables, dominio, neighbours, constraints)   
 

def possivel_solucao(caixas,goals_alcancaveis):
    csp_sokoban1 = csp_possivel_solucao(caixas,goals_alcancaveis) # <--- a vossa função csp_possivel_solucao 
    r = backtracking_search(csp_sokoban1, inference = forward_checking)
    return r
    
def find_alcancaveis_1goal(s,goal):
    csp_sokoban2 = csp_find_alcancaveis_1goal(s,goal) # <--- a vossa função csp_find_alcancaveis_1goal 
    r = backtracking_search(csp_sokoban2, order_domain_values = number_ascending_order, inference = forward_checking)    
    return {} if r == None else r

def join_dict(merged_dict,result, goal):
    for a in result.keys():
        if result[a] == 1:
            merged_dict[a].append(goal)
    return merged_dict

def find_alcancaveis_all_goals(s):
    variables = list(s.navegaveis) + list(s.proibidas)
    merged_dict = {key: [] for key in variables}
    sorted_goals = sorted(list(s.goal))
    for goal in sorted_goals:
        result = find_alcancaveis_1goal(s,goal)
        merged_dict = join_dict(merged_dict,result, goal) 
    return {} if merged_dict == None else merged_dict
