class Reverse_complement:
    def __init__(self, fasta):
        """
        :param fasta: fasta: 'fasta' file with the nucleotide sequence to convert.
        """
        self.fasta = fasta

    def get_sequence(self):
        """
        :return: returns the nucleotide sequence of a 'fasta' file.
        """
        with open(self.fasta, 'r') as seq:
            sequence = seq.read().upper()
        return sequence

    def get_reverse(self):
        """
        :return: returns the 3' 5' directionality nucleotide sequence.
        """
        return self.get_sequence()[::-1]

    def get_complement(self):
        """
        :return: returns the complementary sequence of nucleotides.
        """
        complement = ''
        for i in self.get_sequence():
            if i == 'A':
                complement += 'T'
            elif i == 'T':
                complement += 'A'
            elif i == 'C':
                complement += 'G'
            elif i == 'G':
                complement += 'C'
        return complement

    def get_reverse_complement(self):
        """
        :return: returns the reverse sequence of the complementary sequence of nucleotides.
        """
        return self.get_complement()[::-1]
