import re


class SequenceError(Exception):
    """ Indicates an error with a given sequence. """
    pass


class GeneticSequence:
    """ Base class for all genetic sequence types. """
    def __init__(self, sequence, alphabet):
        pattern = re.compile(f"^[{alphabet.upper()}]*$")
        if not pattern.match(sequence.upper()):
            raise SequenceError("Invalid characters found in sequence.")
        self.sequence = sequence.upper()
        self.alphabet = alphabet.upper()


class NucleotideSequence(GeneticSequence):
    """ Base class for all nucleotide sequences. """
    def __init__(self, sequence, alphabet):
        super().__init__(sequence, alphabet)

    
    def count(self, nucleotide):
        if nucleotide not in self.alphabet:
            raise SequenceError("Nucleotide not valid for this sequence.")
        return len([x for x in self.sequence if x == nucleotide.upper()])
        

    def percentage_gc(self):
        return (self.count('C') + self.count('G')) / len(self.sequence)
    

    def point_mutations(self, other):
        if type(other) != type(self):
            raise SequenceError("Sequences must be of the same type.")
        if len(other.sequence) != len(self.sequence):
            raise SequenceError("Sequences must be of the same length.")
        mutations = 0
        for a, b in zip(self.sequence, other.sequence):
            if a != b:
                mutations += 1
        return mutations


class DnaSequence(NucleotideSequence):
    """ Represents a DNA sequence. """
    def __init__(self, sequence):
        alphabet = "ACGT"
        super().__init__(sequence, alphabet)


    def count_a(self):
        return self.count('A')


    def count_c(self):
        return self.count('C')
    

    def count_g(self):
        return self.count('G')


    def count_t(self):
        return self.count('T')


class RnaSequence(NucleotideSequence):
    """ Represents an RNA sequence. """
    def __init__(self, sequence):
        alphabet = "ACGU"
        super().__init__(sequence, alphabet)


    def count_a(self):
        return self.count('A')


    def count_c(self):
        return self.count('C')
    

    def count_g(self):
        return self.count('G')


    def count_u(self):
        return self.count('U')
