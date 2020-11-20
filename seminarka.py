import time
import os


def bit_to_mb(n):
    if isinstance(n, list or n, tuple):
        mbList = []
        for x in range(len(n)):
            tmp = n[x]
            tmp = (1023.0 ** -2) * tmp
            mbList.append(tmp)
        return mbList
    else:
        return (1023.0 ** -2) * n


def ex2(information):
    # pretvoreni tuplu do retezce pomoci specifikace
    current_year: str = time.strftime("%Y")
    output = []
    tmp = information.strip("[]")
    input = tmp.replace("}", "}|").replace(", {", "{").replace('"', "").replace('{', "").replace('}', "").split("|")
    del input[-1]
    for i in range(len(input)):
        tmp = str(input[i])
        info_arr = tmp.split(",")
        sentences = []
        for j in range(len(info_arr)):
            if info_arr[j] == "Muz":
                sentences.append("Pan ")
            elif info_arr[j] == "Zena":
                sentences.append("Paní ")
            if j == 1:
                tmp = info_arr[1].split(" ")
                sentences.append(tmp[2] + " " + tmp[1] + ", ")
            if j == 2 and info_arr[2] != " ":
                date_of_birth = int(info_arr[2])
                age = (int(current_year)) - date_of_birth
                sentences.append("ve věku " + str(age) + " let.")
            elif j == 2 and info_arr[2] == ' ':
                sentences.append("ve věku XXX let.")
            if j == 3 and info_arr[3] != " ":
                sentences.append("bytem " + info_arr[3])
            elif j == 3 and info_arr[3] == ' ':
                sentences.append("bytem neznámé, ")
        output.append(sentences)
    return output


def get_me_info(path):
    if not path:
        path = os.path.abspath(os.getcwd())

    nestedList = [["hello word", ".py", round(1.345346, 3), time.strftime("%a, %d %b %Y %H:%M:%S")],
                  ["hello word", ".java", round(2.453534, 3), time.strftime("%a, %d %b %Y %H:%M:%S")],
                  ["hello word", ".c", round(3.9686721, 3), time.strftime("%a, %d %b %Y %H:%M:%S")]
                  ]
    print('|--------------------------------- get_me_info -------------------------------------|')
    print('|-----------------------------------------------------------------------------------|')
    print('|-----------------------------------------------------------------------------------|')
    print('|       Soubor       |    Sufix    |   Velikost v MB   |     Naposledy změněno      |')
    print('|             <jmeno>|   <koncovka>|    <velikost v MB>|               <datum / čas>|')
    for item in nestedList:
        print("|", item[0], "|", item[1], "|", item[2], "|", item[3], "|")
    print('|-----------------------------------------------------------------------------------|')
    print('|-----------------------------------------------------------------------------------|')
    print('|----------------------------<{0}>----------------------------|'.format(
        time.strftime("%a, %d %b %Y %H:%M:%S")))


# print(get_me_info())

fileNames = os.listdir(os.path.abspath(os.getcwd()))
for fileName in fileNames:
    suffix = fileName.split('.', 1)
    print(type(fileName))
    #print('Suffix: ' + suffix)
