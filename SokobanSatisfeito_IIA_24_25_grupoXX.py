
# Para implementarem a vossa função **`csp_possivel_solucao`**, devem formular o problema como um CSP. 
# A função recebe como input exatamente o mesmo que a função `possivel_solucao` e deve retornar como output uma instância de um problema CSP. 
# Notem que o problema pode ser visto como um problema de coloração de mapas em que:
# - As células são as variáveis (as regiões num mapa);
# - Os domínios são dados pela lista de goals alcançáveis pelas respectivas células (as cores para colorir o mapa);
# - Duas células são vizinhas se partilharem algum dos goals (se forem regiões contíguas);
# - Duas células vizinhas não podem ter o mesmo valor (duas regiões contíguas não podem ter a mesma cor).
# Lembrem-se que ambos os inputs são dados, i.e., as caixas e a atribuição de células a listas de goals (os goals alcançáveis).
def csp_possivel_solucao(caixas, goals_alcancaveis):

    # Variáveis são as coordenadas das caixas
    variaveis = list(caixas)
    
    # Domínios são os goals alcançáveis para a posição de cada caixa
    dominios = {}
    for caixa in variaveis:
        dominios[caixa] = goals_alcancaveis[caixa]
        
    # Encontrar vizinhos - células que têm goals em comum
    neighbors = {}
    for caixa1 in variaveis:
        neighbors[caixa1] = []
        goals1 = goals_alcancaveis[caixa1]
        for caixa2 in variaveis:
            if caixa1 != caixa2:
                goals2 = goals_alcancaveis[caixa2]
                # Verificar se têm algum goal em comum
                if any(goal in goals1 for goal in goals2):
                    neighbors[caixa1].append(caixa2)
    
    # Função de restrição
    def constraint(A, a, B, b):
        """Retorna True se as caixas A e B podem ser atribuídas aos goals a e b respectivamente"""
        # Duas caixas não podem ter o mesmo goal
        return a != b
    
    return CSP(variaveis, dominios, neighbors, constraint)


# Para implementarem a função **`csp_find_alcancaveis_1goal`** devem formular o problema como um CSP em que:

# - As células são as variáveis;
# - Os domínios são a possibilidade (1) ou não (0) de uma caixa partir da célula e chegar ao goal;
# - Duas células são vizinhas se forem adjacentes (na vertical ou horizontal) e se for possível empurrar uma caixa de uma para a outra, num dos sentidos ou nos dois. Se forem adjacentes, mas nenhuma caixa pode ser empurrada de uma para a outra, então não são vizinhas.
# - As restrições, tantos as unárias como as binárias, ficam por vossa conta!

# Reparem que este CSP pode devolver soluções que, apesar de válidas no contexto do problema, 
# não ajudam o Sokoban tanto como outras. 
# Por exemplo, se duas soluções válidas tiverem como única diferença o valor atribuído a uma das células 
# (0 num caso, 1 no outro), a solução que mais ajuda o Sokoban é aquela que tem o 0, 
# pois permite-lhe mais facilmente detetar um *deadlock*. 
# É por isso que a função `find_alcancaveis_1goal` faz sempre a procura com `order_domain_values = number_ascending_order`, 
# como especificado acima.
def csp_find_alcancaveis_1goal(s, goal):
    # Buscar todas as células navegáveis e proibidas como variáveis
    variaveis = sorted(list(s.navegaveis.union(s.proibidas)))
    
    # Inicializar domínios - todas as células podem potencialmente alcançar (1) ou não alcançar (0) o goal
    dominios = {}
    for var in variaveis:
        if var in s.calc_traps():  # Se a célula for uma trap, não chega ao goal
            dominios[var] = [0]
        else:
            dominios[var] = [0, 1]
    
    # Definir o domínio do goal como [1] pois deve ser alcançável
    dominios[goal] = [1]

    # Encontrar vizinhos - células adjacentes onde as caixas podem ser empurradas
    neighbors = {}
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    
    for cell in variaveis:
        neighbors[cell] = []
        for dx, dy in moves:
            next_cell = (cell[0] + dx, cell[1] + dy)
            push_cell = (cell[0] - dx, cell[1] - dy)  # Célula necessária para empurrar
            
            # Verificar se o movimento é válido:
            # 1. Próxima célula existe e é navegável
            # 2. Célula necessária para empurrar existe e é navegável (necessária para o Sokoban empurrar)
            # 3. Próxima célula não é uma trap
            if (next_cell in variaveis and 
                push_cell in variaveis and 
                next_cell not in s.calc_traps()):
                neighbors[cell].append(next_cell)
    
    # Remover vizinhos para células que não podem ter vizinhos
    # Remove neighbors for cells that can't have neighbors
    no_neighbors = [cell for cell in variaveis if not neighbors[cell]]
    for cell in no_neighbors:
        dominios[cell] = [0]  # Can't reach goal if no valid neighbors
        for other_cell in neighbors:
            if cell in neighbors[other_cell]:
                neighbors[other_cell].remove(cell)
    
    def constraint(A, a, B, b):
        """
        Função de restrição:
        - Se ambas as células não podem alcançar o goal (0,0), não tem problema
        - Se as células têm valores diferentes (0,1 ou 1,0), não tem problema
        - Se ambas as células podem alcançar o goal (1,1), elas devem ser adjacentes
        """
        if a == 0 and b == 0:
            return True
        if a != b:
            return True
        if a == 1 and b == 1:
            # Verificar se as células são adjacentes
            return abs(A[0] - B[0]) + abs(A[1] - B[1]) == 1
        return True
    
    return CSP(variaveis, dominios, neighbors, constraint)

# função que chama a função `find_alcancaveis_1goal` 
# tantas vezes quantas o número de goals do puzzle. 
# Recebe uma instância do problema Sokoban e devolve a variável `alcancaveis` 
# que é construída a partir dos resultados das várias chamadas.
def find_alcancaveis_all_goals(s):
    sorted_goals = sorted(list(s.goal))
    pass # o vosso código aqui
    return result_alcancaveis

