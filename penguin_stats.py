# penguin_stats.py
# Sadaf Sayed
# 11/23/2026
# Functions for calculating and classifying penguin statistics

# Calculate the percentage of penguins in a species.
def calculate_percentage(count, total):
    percentage = count / total * 100
    return percentage

# Classify a species based on its percentage.
def classify_species(percent):
    if percent < 25:
        return "small"
    elif percent < 40:
        return "medium"
    else:
        return "large"

# Describe the selected species' position by population size.
def get_position_description(selected_species, largest_species, smallest_species):
    if selected_species == largest_species:
        return "largest"
    elif selected_species == smallest_species:
        return "smallest"
    else:
        return "middle-sized"
