# -*- coding: utf-8 -*-
"""LabPA_4_Sg1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CKa59Q2FykLKdT72IiLm8VZv7dtIf0vz

Exercitiul 1
"""

def main():
    with open("test.in", "r") as input, open("test.out", "w") as output:
        nota = 1
        for line in input.read().split():
            nr1, nr2, result = [int(x) for x in line.replace("=", "*").split("*")]
            if nr1 * nr2 != result:
                line = line + f" Gresit {nr1 * nr2}"
            else:
                nota += 1
                line = line + " Corect"
            print(line, file=output)
        print(f"Nota {nota}", file=output)

main()

"""Exercitiul 2"""

# 64 Danil Marius
# 70 Derek Alexandru
# 100 Pirpiric Claudiu
# 18 Alexandrescu Matias
# 64 Popescu Catalin
# 100 Cozia Daniel
# 82 Stefan Dinca
# -1

def main():
    lista_punctaje = []
    punctaj_si_nume = input()
    counter = 1
    while punctaj_si_nume != "-1":
        punctaj, nume = punctaj_si_nume.split(" ", 1)
        lista_punctaje.append((int(punctaj), nume, counter))
        counter += 1
        punctaj_si_nume = input()
    set_punctaje = set(sorted([punctaj for punctaj, nume, count in lista_punctaje], reverse=True))
    punctaje_sortate = sorted(list(set_punctaje), reverse=True)
    dict_punctaje = {}
    for punctaj in punctaje_sortate:
        dict_punctaje[punctaj] = [(nume, count) for p, nume, count in lista_punctaje if p==punctaj]
    print(dict_punctaje)
    
main()

"""Exercitiul 3"""

from math import sqrt

def primes():
    yield 2
    p=3
    while True:
        i=3
        while i <= sqrt(p):
            if p % i == 0:
                break
            i += 2
        else:
            yield p
        p += 2

n = int(input())
for i in primes():
    if i<=n:
        print(i)
    else:
        break
print()

for i in primes():
    if n:
        print(i)
        n -= 1
    else:
        break

"""Exercitiul 4"""

def min_max(*args):
    try:
        nrs = [int(i) for i in args]
        return min(nrs), max(nrs)
    except (TypeError, ValueError) as e:
        return None

def main():
    try:
        with open("numere.txt", "r") as numere:
            ret = min_max(*numere.read().split())
            print(ret)
            if ret != None:
                with open("impartire.txt", "w") as impartire:
                    impartit = float(ret[1]) / float(ret[0])
                    print(impartit, file=impartire)

    except (FileNotFoundError, OSError, ValueError, ZeroDivisionError) as e:
        print(e)

if __name__ == "__main__":
    main()

"""Exercitiul 5"""

from functools import cmp_to_key

def comp_implicit(str1, str2):
    if str1 > str2:
        return 1
    elif str1 == str2:
        return 0
    else:
        return -1

def comp_len_lexicografic(str1, str2):
    if len(str1) != len(str2):
        return comp_implicit(len(str1), len(str2))
    return comp_implicit(str1, str2)

def comp_len(str1, str2):
    if len(str1) != len(str2):
        return comp_implicit(len(str1), len(str2))
    return 0

def main():
    with open("cuvinte.txt", "r") as cuvinte, open("cuv_sortate.txt", "w") as cuv_sortate:
        cuv = cuvinte.read().split()
        print(*sorted(cuv, key=cmp_to_key(comp_implicit), reverse=True), file=cuv_sortate)
        print(*sorted(cuv, key=cmp_to_key(comp_len_lexicografic)), file=cuv_sortate)
        print(*sorted(cuv, key=cmp_to_key(comp_len)), file=cuv_sortate)

if __name__ == "__main__":
    main()