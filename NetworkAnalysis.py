
# The main thing I did not really understand was how to implement the mathematical induction.

# check reflexivity for friends of network
def reflexivity(net):
    for user in net:
        if user not in net[user]:
            return False
    return True

# check symmetry for friends
def symmetry(net):
    for user in net:
        for friend in net[user]:
            if friend in net and user not in net[friend]:
                return False
    return True

# check transitivity for friends
def transitivity(net):
    for user in net:
        for friend in net[user]:
            if friend in net:
                for friend_of_friend in net[friend]:
                    if friend_of_friend not in net[user]:
                        return False
    return True

# validate claims using direct proofs and countrexamples
def validate_claims(net):
    if reflexivity(net):
        print("The network is reflexive.")      # direct proof for reflexivity
    else:
        print("The network is not reflexive.")  # counterexample for reflexivity


    if symmetry(net):
        print("The network is symmetric.")
    else:
        print("The network is not symmetric.")


    if transitivity(net):
        print("The network is transitive.")
    else:
        print("The network is not transitive.")

# network of friends
network = {
    'Nolan': {'Nolan', 'Nick'},
    'Nick': {'Nick', 'Nolan', 'Chris'},
    'Chris': {'Chris', 'Nick'},
    'Cole': {'Cole'}
}

# print results
print("Reflexivity:", reflexivity(network))
print("Symmetry:", symmetry(network))
print("Transitivity:", transitivity(network))

# validate claims
validate_claims(network)