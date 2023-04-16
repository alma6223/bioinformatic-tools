class Range_extractor_dna:
    def __init__(self, fasta):
        """
        :param fasta: 'fasta' file with the nucleotide sequence to extract.
        """
        self.fasta = fasta

    def get_sequence(self):
        """
        :return: returns the nucleotide sequence of a 'fasta' file.
        """
        with open(self.fasta, 'r') as seq:
            sequence = seq.read().upper()
        return sequence

    def range_extractor_dna(self, start, end):
        """
        :param start: start range position.
        :param end: end range position.
        :return: returns the extracted nucleotide sequence.
        """
        return self.get_sequence()[start:end]