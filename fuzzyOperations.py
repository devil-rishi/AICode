A = {"x1": 0.2, "x2": 0.7, "x3": 1.0}
B = {"x1": 0.5, "x2": 0.4, "x3": 0.9}

def fuzzy_union(A, B):
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_intersection(A, B):
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) & set(B)}

def compliment(A):
    return {x: 1 - A[x] for x in A}

def fuzzy_cartesian(A, B):
    return {(x, y): min(A[x], B[y]) for x in A for y in B}

def max_min_composition(R1, R2, X, Y, Z):
    result = {}
    for x in X:
        for z in Z:
            values = []
            for y in Y:
                values.append(min(R1.get((x, y), 0), R2.get((y, z), 0)))
            result[(x, z)] = max(values)
    return result

print("Union", fuzzy_union(A, B))
print("Intersection", fuzzy_intersection(A, B))
print("Complement of A", compliment(A))
print("Cartesian Product ", fuzzy_cartesian(A, B))

X = {"x1", "x2"}
Y = {"y1", "y2"}
Z = {"z1", "z2"}

R1 = {("x1", "y1"): 0.7, ("x1", "y2"): 0.4, ("x2", "y1"): 0.9, ("x2", "y2"): 0.5}
R2 = {("y1", "z1"): 0.8, ("y1", "z2"): 0.6, ("y2", "z1"): 0.3, ("y2", "z2"): 0.7}

print("Max-Min Composition: ", max_min_composition(R1, R2, X, Y, Z))
