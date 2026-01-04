import math
from itertools import combinations

'''
Implementation for a decision tree clasificator
'''
class DecisionTree:
    def __init__(self, data_set):
        self.data = data_set
        self.set_entropy = self.entropy(self.data)
        self.attribute_values = self.generate_attribute_sets()

    def positive_count(self, data_set):
        return sum(1 for class_value, _ in data_set if class_value == 1)

    def entropy(self, data_set):
        positives = self.positive_count(data_set)
        positive_class_fraction = positives / len(data_set)
        entropy = positive_class_fraction * math.log(positive_class_fraction, 2) * (-1)
        return entropy
    
    def sum_in_information_gain(self, data_set, attribute_position, value):
        subset_with_value = self.attribute_value_subset(attribute_position, value)
        elements_with_value_count = self.positive_count(subset_with_value)
        divisor = len(subset_with_value) / len(data_set)
    
    def information_gain(self):
        pass


    def choose_best_split(self, attribute_position):
        best_gain = 0
        best_split = ()
        for value in self.attribute_values:
            current_gain = self.information_gain(attribute_position, value)
            if current_gain > best_gain:
                best_gain = current_gain
                best_split = value
        return best_split

    '''
    For a given attribute value it finds each instance of its appearance in the data_set
    '''
    def attribute_value_subset(self, attribute_position, attribute_value):
        entropy_subset = 0
        for class_value, dna in self.data_set:
            if dna[attribute_position] == attribute_value:
                entropy_subset.append((class_value, dna))
        return entropy_subset
    
    def generate_attribute_sets(self):
        values = {"A", "C", "G", "T"}
        sorted_vals = sorted(list(values))
        attribute_sets = []

        # We allow only subsets of size 1 and 2 (3 is included due to 4 - 1 = 3)
        for i in range(1, 3):
            for left_of_split in combinations(sorted_vals, i):

                right_of_split = tuple(values - set(left_of_split))
                if len(left_of_split) == len(right_of_split) and left_of_split > right_of_split:
                    continue

                attribute_sets.append((left_of_split, right_of_split))

        for L, R in attribute_sets:
            print(f"{L} vs {R}")
        
        return attribute_sets
        


class Attribute:
    def __init__(self):
        self.position = 0
        self.values = 0