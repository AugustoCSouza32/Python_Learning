sequence = []

while(True):
    number = int(input("number: "))
    sequence.append(number)

    exit = input("Exit ? (y / n)")

    match exit:
        case "y":
            break
        case "n":
            continue


# subtrai o proximo com o anterior até ter uma sequencia nova:

def new_sequence (numbers: list) -> list:
    new_numbers = []
    for i in range(len(numbers)):
        if i != len(new_numbers):
            num = numbers[i] - numbers[i + 1]
            new_numbers.append(num)

    return new_numbers


def its_equals (vet: list) -> bool:
    equals = len(set(vet)) <= 1