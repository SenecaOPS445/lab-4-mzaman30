#!/usr/bin/env python3

# Function to join sets (Union operation)
def join_sets(s1, s2):
    # Return a set that contains every value from both s1 and s2 (union)
    return s1 | s2  # This is the same as s1.union(s2)

# Function to match sets (Intersection operation)
def match_sets(s1, s2):
    # Return a set that contains all values found in both s1 and s2 (intersection)
    return s1 & s2  # This is the same as s1.intersection(s2)

# Function to find different sets (Symmetric Difference)
def diff_sets(s1, s2):
    # Return a set that contains all different values not shared between s1 and s2
    return s1 ^ s2  # This is the same as s1.symmetric_difference(s2)

if __name__ == '__main__':
    # Example sets
    set1 = set(range(1, 10))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
    set2 = set(range(5, 15))  # {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

    # Print the sets
    print('set1:', set1)
    print('set2:', set2)

    # Print the results of the three operations
    print('join: ', join_sets(set1, set2))  # Union of set1 and set2
    print('match: ', match_sets(set1, set2))  # Intersection of set1 and set2
    print('diff: ', diff_sets(set1, set2))  # Symmetric Difference between set1 and set2
