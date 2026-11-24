# PalmerPenguinsM11.py
# Sadaf Sayed
# 11/23/2026
# Organize Palmer Penguin analysis using custom modules.

import math
from penguin import Penguin

import penguin_stats
from penguin_stats import calculate_percentage

# constants representing the species and count
SP_CHINSTRAP = "Chinstrap"
SP_GENTOO = "Gentoo"
SP_ADELIE = "Adelie"

NUM_CHINSTRAP = 68
NUM_GENTOO = 123
NUM_ADELIE = 151

species_names = [
    SP_CHINSTRAP,
    SP_GENTOO,
    SP_ADELIE
]

species_counts = [
    NUM_CHINSTRAP,
    NUM_GENTOO,
    NUM_ADELIE
]



def display_species_statistics(names, counts, percentages):
    for index, species in enumerate(names):
        print(f"{species}: {counts[index]} ({percentages[index]:.2f}%)")

def read_penguin_row(row_number):
    penguin_row = ""

    try:
        # Open the CSV file and skip the header row
        with open("PalmerPenguins.csv", "r") as penguin_file:
            penguin_file.readline()
            current_row = 1

            # Search for the requested data row
            for row in penguin_file:
                if current_row == row_number:
                    penguin_row = row.strip()
                    break

                current_row += 1

    except FileNotFoundError:
        print("Error: PalmerPenguins.csv was not found.")

    if penguin_row == "":
        raise ValueError(
            f"Penguin observation {row_number} "
            f"could not be retrieved."
        )

    # Return the requested row as a string
    return penguin_row

def process_penguin_row(row_number):
    try:
        penguin_row = read_penguin_row(row_number)

        print("\nSample dataset row:")
        print(penguin_row)

        penguin_data = penguin_row.split(",")
        print(penguin_data)

        sample_number = int(penguin_data[0])
        species = penguin_data[1]
        bill_length = float(penguin_data[2])
        bill_depth = float(penguin_data[3])
        body_mass = int(penguin_data[5])
        sex = penguin_data[6]

        print("\nSample Penguin Observation")
        print(f"Sample Number: {sample_number}")
        print(f"Species: {species}")
        print(f"Bill length: {bill_length} mm")
        print(f"Bill depth: {bill_depth} mm")
        print(f"Body mass: {body_mass} g")
        print(f"Sex: {sex}")

    except ValueError as excpt:
        print(f"Error: {excpt}")

    except IndexError:
        print("Error: The penguin observation is incomplete.")


def main():
    total_species = len(species_names)

    # calculate totals and averages
    total_penguins = sum(species_counts)
    average_penguins = total_penguins / total_species
    average_penguins_rounded_up = math.ceil(average_penguins)

    # calculate percentages
    chinstrap_percent = penguin_stats.calculate_percentage(species_counts[0], total_penguins)
    gentoo_percent = penguin_stats.calculate_percentage(species_counts[1], total_penguins)
    adelie_percent = penguin_stats.calculate_percentage(species_counts[2], total_penguins)

    species_percentages = [
        chinstrap_percent,
        gentoo_percent,
        adelie_percent
    ]

    largest_count = max(species_counts)
    smallest_count = min(species_counts)

    largest_index = species_counts.index(largest_count)
    smallest_index = species_counts.index(smallest_count)

    largest_species = species_names[largest_index]
    smallest_species = species_names[smallest_index]

    # output the species names with introductory text

    print("*** introducing the Palmer Penguins:")
    print("\t" + species_names[0] + "!")
    print("\t\t" + species_names[1] + "!")
    print("and last but not least...")
    print("\t" + species_names[2] + "!")
    print()

    print(f"There are a total of {total_species} penguin species in this datset.")
    print(f"There are a total of {total_penguins} penguins in the dataset.")
    print(f"The average number of penguins per species is {average_penguins:.1f}.")
    print(f"The average rounded up is {average_penguins_rounded_up} penguins.")
    print()

    # display species statistics using a loop
    display_species_statistics(species_names, \
                               species_counts, species_percentages)
    print("\nModule Import Demonstration")
    percentage = calculate_percentage(
        species_counts[0], total_penguins)
    print(f"Chinstrap percentage: {percentage:.2f}%")

    print("\nCustom Module Location")
    print(penguin_stats.__file__)

    print(f"The species with the most obsevations is {largest_species} with {largest_count} penguins.")
    print(f"The species with the fewest observations is {smallest_species} with {smallest_count} penguins.")

    # Process two penguin observations
    process_penguin_row(1)
    process_penguin_row(153)

    # Demonstrate exception handling
    print("\nException Handling Demonstration")
    process_penguin_row(999)
    # Module 8: Lists and body mass statistics
    sample_rows = [1, 2, 3, 4, 5]
    body_masses = []
    penguin_objects = []

    for row_number in sample_rows:
        penguin_row = read_penguin_row(row_number)
        penguin_data = penguin_row.strip().split(",")

        sample_number = int(penguin_data[0])
        species = penguin_data[1]
        body_mass = int(penguin_data[5])

        body_masses.append(body_mass)
        penguin_objects.append(
            Penguin(sample_number, species, body_mass)
        )

    print("\nSample Body Masses")
    print(body_masses)

    print("\nBody Mass Summary")
    print(f"Observations: {len(body_masses)}")
    print(f"Total body mass: {sum(body_masses)} g")
    print(f"Smallest body mass: {min(body_masses)} g")
    print(f"Largest body mass: {max(body_masses)} g")
    print(f"Average body mass: {sum(body_masses)/len(body_masses):.2f} g")

    species_dictionary = {
    SP_CHINSTRAP: NUM_CHINSTRAP,
    SP_GENTOO: NUM_GENTOO,
    SP_ADELIE: NUM_ADELIE
    }

    print("\nSpecies Counts Using a Dictionary")
    for species_name in species_dictionary:
        print(f"{species_name}: {species_dictionary[species_name]}")

    # Module 9: Penguin objects
    print("\nPenguin Object Demonstration")
    penguin_objects[0].display_info()

    print("\nPenguin Objects")
    for penguin in penguin_objects:
        penguin.display_info()

    total_object_mass = 0
    for penguin in penguin_objects:
        total_object_mass += penguin.body_mass

    average_object_mass = total_object_mass / len(penguin_objects)

    print("\nObject-Based Body Mass Summary")
    print(f"Observations: {len(penguin_objects)}")
    print(f"Total body mass: {total_object_mass} g")
    print(f"Average body mass: {average_object_mass:.2f} g")


    print()
    # initialize the valid selection counter
    valid_selections = 0
    print("Explore the Palmer Penguins")
    print("Enter Chinstrap, Gentoo, Adelie, Sample, or Done.")
    species_choice = input("Enter a species: ")
    # repeatedly prompt the user to explore species
    while species_choice != "Done":
        if species_choice == "Sample":
            try:
              sample_number = int(input("Enter a sample number: "))
              process_penguin_row(sample_number)
            except ValueError:
                print("Error: Please enter a valid integer sample number.")
            finally:
                print("Sample request completed.")

        elif species_choice not in species_names:
            print(f"{species_choice} is not one of the species in this dataset.")
        else:
            if species_choice == species_names[0]:
                selected_index = 0
            elif species_choice == species_names[1]:
                selected_index = 1
            else:
                selected_index = 2

            selected_species = species_names[selected_index]
            selected_count = species_counts[selected_index]
            selected_percent = species_percentages[selected_index]

            size_category = penguin_stats.classify_species(selected_percent)

            position_description = \
                penguin_stats.get_position_description(selected_species, largest_species, smallest_species)

            average_position = "above" if selected_count > average_penguins else "below"

              # update the number of valid selections
            valid_selections += 1
            print(f"Species: {selected_species}")
            print(f"Count: {selected_count}")
            print(f"Percentage: {selected_percent:.2f}%")
            print(f"Size category: {size_category}")
            print(f"Position: {position_description}")
            print(f"Compared to average: {average_position}")

              # ask the user to choose another species
        species_choice = input("Enter another species: ")

    print()
    print("Exploration Summary")
    print(f"You explored {valid_selections} valid penguin species.")


if __name__ == "__main__":
    main()

