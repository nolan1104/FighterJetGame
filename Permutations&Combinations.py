
def generate_combinations(items, r):
    if r == 0:
        return [[]]  # A single combination of size 0
    if len(items) < r:
        return []  # No combinations possible
    
    # Include the first item in the combination
    with_first = [[items[0]] + combo for combo in generate_combinations(items[1:], r - 1)]
    # with_first = [[Apple] + [Banana] -> [Apple, Banana], [Apple] + [Cherry] -> [Apple, Cherry]], [Banana] + [Cherry] -> [Banana, Cherry]]
    # Exclude the first item from the combination
    without_first = generate_combinations(items[1:], r)
    
    return with_first + without_first

def generate_permutations(items):   # Generate all permutations of the given items
    if len(items) == 0:             # Base case, evaluate if the list is empty
        return [[]]                 # Return an empty list
    permutations = []               # Create an empty list
    for i in range(len(items)):     # Loop through the list
        remaining_items = items[:i] + items[i+1:]   # Get the remaining items
        for perm in generate_permutations(remaining_items): # Recursive call
            permutations.append([items[i]] + perm)  # Add the current item to the permutation
    return permutations             # Return the list of permutations
 

 # main function - everything above is copied from blackboard
def main():
    # list of names
    people = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank"]

    # number of participants to include (n)
    n = int(input("Enter the number of people (max 8): "))
    # return if number is invalid
    if n < 1 or n > 8:
        print("Invalid number. Please enter a number between 1 and 8.")
        return

    # size of groups/roles (k)
    k = int(input("Enter the size of groups/roles: "))
    # return if number is invalid
    if k < 1 or k > n:
        print("Invalid group/role size, please enter a number between 1 and the number of people.")
        return

    selected_people = people[:n]

    # calculate permutations (order matters)
    perms = generate_permutations(selected_people)
    perms = [perm for perm in perms if len(perm) == k]
    print(f"\nTotal number of permutations (order matters): {len(perms)}")
    print("First 5 permutations:")
    for perm in perms[:5]:
        print(perm)

    # calculate combinations (order doesn't matter)
    combs = generate_combinations(selected_people, k)
    print(f"\nTotal number of combinations (order doesn't matter): {len(combs)}")
    print("First 5 combinations:")
    for comb in combs[:5]:
        print(comb)

if __name__ == "__main__":
    main()
