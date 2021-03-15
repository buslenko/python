import math

def f23(table):
    for i in range(len(table) - 1):
        if table[i][0] is None:
            del table[i]

    for r in table:
        if r[0] == "Да":
            r[0] = "Выполнено"
        else:
            r[0] = "Не выполнено"
        tmp = r[1].split('&')
        r.append(str(round(float(tmp[1]), 1)))
        r[1] = (tmp[0].split(' ')[1])

    return table

print(
    f23(
        [
            ["Да", "Амир Бучоний&0.85"],
            ["Да", "Гордей Фосев&0.65"],
            [None, None],
            ["Да", "Станислав Кушифов&0.65"],
            ["Да", "Юрий Зешберг&0.46"],
        ]
    )
)