

def poisk(search_word):
    with open("Databaze.csv", "r") as file:
        for line in file:
            if search_word in line:
                 modified_string = line.replace(",", " ")
                 return modified_string
                # print(line)
            


def poisk2(search_word):
    with open("Databaze.csv", "r") as file:
        i = 0
        for line in file:
            if search_word in line:
                #  modified_string = line.replace(",", " ")
                 return i
            i += 1