# ----------------
# Fonctions d'aide
# ----------------
def swap(tab, i, j):
    """Échange la place de deux éléments dans un tableau"""
    tab[i],tab[j] = tab[j],tab[i]


# ---------------
# Tris classiques
# ---------------
def bubble_sort(A):
    """Trie le tableau en déplaçant les plus grosses valeurs vers la fin du
    tableau, un peu comme des bulles dans l'eau qui remonteraient à la
    surface"""
    for i in range(len(A),1,-1):
        for j in range(0, i-1):
            if A[j+1] < A[j]:
                swap(A, j+1, j)

###############################################################################################                

def insertion_sort(A):
    """Trie le tableau en plaçant l'élément courant à la bonne place dans
    le sous-tableau déjà trié"""
    for i in range(1, len(A)):
        x = A[i]
        j = i
        
        while (j > 0) & (A[j - 1] > x):
            A[j] = A[j - 1]
            j = j - 1
        
        A[j] = x

####################################################################################################

def selection_sort(A):
    """Trie le tableau en cherchant le plus petit élément à mettre dans la
    première case, puis le second plus petit à mettre dans la seconde case,
    etc"""
    for i in range(0, len(A) - 1):
        small = i
        for j in range(i + 1, len(A)):
            if A[j] < A[small]:
                small = j
        if small != i:
            swap(A, i, small)

#############################################################################################
# --------------
# Tris récursifs
# --------------
def merge_sort(tab):
    """Trie le tableau via le principe de « diviser pour mieux régner »
    avec l'intelligence du tri qui se trouve au moment de la fusion"""
    def merge(tab, start, mid, end):

        i = start
        j = mid + 1
        temp = [0]*(end - start + 1)
        k = 0

        while (i <= mid) and (j <= end):
            if tab[i] <= tab[j]:
                temp[k] = tab[i]
                i += 1
            else:
                temp[k] = tab[j]
                j += 1
            k += 1

        while i <= mid:
                temp[k] = tab[i]
                i += 1
                k += 1
        while j <= end:
                temp[k] = tab[j]
                j += 1
                k += 1
        for k in range(start, end + 1):
                tab[k] = temp[k - start]
            
    def merge_sort_r(tab, start, end):


        # P =  end - start

        if start < (end):
            mid = (start+end) // 2
            # print(int(start),int(end),mid)
            # print(tab[start:end])
            merge_sort_r(tab, start, mid)
            merge_sort_r(tab, mid + 1, end)        
            merge(tab, start, mid, end)
        
    
    merge_sort_r(tab, 0, len(tab) - 1)

#######################################################################################

def quick_sort(tab):
    """Divise le tableau en deux, trie chacune des sous-parties et fusionne
    intelligemment les deux sous-parties triées"""
    def partition(tab, first, last):
    
        pivot = tab[first]
        i = first + 1
        j = last

        while True:
            while i <= j and tab[i] <= pivot:
                i += 1
            while i <= j and tab[j] >= pivot:
                j -= 1
            if i <= j:
                tab[i], tab[j] = tab[j], tab[i]
            else:
                break

        tab[first], tab[j] = tab[j], tab[first]
        return j

    def quick_sort_r(tab, first, last):
    
        if first < last:
            pivot = partition(tab, first, last)
            quick_sort_r(tab, first, pivot - 1)
            quick_sort_r(tab, pivot + 1, last)
            
    quick_sort_r(tab, 0, len(tab)-1)
    
########################################################################################################