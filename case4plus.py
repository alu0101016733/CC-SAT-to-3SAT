def case4plus(clause, i):
    variables = []
    for j in range(len(clause) - 3):
        variables.append(f"T{i}_{j}")

    tInUse = 0;

    clauses = []
    clauses.append([clause[0], clause[1], variables[tInUse]])

    for j in range(1, len(variables)):
        clauses.append(['!'+variables[tInUse], clause[j + 1], variables[tInUse + 1]])
        tInUse += 1

    clauses.append(['!'+variables[tInUse], clause[-2], clause[-1]])
    return variables, clauses


if __name__ == "__main__":
    data = {
        'U': ["u0","u1","u2","u4","u5","u6"],
        'C': [
            #["u0","u1","u2","u4"],
            #["u0","u1","u2","u4","u5"],
            ["u0","u1","u2","u4","u5","u6"]
            # ...
        ]
    }

    variables, clauses = case4plus(data['C'][0], 3)

    print(variables)
    print(clauses)
