# https://www.codewars.com/kata/complementary-dna/train/python

test_dna = "ATTGC"
dna = test_dna


def DNA_strand(dna):
    # словарь комплиментарности

    my_other_dict = {"A" : "T", "T":"A", "G": "C", "C": "G"}

    list_chars = list(dna)
    print(list_chars)

    new_list_dna = []

    for element in list_chars:
        new_list_dna.append(my_other_dict[element])

    print(new_list_dna)
    new_dna = ''.join(new_list_dna)
    return new_dna


DNA_strand(dna)