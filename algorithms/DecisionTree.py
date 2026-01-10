import math
from itertools import combinations
from algorithms.Node import Node

'''
Implementation for a decision tree clasificator
'''
class DecisionTree:
    def __init__(self, data_set, max_depth=5):
        self.data = data_set
        self.max_depth = max_depth
        self.set_entropy = self.entropy(self.data)
        self.possible_splits = self.generate_attribute_sets()
        self.root = None

    def train(self):
        self.root = self.decision_tree_id3_mod(self.data, depth=0)
        return self.root
    
    def get_positive_count(self, data_set):
        return sum(1 for class_value, _ in data_set if class_value == 1)

    def get_majority_class(self, data_set):
        positives = self.get_positive_count(data_set)
        return 1 if positives >= len(data_set) / 2 else 0

    def entropy(self, data_set):
        if not data_set: return 0
        positives = self.get_positive_count(data_set)
        pc_frac = positives / len(data_set)
        if pc_frac == 0 or pc_frac == 1: return 0
        return (pc_frac * math.log(pc_frac, 2) + (1 - pc_frac) * math.log(1 - pc_frac, 2)) * (-1) 
    
    def information_gain(self, parent, left, right):
        total_S = len(parent)
        if total_S == 0: return 0

        w_left = len(left) / total_S
        w_right = len(right) / total_S
        inf_gain = self.entropy(parent) - (w_left * self.entropy(left)) + (w_right * self.entropy(right))
        
        return inf_gain

    '''
    For a given attribute it chooses 
    '''
    def choose_best_split(self, data):
        best_gain = -1
        best_split = None
        dna_length = len(data[0][1])
        for i in range(dna_length):
            for split in self.possible_splits:
                left_subset, right_subset = self.split_data(data, i, split)
                current_gain = self.information_gain(data, left_subset, right_subset)
                if current_gain > best_gain:
                    best_gain = current_gain
                    best_split = (i, split, left_subset, right_subset)
        return best_gain, best_split

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
    
    def split_data(self, data, attribute_position, group):
        left, right = [], []
        for class_value, dna in data:
            if dna[attribute_position] in group:
                left.append((class_value, dna))
            else:
                right.append((class_value, dna))
        return left, right
    
    def decision_tree_id3_mod(self, data, depth):

        # STOP CONDITIONS
        if not data:
            return Node(class_value=0)
        
        # 2. Czysty węzeł (wszystkie przykłady tej samej klasy)
        first_class = data[0][0]
        if all(row[0] == first_class for row in data):
            return Node(class_value=first_class)

        # 3. Osiągnięto maksymalną głębokość
        if depth >= self.max_depth:
            return Node(class_value=self.get_majority_class(data))
        
        # BEST SPLIT CHOICE
        best_gain, split_details = self.choose_best_split(data)
        
        if best_gain <= 0:
            return Node(class_value=self.get_majority_class(data))
        
        attr_pos, group, left_data, right_data = split_details

        left_node = self.decision_tree_id3_mod(left_data, depth + 1)
        right_node = self.decision_tree_id3_mod(right_data, depth + 1)

        return Node(
            attribute_pos=attr_pos,
            split_condition_group=group,
            left_node=left_node,
            right_node=right_node
        )
    
