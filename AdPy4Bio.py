# Advanced Python for Biologists exercises

# Ch.2 : Recursion and trees

def generate_trimers():
    bases = ["A" , "T" , "G" , "C"]
    result = []
    for base1 in bases:
        for base2 in bases:
            for base3 in bases:
                result.append(base1 + base2 + base3)
    return result
#each for loop repeats four times (1 per base), so the append line is 4x4x4=64, all possible 3mers

def generate_kmers(length): #can't use nested loops like above b/c don't know how many we need
    result = [''] #starting point for each of the final sequences
    for i in range(length): #extending each element in list
        new_result = [] #temporary new list
        for kmer in result:
            for base in ["A" , "T" , "G" , "C"]:
                new_result.append(kmer + base) #extend by adding each of 4 possible bases onto end
            result = new_result #using temp list as list of sequences for next round
        return result

#same issue, but recursive coding

def generate_kmers_rec(length):
    if length == 1: #if the length is one
        return ["A" , "T" , "G" , "C"] #then the result is simply a list of the four bases
    else:
        result = []
        for seq in generate_kmers_rec(length - 1): #to get this result when the length>1, take the list of all possible sequences whose length is one less than the length you're looking for
            for base in ["A" , "T" , "G" , "C"]: #and add each of the four possible bases to it
                result.append(seq + base)
            return result

#-----

# Last Common Ancestor

tax_dict = {
'Pan troglodytes' : 'Hominoidea', 'Pongo abelii' : 'Hominoidea',
'Hominoidea' : 'Simiiformes', 'Simiiformes' : 'Haplorrhini',
'Tarsius tarsier' : 'Tarsiiformes', 'Haplorrhini' : 'Primates',
'Tarsiiformes' : 'Haplorrhini', 'Loris tardigradus' :
'Lorisidae',
'Lorisidae' : 'Strepsirrhini', 'Strepsirrhini' : 'Primates',
'Allocebus trichotis' : 'Lemuriformes', 'Lemuriformes' :
'Strepsirrhini',
'Galago alleni' : 'Lorisiformes', 'Lorisiformes' :
'Strepsirrhini',
'Galago moholi' : ' Lorisiformes'
}

new_tax_dict = {
'Primates': ['Haplorrhini', 'Strepsirrhini'],
'Tarsiiformes': ['Tarsius tarsier'],
'Haplorrhini': ['Tarsiiformes', 'Simiiformes'],
'Simiiformes': ['Hominoidea'],
'Lorisidae': ['Loris tardigradus'],
'Lemuriformes': ['Allocebus trichotis'],
'Lorisiformes': ['Galago alleni','Galago moholi'],
'Hominoidea': ['Pongo abelii', 'Pan troglodytes'],
'Strepsirrhini': ['Lorisidae', 'Lemuriformes', 'Lorisiformes']
}

def get_children_rec(taxon):
    result = [taxon]
    children = new_tax_dict.get(taxon, [])
    for child in children:
        result.extend(get_children_rec(child))
    return result

def get_ancestors_rec(taxon):
    if taxon == "Primates":
        return [taxon]
    else:
        parent = tax_dict.get(taxon)
        parent_ancestors = get_ancestors_rec(parent)
        return [parent] + parent_ancestors

def get_lca(taxon1, taxon2):
    taxon1_ancestors = [taxon1] + get_ancestors_rec(taxon1)
    for taxon in [taxon2] + get_ancestors_rec(taxon2):
        if taxon in taxon1_ancestors:
            return taxon

def get_lca_list_rec(taxa):
    print("getting lca for " + str(taxa))
    if len(taxa) == 2:
        return get_lca(taxa[0], taxa[1])
    else:
        taxon1 = taxa.pop()
        taxon2 = get_lca_list_rec(taxa)
        return get_lca(taxon1, taxon2)

#----

# Ch3 : Complex data structures

dna = 'aattggaattggaattg'
k = 4
kmer2count = {}
for start in range(len(dna) - k + 1): #iterate over each possible start position using a range
    kmer = dna[start:start + k] #extract the kmer
    current_count = kmer2count.get(kmer, 0) #look up current count for kmer from the dict
    kmer2count[kmer] = current_count + 1 #update dict value to be current + 1
print(kmer2count) #keys = kmers; values = counts


dna = 'aattggaattggaattg'
k = 4
kmer2list = {} #rather than count, build up a list of start positions for each kmer
for start in range(len(dna) - k + 1):
    kmer = dna[start:start + k]
    list_of_positions = kmer2list.get(kmer, [])
    list_of_positions.append(start)
    kmer2list[kmer] = list_of_positions
print(kmer2list) #get a dict of lists

#-----

# Distance matrix

# two parts: calculating similarity scores and creating dict to hold results

gene_sets = {
    'arsenic' : {1,2,3,4,5,6,8,12},
    'cadmium' : {2,12,6,4},
    'copper' : {7,6,10,4,8},
    'mercury' : {3,2,4,5,1}
}

similarity_scores = {}
for condition1, set1 in gene_sets.items():
    single_scores = {
        condition2 : len(set1.intersection(set2)) / len(set1.union(set2))
        for condition2, set2 in gene_sets.items()
        if condition1 != condition2
        }
    similarity_scores[condition1] = single_scores
    print(condition1, single_scores)
print(similarity_scores)

#even shorter!

similarity_scores = {
    c1: {
        c2 : len(s1.intersection(s2)) / len(s1.union(s2))
        for c2,s2 in gene_sets.items()
        if c1 != c2
        }
    for c1,s1 in gene_sets.items()
}

#-----

# Testing for monophyly

def are_closely_related(my_list, taxon1, taxon2, taxon3):
    result = False
    # does the current list match the condition?
    if (contains(my_list, taxon1)
    and contains(my_list, taxon2)
    and not contains(my_list, taxon3)):
        result = True
    # do any sublists match the condition?
    for sublist in my_list:
        if isinstance(sublist, list):
            if are_closely_related(sublist, taxon1, taxon2, taxon3):
                result = True
    return result

assert are_closely_related(tree, 'raccoon', 'dog', 'bear') == False
assert are_closely_related(tree, 'raccoon', 'bear', 'weasel') == True
assert are_closely_related(tree, 'raccoon', 'bear', 'dog') == True

# didn't run the above b/c wasn't sure of the values for my_list or the taxons

#-----

# Ch4 : Object oriented Python

