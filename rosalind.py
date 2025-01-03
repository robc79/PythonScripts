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


class NucleotideCounter:
    """ Class for counting nucleotides in a sequence. """
    def __init__(self, alphabet):
        self.alphabet = alphabet.upper()
    

    def count(self, nucleotide, sequence):
        """ Count occurrences of nucleotide in the given sequence. """
        if nucleotide not in self.alphabet:
            raise SequenceError("Nucleotide not valid for sequence.")
        return len([x for x in sequence if x == nucleotide])


class DnaSequence(GeneticSequence):
    """ Represents a DNA sequence. """
    def __init__(self, sequence):
        alphabet = "ACGT"
        super().__init__(sequence, alphabet)
        self.nucleotide_counter = NucleotideCounter(alphabet)
    

    def count_a(self):
        return self.nucleotide_counter.count('A', self.sequence)


    def count_c(self):
        return self.nucleotide_counter.count('C', self.sequence)
    

    def count_g(self):
        return self.nucleotide_counter.count('G', self.sequence)


    def count_t(self):
        return self.nucleotide_counter.count('T', self.sequence)


class RnaSequence(GeneticSequence):
    """ Represents an RNA sequence. """
    def __init__(self, sequence):
        alphabet = "ACGU"
        super().__init__(sequence, alphabet)
        self.nucleotide_counter = NucleotideCounter(alphabet)


    def count_a(self):
        return self.nucleotide_counter.count('A', self.sequence)


    def count_c(self):
        return self.nucleotide_counter.count('C', self.sequence)
    

    def count_g(self):
        return self.nucleotide_counter.count('G', self.sequence)


    def count_u(self):
        return self.nucleotide_counter.count('U', self.sequence)
