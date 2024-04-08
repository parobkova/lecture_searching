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



def main():
    #pass
    #volať funkciu reaA_data
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)


if __name__ == '__main__':
    main()