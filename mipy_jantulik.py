import time
import os


def bit_to_mb(n):
    if isinstance(n, list):  # kontrola zda input neni list nebo tuple
        mb_list = []
        for x in range(len(n)):
            tmp = n[x]
            tmp = (1024.0 ** -2) * tmp  # prevedeni konkretnich hodnot v listu/tuplu na MB
            mb_list.append(tmp)
        return mb_list
    elif isinstance(n, tuple):
        mb_tuple = ()
        tmp_list = list(mb_tuple)
        for x in range(len(n)):
            tmp = n[x]
            tmp = (1024.0 ** -2) * tmp  # prevedeni konkretnich hodnot v listu/tuplu na MB
            tmp_list.append(tmp)
        return tuple(tmp_list)
    else:
        return (1024.0 ** -2) * n  # prevedni samotne hodnoty


def ex2(information):
    current_year: str = time.strftime("%Y")  # zjisteni roku
    output = []
    tmp = information.strip("[]")  # zbaveni se hranatych zavorek
    input = tmp.replace("}", "}|").replace(", {", "{").replace('"', "").replace('{', "").replace('}', "").split(
        "|")  # prevedeni vstutu na list pro upravu
    del input[-1]  # smazani poseldniho elementu
    for i in range(len(input)):  # pruchod listu
        tmp = str(input[i])
        info_arr = tmp.split(",")  # vytvoreni noveho pole pouze s informacemi o jednom uzivateli
        for j in range(len(info_arr)):
            # rozhodovani o osloveni
            if info_arr[j] == "Muz":
                first_parm = 'Pan'
            elif info_arr[j] == "Zena":
                first_parm = 'Paní'
            # prohodit prijmeni a jmeno
            if j == 1:
                tmp = info_arr[1].split(" ")
                second_parm = tmp[2] + " " + tmp[1]
            # vypocitani veku pokud byl zadan, kdyz ne tak napsani XXX
            if j == 2 and info_arr[2] != " ":
                date_of_birth = int(info_arr[2])
                age = (int(current_year)) - date_of_birth
                fourth_param = age
            elif j == 2 and info_arr[2] == ' ':
                fourth_param = 'XXX'
            # zjistovani mista bydliste, pokud neni nahrazeni za nezname
            if j == 3 and info_arr[3] != " ":
                third_param = info_arr[3]
            elif j == 3 and info_arr[3] == ' ':
                third_param = 'neznámé'
        output.append('{0} {1}, bytem {2}, ve věku {3}.'.format(first_parm, second_parm, third_param,
                                                                fourth_param))  # kompletace noveho retezce a vlozeni do vystupniho listu
    return output


def get_me_info(file_path, sort_by):
    # kontrola zda nam byla zadana adresa pro adresar
    if not file_path:
        file_names = os.listdir(os.path.abspath(os.getcwd()))
    else:
        file_names = os.listdir(file_path)

    nested_list = []
    # vytazeni dulezitych informaci pro tabulku (nazev, suffix, velikost, datun posledni zmeny)
    for file_name in file_names:
        name, suffix = file_name.split('.')
        size = round(bit_to_mb(os.path.getsize(file_path + file_name)), 3)
        last_edit = (time.ctime(os.path.getmtime(file_path + file_name)))
        tmp = [name, "." + suffix, (str(size)), last_edit]
        nested_list.append(tmp)
    # trizeni podle druheho argumentu
    if sort_by == 'sufix':
        sorted_nested_list = sorted(nested_list, key=lambda x: x[1])
    elif sort_by == 'velikost':
        sorted_nested_list = sorted(nested_list, key=lambda x: x[2])
    elif sort_by == 'datum':
        sorted_nested_list = sorted(nested_list, key=lambda x: x[3])
    else:
        sorted_nested_list = sorted(nested_list, key=lambda x: x[0])

    # vypis tabulky i s cyklem na specificka data a vypoctem odsazeni a vlozenim datumu do zapati

    print('|--------------------------------- get_me_info -------------------------------------|')
    print('|-----------------------------------------------------------------------------------|')
    print('|-----------------------------------------------------------------------------------|')
    print('|       Soubor       |    Sufix    |   Velikost v MB   |     Naposledy změněno      |')
    print('|             <jmeno>|   <koncovka>|    <velikost v MB>|               <datum / čas>|')
    for item in sorted_nested_list:
        print("|", " " * (17 - len(item[0])), item[0], "|", " " * (10 - len(item[1])), item[1], "|",
              " " * (16 - len(item[2])), item[2], "|", " " * (25 - len(item[3])),
              item[3], "|")
    print('|-----------------------------------------------------------------------------------|')
    print('|-----------------------------------------------------------------------------------|')
    print('|----------------------------<{0}>----------------------------|'.format(
        time.strftime("%a, %d %b %Y %H:%M:%S")))


