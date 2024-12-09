def actionss(state):
    sokoban=state['sokoban']
    caixas=state['sokoban']
    if self.csp_possivel_solucao(caixas,self.alcancaveis) == None:
        return []
    else:
        return [action for action in self.dict_actions if self.possible(sokoban,caixas,self.dict_actions[action])]

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

"""
# constraints         
def constraints(A,a,B,b):
    
    print("A:")
    print(A)
    print("a:")
    print(a)
    print("B:")
    print(B)
    print("b:")
    print(b)
    print("------------")
    if b == 0 and a == 0:
        return False
    else:
        return True
    """

def constraints(A, a, B, b):
    """
    Função de restrição para o CSP:
    - A e B são células, e a, b são os valores binários (0 ou 1) representando
      se uma caixa pode alcançar o objetivo a partir dessa célula.
    - Se uma caixa pode alcançar o objetivo a partir de A, ela deve ser capaz de
      se mover para células vizinhas de forma consistente, respeitando as regras do jogo.
    """
    if a == 0 and b == 0:
        return True

    if a != b:
        return True

    if a == 1 and b == 1:
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        ax, ay = A
        bx, by = B

        for delta in deltas:
            if (ax + delta[0], ay + delta[1]) == B or (bx + delta[0], by + delta[1]) == A:
                return True

        return False

    return True
   
def csp_find_alcancaveis_1goal(s, goal):
    """
    Função para resolver o problema CSP com base no mapa Sokoban, considerando
    as variáveis, domínio, vizinhos e restrições.
    """
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
    
    for g in goal:
        dominio[g] = [1]

    print(f"Domínio: {dominio}")
    print(f"Vizinhos: {neighbours}")
    
    # Criação do CSP
    return CSP(variables, dominio, neighbours, constraints)   
 
"""
def csp_find_alcancaveis_1goal(s, goal):

    variables = list(s.navegaveis)+ list(s.proibidas)
    variables = sorted(set(variables), key=lambda x: (x[0], x[1]))
    buffer = []
    neighbours = {}
    dominio = {}
    traps = {}
    no_neighbours = []
    dict_actions = [(-1,0), (0,-1), (0,1),(1,0)]
    
    dominio
    for x in variables:
        if x in s.calc_traps():
            dominio[x] = [0]
            traps[x] = 0
    print(dominio.keys())        
    for x in variables:
        if not (x in s.calc_traps()):
            dominio[x] = [0,1]
        
            for y in dict_actions:
                if ((x[0]+y[0], x[1]+y[1]) in variables) and ((x[0]-y[0], x[1]-y[1]) in variables) and (not((x[0]+y[0], x[1]+y[1]) in traps.keys())):
                    buffer.append((x[0]+y[0], x[1]+y[1]))
            if not buffer:
                no_neighbours.append(x)
                neighbours[x] = []
            else:
                neighbours[x] = buffer
            buffer = []
        else:
            dominio[x] = [0]
    
    for i in no_neighbours:
        dominio[i] = [0]
        for k in neighbours.keys():
            if i in neighbours[k]:
                neighbours[k].remove(i)
    
    for goal in s.goal:
        dominio[goal] = [1]
    
    print(dominio)
    print(neighbours)
    return CSP(variables, dominio, neighbours, constraints)
"""
def possivel_solucao(caixas,goals_alcancaveis):
    csp_sokoban1 = csp_possivel_solucao(caixas,goals_alcancaveis) # <--- a vossa função csp_possivel_solucao 
    r = backtracking_search(csp_sokoban1, inference = forward_checking)
    return r
    
def find_alcancaveis_1goal(s,goal):
    csp_sokoban2 = csp_find_alcancaveis_1goal(s,goal) # <--- a vossa função csp_find_alcancaveis_1goal 
    r = backtracking_search(csp_sokoban2, order_domain_values = number_ascending_order, inference = forward_checking)    
    return {} if r == None else r
