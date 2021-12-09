def case1(clause, i):
    variables = [f"T{i}_0", f"T{i}_1"]
    clauses = [clause.copy(), clause.copy(), clause.copy(), clause.copy()]

    clauses[0].extend([      variables[0],       variables[1]])
    clauses[1].extend([      variables[0], '!' + variables[1]])
    clauses[2].extend(['!' + variables[0],       variables[1]])
    clauses[3].extend(['!' + variables[0], '!' + variables[1]])

    return variables, clauses


if __name__ == "__main__":
    data = {
        'U': ["u0"],
        'C': [
            ["u0"],
            # ...
        ]
    }

    variables, clauses = case1(data['C'][0], 3)

    print(variables)
    print(clauses)
