import json
import os

# get current working directory path
cwd_path = os.getcwd()



def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    #načítanie kľúčov zo súboru
    with open("sequential.json", "r") as f:
        allowed_keys = json.load(f)

    #overenie že sú správne kľúče
    if field not in allowed_keys:
        return None

    with open(file_name, "r") as f:
        data = json.load(f)

    #vrátenie hodnot
    return data.get(field)


def linear_search(sekvencia, cislo):
    positions = []
    count = 0
    idx = 0

    while idx < len(sekvencia):
        if sekvencia[idx] == cislo:
            count = count +1
            positions.append(idx)
        idx = idx + 1

    return positions, count



def main():
    #pass
    #volať funkciu read_data
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    linear_algorithm = linear_search(sequential_data, 5)
    print(linear_algorithm)


if __name__ == '__main__':
    main()