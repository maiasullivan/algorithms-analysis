import random
import time
import sys

class DataGenerator:
    # Program name.
    prog_name = "DataGenerator"

    def __init__(self, start_of_range, end_of_range):
        # Start of integer range to generate values from.
        self.start_of_range = start_of_range
        # End of integer range to generate values from.
        self.end_of_range = end_of_range
        # Random generator to use.
        random.seed(time.time())

    def sample_with_replacement(self, samples_len=None):
        """
        Generate one sample or samples, using sampling with replacement.
        """
        if not samples_len: 
            sample = random.randint(self.start_of_range, self.end_of_range)
            return sample
        
        # Implemented by generating each sample independently without any consideration of previous samples
        # Each time we generate a sample, it's like drawing from the population without removing the selected item

        samples = []
        for i in range(samples_len):
            sample = random.randint(self.start_of_range, self.end_of_range)
            samples.append(sample)

        return samples

    def sample_without_replacement(self, samples_len):
        """
        Sample without replacement, using "Algorithm R" by Jeffrey Vitter, in paper "Random sampling without a reservoir".
        This algorithm has O(size of range) time complexity.

        @param samples_len Number of samples to generate.
        @throws IllegalArgumentException When samples_len is greater than the valid integer range.
        """
        population_size = self.end_of_range - self.start_of_range + 1

        if samples_len > population_size:
            raise ValueError("samples_len cannot be greater than population_size for sampling without replacement.")

        # Create an empty list to store the samples
        samples = []
        # Fill the list with initial values in the range
        for i in range(samples_len):
            samples.append(i + self.start_of_range)

        # Replace the initial values with samples. This removes them
        for j in range(samples_len, population_size):
            t = random.randint(0, j+1)
            if t < samples_len:
                samples[t] = j + self.start_of_range

        # This process ensures that each sample is selected independently
        # once a sample is selected, the corresponding initial value is overwritten with the selected sample
        # This prevents the same item from being selected more than once, effectively achieving sampling without replacement.

        return samples

    @staticmethod
    def usage():
        """
        Error Message
        """
        print(DataGenerator.prog_name + ": <start of range to sample from> <end of range to sample from> <number of values to sample> <type of sampling>")
        print("<type of sample> = {with | without}.")
        exit(1)


def main():
    # check correct number of command line arguments
    args = sys.argv[1:]
    if len(args) != 4:
        DataGenerator.usage()

    try:
        # integer range
        start_of_range = int(args[0])
        end_of_range = int(args[1])

        # number of values to sample
        samples_len = int(args[2])

        # type of sampling
        sampling_type = args[3]

        gen = DataGenerator(start_of_range, end_of_range)

        samples = []
        if sampling_type == 'with':
            samples = gen.sample_with_replacement(samples_len)
        # sampling without replacement
        elif sampling_type == "without":
            samples = gen.sample_without_replacement(samples_len)
        else:
            print(sampling_type + " is an unknown sampling type.")
            DataGenerator.usage()

        # print out samples
        print(samples)

    except Exception as e:
        print(e.getMessage())
        DataGenerator.usage()

if __name__ == "__main__":
    main()
