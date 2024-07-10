def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    if (len(dna1) > len(dna2)):
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count_nucleotide = 0
    
    for ch in dna:
        if nucleotide == ch:
            count_nucleotide = count_nucleotide + 1
    return count_nucleotide

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    if (dna2 in dna1):
        return True
    else:
        return False
        
                
def is_valid_sequence(dna_seq):
    '''(str) -> bool

    Return True if and only if the DNA sequence is valid (contains no characters
    other than 'A', 'T', 'G', and 'C').

    >>> is_valid_sequence('ACTGH')
    False
    >>> is_valid_sequence('TCAG')
    True
    '''
    count = 0
    for ch in dna_seq:
        if ch in 'ATGC':
            count = count
        else:
            count = count + 1
    if count > 0:
        return False
    else:
        return True
            
def insert_sequence(dna1, dna2, number):
    '''(str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA
    sequence into the first DNA sequence at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>> insert_sequence('ATGCGAT', 'GCG', 4)
    ATGCGCGGAT
    '''
    
    return dna1[:number] + dna2 + dna1[number:]

def get_complement(dna):
    '''(str) -> str

    Return the nucleotide's complement.

    >>> get_complement('A')
    T
    >>> get_complement('G')
    C
    '''

    
    for ch in dna:
        if ch == 'A':
            return 'T'
        elif ch == 'T':
            return 'A'
        elif ch == 'G':
            return 'C'
        elif ch == 'C':
            return 'G'
   
    
    
def get_complementary_sequence(dna):
    '''(str) -> str

    Return the DNA sequence that is complementary to the
    given DNA sequence.

    >>> get_complement('ATGC')
    TACG
    >>> get_complement('ATAGCG')
    TATCGC
    '''

    new_dna = ''
    for ch in dna:
        if ch == 'A':
            new_dna = new_dna + 'T'
        elif ch == 'T':
            new_dna = new_dna + 'A'
        elif ch == 'G':
            new_dna = new_dna + 'C'
        elif ch == 'C':
            new_dna = new_dna + 'G'
    return new_dna
