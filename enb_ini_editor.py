import os

# Receive a filepath and return a list of each line in the file
def list_file_lines(filepath):
    with open(filepath) as file_object:
        lines = file_object.readlines()
    cleaned_lines = []
    # BONNIE RECOMMENDATION
    #cleaned_lines = [line.rstrip("\n") for line in lines if line != "\n"]
    for line in lines:
        if line != "\n":
            cleaned_lines.append(line.rstrip("\n"))
    return cleaned_lines

# Build a list of [SECTIONS] from a list of each line in a file
def list_sections(file_lines):
    sections = []
    for line in file_lines:
        if line[0] == "[":
            sections.append(line)
    return sections

# Build a list of dictionaries for each of the [SECTIONS] from a list of each line in a file
def build_value_dicts(file_lines):
    dicts = [ ]
    first_section = True
    for line in file_lines:
        if line[0] == "[":
            if first_section == False:
                dicts.append(dict)
                dict = { }
            else:
                first_section = False
                dict = { }
        else:
            key = ""
            value = ""
            reading_key = True
            for character in line:
                if character != "=":
                    if reading_key == True:
                        key = key + character
                    else:
                        value = value + character
                else:
                    reading_key = False
            dict[key] = value
    dicts.append(dict)
    return dicts

# Directories & multiplier filepath
original_inis_directory = "/home/matthew/Games/Skyrim/enbseries/original_inis/"
directory_game_inis = "/home/matthew/Games/Skyrim/enbseries/"
multiplier_ini_filepath = "/home/matthew/Games/Skyrim/enbseries/multiplier.ini"

# Establish test variable

# Begin program logic...
print("Starting Tweak Tool for Rudy's ENB...\n")

# Build multiplier file sections list and value dictionaries
print("Reading value multipliers..")

multiplier_file_lines = list_file_lines(multiplier_ini_filepath)
multiplier_sections = list_sections(multiplier_file_lines)

print("Detected configurtion sections: ", end="")
for section in multiplier_sections:
    print(section + " ", end="")
print("\n", end="")
    
multiplier_dictionaries = build_value_dicts(multiplier_file_lines)

for step in range(len(multiplier_sections)):
    print(multiplier_sections[step] + " is:")
    print(multiplier_dictionaries[step])
print("\n", end="")
    
# Generate a list of all ini files to adjust
ini_filenames = os.listdir(path=original_inis_directory)                
                    
print("The following ini files will be adjsuted:")
for ini_filename in ini_filenames:
    print("\t" + ini_filename)
print("\n", end="")

# Build original ini dictionaries of file lines, sections lists and value dictionaries
print("Reading original inis...\n")

original_ini_file_lines = {}
original_ini_sections = {}
original_ini_values = {}

for ini_filename in ini_filenames:
    print("Reading " +  ini_filename)
        
    print("Reading file lines...")
    original_ini_file_lines[ini_filename] = list_file_lines(original_inis_directory + ini_filename)
    
    print("Reading sections...")
    original_ini_sections[ini_filename] = list_sections(original_ini_file_lines[ini_filename])
    print("Sections found: ", end="")
    for section in original_ini_sections[ini_filename]:
        print(section, end="")
        print(" ", end="")
    print("\n", end="")
    
    print("Reading values...")
    original_ini_values[ini_filename] = build_value_dicts(original_ini_file_lines[ini_filename])
    print("Completed reading file\n")

print("Sample file: " + ini_filenames[45])
print("Sample file lines:")
print(original_ini_file_lines[ini_filenames[45]])
print("Sample file sections:")
print(original_ini_sections[ini_filenames[45]])
print("Sample file values:")
print(original_ini_values[ini_filenames[45]])

# Curren testing
print("\n\t---\n\tCurrent testing\n\t---\n")

test_file_sections = original_ini_sections[ini_filenames[45]]

print("Test file...\nObtained ini sections: ", end="")
print(original_ini_sections[ini_filenames[45]])
print("Steps: ", end="")
print(len(original_ini_sections[ini_filenames[45]]))
print("Step #3: ", end="")
print(original_ini_sections[ini_filenames[45]][3])
print("Sections I want to modify: ", end="")
print(multiplier_sections)
print("")

for ini_filename in ini_filenames:
    print("Processing " + ini_filename + "...")
    sections = original_ini_sections[ini_filename]
    for multiplier_index, multiplier_section in enumerate(multiplier_sections):
        print("Searching for " + multiplier_section + "... ", end="")
        for index, section in enumerate(sections):
            if multiplier_section == section:
                print("Found " + multiplier_section + " at " + str(index) + "!")
                print("Value dictionary: ", end="")
                values = original_ini_values[ini_filename][index]
                print(values)
                print("Multiplier dictionary: ", end="")
                print(multiplier_dictionaries[multiplier_index])
    print("")



