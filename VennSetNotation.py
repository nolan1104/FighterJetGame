import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Union of a set
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
union_AB = A | B
print("Union of A and B:", union_AB)

venn2([A, B], ("A", "B"))
plt.title("Union of A and B")
plt.show()

# Helps me distinguish each section in the terminal
print("---------------------------------------------------------------------------------------------------------------------")

# Intersection of a set
A = {2, 4, 6, 8}
B = {3, 5, 6, 9}
intersection_AB = A & B
print("Intersection of A and B:", intersection_AB)

venn2([A, B], ("A", "B"))
plt.title("Intersection of A and B")
plt.show()

print("---------------------------------------------------------------------------------------------------------------------")

# Difference of a set
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
difference_AB = A - B
print("Difference of A and B:", difference_AB)

venn2([A, B], ("A", "B"))
plt.title("Difference of A and B")
plt.show()

print("---------------------------------------------------------------------------------------------------------------------")

# Complement of a set
A = {2, 4, 6, 8}
U = {1, 2, 3, 4, 5, 6, 7, 8, 9}
completement_A = U - A
print("Complement of A:", completement_A)

print("---------------------------------------------------------------------------------------------------------------------")

# Application of Set Operations
students = 30
basketball_students = 18
football_students = 15
both_students = 10
neither_students = students - (basketball_students + football_students - both_students)
print("Number of students who play either football or basketball:", students - neither_students)
print("Number of students who play neither football nor basketball:", neither_students)

print("---------------------------------------------------------------------------------------------------------------------")

# Applying Indempotnece Law
A = {1, 2, 3}
B = {2, 3, 4}

print("Union of A:", A | A == A)
print("Intersection of A:", A & A == A)
print("Union of B:", B | B == B)
print("Intersection of B:", B & B == B)

print("---------------------------------------------------------------------------------------------------------------------")

# Applying Commutative Law
A = {1, 2, 3}
B = {2, 3, 4}

print("Union of A and B:", A | B == B | A)
print("Intersection of A and B:", A & B == B & A)

print("---------------------------------------------------------------------------------------------------------------------")

# Applying Associative Law
A = {1, 2}
B = {2, 3}
C = {3, 4}

print("Union of A, B, and C:", (A | B) | C == A | (B | C))
print("Intersection of A, B, and C:", (A & B) & C == A & (B & C))

print("---------------------------------------------------------------------------------------------------------------------")

# Applying Distributive Law
A = {1, 2}
B = {2, 3}
C = {3, 4}

print("Union of A and (B intersection C):", A | (B & C) == (A | B) & (A | C))
print("Intersection of A and (B union C):", A & (B | C) == (A & B) | (A & C))

print("---------------------------------------------------------------------------------------------------------------------")

# Using set operations to solve problems
S = {"Alice", "Bob", "Charlie"}   # Set of all students
C1 = {"Alice", "Bob"}             # Set of students in course 1
C2 = {"Bob", "Charlie"}           # Set of students in course 2

print("Students enrolled in both courses:", C1 & C2)
print("Students enrolled in at least one course:", C1 | C2)
print("Student who is only enrolled in course 1:", C1 - C2)



