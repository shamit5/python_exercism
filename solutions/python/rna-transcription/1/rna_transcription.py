def to_rna(dna_strand):
    """Translate a DNA strand into its corresponding RNA                   complement."""
    
   # ans = ""
   # for dna in dna_strand :
   #     if dna == 'G':
   #           ans = ans + 'C'
           
   #     elif dna == 'C':
   #           ans = ans + 'G'
           
   #     elif dna == 'T':
   #           ans = ans + 'A'
           
   #     else:
   #         ans = ans + 'U'
  
   # return ans    
    complements = {"G": "C", "C": "G", "T": "A", "A": "U"}

    lists = [complements[dna] for dna in dna_strand]

    return "".join(lists)