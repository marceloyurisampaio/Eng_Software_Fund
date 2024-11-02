#Greedy Algorithm Example
def max_atv (atv): 
  #Ordenar as atividades pode horário de término de forma crescente
  atv_order = sorted(atv, key=lambda x: x[2])
  atv_selected = []

  fim_atual = 0
  
  for atv in atv_order:
    nome, inicio, fim = atv
    if inicio >= fim_atual:
      atv_selected.append(nome)
      fim_atual = fim
  return atv_selected