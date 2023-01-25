import math
import  random

cmp_ijm = 0
inp_id = input("Enter your student ID: ")
minimum_value = int(input("Minimum value for the range of negative HP: "))
maximum_value= int(input("Maximum value for the range of negative HP: "))
init_h = int(inp_id[:-3:-1])
dpt = int(inp_id[0]) * 2
bnch = int(inp_id[2])
print("Depth and Branches ratio is", dpt, ":", bnch)


def pruning(aph, bta, ind, dpt, attack ):

    global cmp_ijm

    if dpt == 0:
        return ijm_list[ind]

    if attack:
        ijm_list[ind] = -math.inf
        start = (bnch * ind) + 1
        stop = (bnch * ind + bnch) + 1
        for i in range(start, stop):
            val = pruning(aph, bta, i,dpt - 1, False)
            ijm_list[ind] = max(ijm_list[ind], val)
            aph = max(aph, val)
            if aph >= bta:
                break
        return ijm_list[ind]

    else:
        ijm_list[ind] = math.inf
        start = bnch * ind + 1
        stop = (bnch * ind) + bnch + 1
        for i in range(start, stop):
            val = pruning(aph, bta, i,dpt - 1, True)
            ijm_list[ind] = min(ijm_list[ind], val)
            if dpt == 1:
                cmp_ijm += 1
            bta = min(bta, val)
            if aph >= bta:
                break
        return ijm_list[ind]


ijm_list = []
for i in range(dpt):
    node = pow(bnch, i)
    for j in range(node):
        if i % 2 == 0:
            ijm_list.append(-math.inf)
        else:
            ijm_list.append(math.inf)
ijm_rnodes =[]
for i in range(pow(bnch, dpt)):
     ijm_rnodes.append(random.randint(minimum_value, max_val))
ijm_list += ijm_rnodes
print("Terminal States (leaf node values) are", str(ijm_rnodes)[1:-1])
pruning(-math.inf, math.inf,0, dpt, True)
print("Left life(HP) of the defender after maximum damage caused by the attacker is ", init_h - ijm_list[0])
print("After apha-beta Pruning Leaf Node Comparisons", cmp_ijm)