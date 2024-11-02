#Bubble sort -> O(N^2)
def bubble_sort(arr):
    n = len(arr)
    # Loop para acessar todos os elementos do array
    for i in range(n):
        # Loop para comparar os elementos adjacentes
        for j in range(0, n - i - 1):
            # Troca se o elemento encontrado for maior que o próximo
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Array ordenado Bubble:", arr)

###################################################################################################################################################
#Selection Sort e Insertion Sort -> O(n^2)
def selection_sort(arr):
    n = len(arr)
    #Marcando a posição que será adicionado o menor elemento do subarray
    for i in range (n):
        min_index = i
        #Encontrando o menor elemento do subarray
        for j in range(i+1,n): 
            #Encontrou um menor, marcar ele como o menor
            if arr[j] < arr[min_index]:
                min_index = j
        #Fazer a troca do menor com o marcado
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
    
#Exemplo
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Array ordenado Selection:", arr) 

#####################################################################################################################################################
def insertion_sort(arr):
    n = len(arr)
    # Começa com o segundo elemento, pois o primeiro já é considerado ordenado
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elementos maiores que a chave uma posição à frente
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Coloca a chave na posição correta
        arr[j + 1] = key

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11]
insertion_sort(arr)
print("Array ordenado Insertion Sort:", arr)

###################################################################################################################################################
def merge (arr, left_half, right_half):
    i = j = k = 0
    #Unindo de modo ordenado 
    while i < len(left_half) and j < len(right_half): 
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i+=1
        else: 
            arr[k] = right_half[j]
            j+=1
        k+=1

    #Garantindo que não sobrou mais nenhum elemento em nenhuma das duas metades
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        #Chamando a função recursivamente para cada metade do array
        merge_sort(left_half)
        merge_sort(right_half)

        #Função que une as duas metades garantindo que o resultado final estará ordenado
        arr = merge(arr, left_half, right_half) 
        
    return arr
    
#Exemplo
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print("Array ordenado Merge:", arr) 

####################################################################################################################################################
def quick_sort(arr):
    #Caso base: Um array com nenhum ou somente um elemento ja esta ordenado
    if len(arr) <= 1:
        return arr

    #Escolhe um pivo. Normalmente se pega o ultimo elemento.
    pivot = arr[-1]
    left = [] #Array de elementos menores do que o pivo
    right = [] #Array de elementos maiores do que o pivo
    for i in range(len(arr) - 1): 
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    #Chama recursivamente a função para cada parte do array
    return quick_sort(left) + [pivot] + quick_sort(right)
    
#Exemplo
arr = [64, 34, 25, 12, 22, 11, 90]
arr = quick_sort(arr)
print("Array ordenado Quick:", arr) 

#####################################################################################################################################################
def heapify(arr, n, i):
    largest = i         # Inicializa o maior como o nó atual
    left = 2 * i + 1    # Índice do filho à esquerda
    right = 2 * i + 2   # Índice do filho à direita

    # Verifica se o filho à esquerda é maior que o nó atual
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Verifica se o filho à direita é maior que o nó maior atual
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Se o maior não for o nó atual, troca e continua heapificando
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Constrói o heap (rearranja o array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai os elementos do heap um a um
    for i in range(n - 1, 0, -1):
        # Move a raiz (maior elemento) para o final do array
        arr[i], arr[0] = arr[0], arr[i]
        # Chama heapify na raiz para o heap reduzido
        heapify(arr, i, 0)

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)
print("Array ordenado Heap Sort:", arr) 