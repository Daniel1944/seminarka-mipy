def bit_to_mb(n):
    # zjistení o jaký vstup se jedná list, tuple, int
    if isinstance(n, list or n, tuple):
        mbList = []
        for x in range(len(n)):
            tmp = n[x]
            tmp = (1023.0 ** -2) * tmp
            mbList.append(tmp)
            tmp = 0
        return mbList
    else:
        return (1023.0 ** -2) * n


def ex2(information):
    current_year = 2020
    output = []
    tmp = information.strip("[]")
    input = tmp.replace("}", "}|").replace(", {", "{").replace('"', "").replace('{', "").replace('}', "").split("|")
    del input[-1]

    for i in range(len(input)):
        tmp = str(input[i])
        inforArr = tmp.split(",")
        sentences = []
        for j in range(len(inforArr)):
            if inforArr[j] == "Muz":
                sentences.append("Pan ")
            elif inforArr[j] == "Zena":
                sentences.append("Paní ")
            if j == 1:
                tmp = inforArr[1].split(" ")
                sentences.append(tmp[2] + " " + tmp[1] + ", ")
            if j == 2 and inforArr[2] != " ":
                x = int(inforArr[2])
                age = current_year - x
                sentences.append("ve věku " + str(age) + " let.")
            elif j == 2 and inforArr[2] == ' ':
                sentences.append("ve věku XXX let.")
            if j == 3 and inforArr[3] != " ":
                sentences.append("bytem " + inforArr[3])
            elif j == 3 and inforArr[3] == ' ':
                sentences.append("bytem neznámé, ")
        output.append(sentences)
    return output


x = '[{"Muz", "Novy Karel", "1950", "Praha"}, {"Zena", "Hladova Jana", "1992", ""}, {"Muz", "Janek Jan", "", "Ostrava"}]'

print(ex2(x))
