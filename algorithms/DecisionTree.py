import math

'''
Implementation for a decision tree clasificator
'''
class DecisionTree:
    def __init__(self, data_set):
        self.data = data_set
        self.set_entropy = self.entropy(self.data)
        self.attribute_values = self.generate_attribute_sets()

    def entropy(self, data_set):
        positives = sum(1 for class_value, _ in data_set if class_value == 1)
        positive_class_fraction = positives / len(data_set)
        entropy = positive_class_fraction * math.log(positive_class_fraction, 2) * (-1)
        return entropy
    
    def information_gain(self, attribute_position):
        entropy_subset = 0
        for value in self.attribute_values:
            self.attribute_value_count(attribute_position, value)

        #information_gain = self.set_entropy - 

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


class Attribute:
    def __init__(self):
        self.position = 0
        self.values = 0