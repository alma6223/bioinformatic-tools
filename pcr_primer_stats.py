class Pcr_primer_stats:
    def __init__(self, fasta):
        """
        :param fasta: 'fasta' file with the nucleotide primer sequence.
        """
        self.fasta = fasta

    def get_primer_sequence(self):
        """
        :return: returns the nucleotide primer sequence of a 'fasta' file.
        """
        with open(self.fasta, 'r') as seq:
            primer_sequence = seq.read().upper()
        return primer_sequence

    def get_sequence_length(self):
        """
        :return: returns the length of the nucleotide primer sequence.
        """
        return len(self.get_primer_sequence())

    def get_base_counts(self):
        """
        :return: returns the number of guanine (G), adenine (A), thymine (T) and cytosine (C) in the nucleotide primer sequence.
        """
        G, A, T, C = 0, 0, 0, 0
        for i in self.get_primer_sequence():
            if i == 'G':
                G += 1
            if i == 'A':
                A += 1
            if i == 'T':
                T += 1
            if i == 'C':
                C += 1
        return G, A, T, C

    def get_gc_content(self):
        """
        :return: returns the percentage of guanine (G) and cytosine (C) in the nucleotide primer sequence.
        """
        G, A, T, C = self.get_base_counts()
        return (G + C) / self.get_sequence_length() * 100

    def get_tm(self):
        """
        :return: returns the melting temperature of the nucleotide primer sequence.
        """
        G, A, T, C = self.get_base_counts()
        return 2 * (A + T) + 4 * (G + C)
