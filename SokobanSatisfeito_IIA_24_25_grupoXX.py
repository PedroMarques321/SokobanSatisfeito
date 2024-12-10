
# Para implementarem a vossa função **`csp_possivel_solucao`**, devem formular o problema como um CSP. 
# A função recebe como input exatamente o mesmo que a função `possivel_solucao` e deve retornar como output uma instância de um problema CSP. 
# Notem que o problema pode ser visto como um problema de coloração de mapas em que:
# - As células são as variáveis (as regiões num mapa);
# - Os domínios são dados pela lista de goals alcançáveis pelas respectivas células (as cores para colorir o mapa);
# - Duas células são vizinhas se partilharem algum dos goals (se forem regiões contíguas);
# - Duas células vizinhas não podem ter o mesmo valor (duas regiões contíguas não podem ter a mesma cor).
# Lembrem-se que ambos os inputs são dados, i.e., as caixas e a atribuição de células a listas de goals (os goals alcançáveis).
def csp_possivel_solucao(caixas, goals_alcancaveis):
    pass


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
    pass

# função que chama a função `find_alcancaveis_1goal` 
# tantas vezes quantas o número de goals do puzzle. 
# Recebe uma instância do problema Sokoban e devolve a variável `alcancaveis` 
# que é construída a partir dos resultados das várias chamadas.
def find_alcancaveis_all_goals(s):
    sorted_goals = sorted(list(s.goal))
    pass # o vosso código aqui
    return result_alcancaveis