#!/usr/bin/env python3

# # Adders
#
# Author: Vladislav Valek
#
# ## Exact Adder Function
#
# Outpus also the energy consumption for each result.

# In[30]:

def exactAdder(a, b, c):
    truth_table = {
        ("000", "000", 0) : ("000", 0, 200, 1.3),
        ("000", "000", 1) : ("001", 0, 200, 1.3),
        ("000", "001", 0) : ("001", 0, 200, 1.3),
        ("000", "001", 1) : ("010", 0, 200, 1.3),
        ("000", "010", 0) : ("010", 0, 200, 1.3),
        ("000", "010", 1) : ("011", 0, 200, 1.3),
        ("000", "011", 0) : ("011", 0, 200, 1.3),
        ("000", "011", 1) : ("100", 0, 200, 1.3),
        ("000", "100", 0) : ("100", 0, 200, 1.3),
        ("000", "100", 1) : ("101", 0, 200, 1.3),
        ("000", "101", 0) : ("101", 0, 200, 1.3),
        ("000", "101", 1) : ("110", 0, 200, 1.3),
        ("000", "110", 0) : ("110", 0, 200, 1.3),
        ("000", "110", 1) : ("111", 0, 200, 1.3),
        ("000", "111", 0) : ("111", 0, 200, 1.3),
        ("000", "111", 1) : ("000", 1, 200, 1.3),
        ("001", "000", 0) : ("001", 0, 200, 1.3),
        ("001", "000", 1) : ("010", 0, 200, 1.3),
        ("001", "001", 0) : ("010", 0, 200, 1.3),
        ("001", "001", 1) : ("011", 0, 200, 1.3),
        ("001", "010", 0) : ("011", 0, 200, 1.3),
        ("001", "010", 1) : ("100", 0, 200, 1.3),
        ("001", "011", 0) : ("100", 0, 200, 1.3),
        ("001", "011", 1) : ("101", 0, 200, 1.3),
        ("001", "100", 0) : ("101", 0, 200, 1.3),
        ("001", "100", 1) : ("110", 0, 200, 1.3),
        ("001", "101", 0) : ("110", 0, 200, 1.3),
        ("001", "101", 1) : ("111", 0, 200, 1.3),
        ("001", "110", 0) : ("111", 0, 200, 1.3),
        ("001", "110", 1) : ("000", 1, 200, 1.3),
        ("001", "111", 0) : ("000", 1, 200, 1.3),
        ("001", "111", 1) : ("001", 1, 200, 1.3),
        ("010", "000", 0) : ("010", 0, 200, 1.3),
        ("010", "000", 1) : ("011", 0, 200, 1.3),
        ("010", "001", 0) : ("011", 0, 200, 1.3),
        ("010", "001", 1) : ("100", 0, 200, 1.3),
        ("010", "010", 0) : ("100", 0, 200, 1.3),
        ("010", "010", 1) : ("101", 0, 200, 1.3),
        ("010", "011", 0) : ("101", 0, 200, 1.3),
        ("010", "011", 1) : ("110", 0, 200, 1.3),
        ("010", "100", 0) : ("110", 0, 200, 1.3),
        ("010", "100", 1) : ("111", 0, 200, 1.3),
        ("010", "101", 0) : ("111", 0, 200, 1.3),
        ("010", "101", 1) : ("000", 1, 200, 1.3),
        ("010", "110", 0) : ("000", 1, 200, 1.3),
        ("010", "110", 1) : ("001", 1, 200, 1.3),
        ("010", "111", 0) : ("001", 1, 200, 1.3),
        ("010", "111", 1) : ("010", 1, 200, 1.3),
        ("011", "000", 0) : ("011", 0, 200, 1.3),
        ("011", "000", 1) : ("100", 0, 200, 1.3),
        ("011", "001", 0) : ("100", 0, 200, 1.3),
        ("011", "001", 1) : ("101", 0, 200, 1.3),
        ("011", "010", 0) : ("101", 0, 200, 1.3),
        ("011", "010", 1) : ("110", 0, 200, 1.3),
        ("011", "011", 0) : ("110", 0, 200, 1.3),
        ("011", "011", 1) : ("111", 0, 200, 1.3),
        ("011", "100", 0) : ("111", 0, 200, 1.3),
        ("011", "100", 1) : ("000", 1, 200, 1.3),
        ("011", "101", 0) : ("000", 1, 200, 1.3),
        ("011", "101", 1) : ("001", 1, 200, 1.3),
        ("011", "110", 0) : ("001", 1, 200, 1.3),
        ("011", "110", 1) : ("010", 1, 200, 1.3),
        ("011", "111", 0) : ("010", 1, 200, 1.3),
        ("011", "111", 1) : ("011", 1, 200, 1.3),
        ("100", "000", 0) : ("100", 0, 200, 1.3),
        ("100", "000", 1) : ("101", 0, 200, 1.3),
        ("100", "001", 0) : ("101", 0, 200, 1.3),
        ("100", "001", 1) : ("110", 0, 200, 1.3),
        ("100", "010", 0) : ("110", 0, 200, 1.3),
        ("100", "010", 1) : ("111", 0, 200, 1.3),
        ("100", "011", 0) : ("111", 0, 200, 1.3),
        ("100", "011", 1) : ("000", 1, 200, 1.3),
        ("100", "100", 0) : ("000", 1, 200, 1.3),
        ("100", "100", 1) : ("001", 1, 200, 1.3),
        ("100", "101", 0) : ("001", 1, 200, 1.3),
        ("100", "101", 1) : ("010", 1, 200, 1.3),
        ("100", "110", 0) : ("010", 1, 200, 1.3),
        ("100", "110", 1) : ("011", 1, 200, 1.3),
        ("100", "111", 0) : ("011", 1, 200, 1.3),
        ("100", "111", 1) : ("100", 1, 200, 1.3),
        ("101", "000", 0) : ("101", 0, 200, 1.3),
        ("101", "000", 1) : ("110", 0, 200, 1.3),
        ("101", "001", 0) : ("110", 0, 200, 1.3),
        ("101", "001", 1) : ("111", 0, 200, 1.3),
        ("101", "010", 0) : ("111", 0, 200, 1.3),
        ("101", "010", 1) : ("000", 1, 200, 1.3),
        ("101", "011", 0) : ("000", 1, 200, 1.3),
        ("101", "011", 1) : ("001", 1, 200, 1.3),
        ("101", "100", 0) : ("001", 1, 200, 1.3),
        ("101", "100", 1) : ("010", 1, 200, 1.3),
        ("101", "101", 0) : ("010", 1, 200, 1.3),
        ("101", "101", 1) : ("011", 1, 200, 1.3),
        ("101", "110", 0) : ("011", 1, 200, 1.3),
        ("101", "110", 1) : ("100", 1, 200, 1.3),
        ("101", "111", 0) : ("100", 1, 200, 1.3),
        ("101", "111", 1) : ("101", 1, 200, 1.3),
        ("110", "000", 0) : ("110", 0, 200, 1.3),
        ("110", "000", 1) : ("111", 0, 200, 1.3),
        ("110", "001", 0) : ("111", 0, 200, 1.3),
        ("110", "001", 1) : ("000", 1, 200, 1.3),
        ("110", "010", 0) : ("000", 1, 200, 1.3),
        ("110", "010", 1) : ("001", 1, 200, 1.3),
        ("110", "011", 0) : ("001", 1, 200, 1.3),
        ("110", "011", 1) : ("010", 1, 200, 1.3),
        ("110", "100", 0) : ("010", 1, 200, 1.3),
        ("110", "100", 1) : ("011", 1, 200, 1.3),
        ("110", "101", 0) : ("011", 1, 200, 1.3),
        ("110", "101", 1) : ("100", 1, 200, 1.3),
        ("110", "110", 0) : ("100", 1, 200, 1.3),
        ("110", "110", 1) : ("101", 1, 200, 1.3),
        ("110", "111", 0) : ("101", 1, 200, 1.3),
        ("110", "111", 1) : ("110", 1, 200, 1.3),
        ("111", "000", 0) : ("111", 0, 200, 1.3),
        ("111", "000", 1) : ("000", 1, 200, 1.3),
        ("111", "001", 0) : ("000", 1, 200, 1.3),
        ("111", "001", 1) : ("001", 1, 200, 1.3),
        ("111", "010", 0) : ("001", 1, 200, 1.3),
        ("111", "010", 1) : ("010", 1, 200, 1.3),
        ("111", "011", 0) : ("010", 1, 200, 1.3),
        ("111", "011", 1) : ("011", 1, 200, 1.3),
        ("111", "100", 0) : ("011", 1, 200, 1.3),
        ("111", "100", 1) : ("100", 1, 200, 1.3),
        ("111", "101", 0) : ("100", 1, 200, 1.3),
        ("111", "101", 1) : ("101", 1, 200, 1.3),
        ("111", "110", 0) : ("101", 1, 200, 1.3),
        ("111", "110", 1) : ("110", 1, 200, 1.3),
        ("111", "111", 0) : ("110", 1, 200, 1.3),
        ("111", "111", 1) : ("111", 1, 200, 1.3),
    }

    return truth_table[a, b, c]

# ## Approximate Adder Function
#
# The output result deviates from the exact solution.
#

# In[31]:

def approxAdder(a, b, c):
    truth_table = {
        ("000", "000", 0) : ("000", 0, 200, 1.3),
        ("000", "000", 1) : ("001", 0, 200, 1.3),
        ("000", "001", 0) : ("001", 0, 200, 1.3),
        ("000", "001", 1) : ("010", 0, 200, 1.3),
        ("000", "010", 0) : ("010", 0, 200, 1.3),
        ("000", "010", 1) : ("011", 0, 200, 1.3),
        ("000", "011", 0) : ("011", 0, 200, 1.3),
        ("000", "011", 1) : ("100", 0, 200, 1.3),
        ("000", "100", 0) : ("100", 0, 200, 1.3),
        ("000", "100", 1) : ("101", 0, 200, 1.3),
        ("000", "101", 0) : ("101", 0, 200, 1.3),
        ("000", "101", 1) : ("110", 0, 200, 1.3),
        ("000", "110", 0) : ("110", 0, 200, 1.3),
        ("000", "110", 1) : ("111", 0, 200, 1.3),
        ("000", "111", 0) : ("111", 0, 200, 1.3),
        ("000", "111", 1) : ("000", 0, 200, 1.3),
        ("001", "000", 0) : ("001", 0, 200, 1.3),
        ("001", "000", 1) : ("010", 0, 200, 1.3),
        ("001", "001", 0) : ("010", 0, 200, 1.3),
        ("001", "001", 1) : ("011", 0, 200, 1.3),
        ("001", "010", 0) : ("011", 0, 200, 1.3),
        ("001", "010", 1) : ("100", 0, 200, 1.3),
        ("001", "011", 0) : ("100", 0, 200, 1.3),
        ("001", "011", 1) : ("101", 0, 200, 1.3),
        ("001", "100", 0) : ("101", 0, 200, 1.3),
        ("001", "100", 1) : ("110", 0, 200, 1.3),
        ("001", "101", 0) : ("110", 0, 200, 1.3),
        ("001", "101", 1) : ("111", 0, 200, 1.3),
        ("001", "110", 0) : ("111", 0, 200, 1.3),
        ("001", "110", 1) : ("000", 0, 200, 1.3),
        ("001", "111", 0) : ("000", 0, 200, 1.3),
        ("001", "111", 1) : ("001", 0, 200, 1.3),
        ("010", "000", 0) : ("010", 0, 200, 1.3),
        ("010", "000", 1) : ("011", 0, 200, 1.3),
        ("010", "001", 0) : ("011", 0, 200, 1.3),
        ("010", "001", 1) : ("100", 0, 200, 1.3),
        ("010", "010", 0) : ("100", 1, 200, 1.3),
        ("010", "010", 1) : ("101", 1, 200, 1.3),
        ("010", "011", 0) : ("101", 1, 200, 1.3),
        ("010", "011", 1) : ("110", 1, 200, 1.3),
        ("010", "100", 0) : ("110", 0, 200, 1.3),
        ("010", "100", 1) : ("111", 0, 200, 1.3),
        ("010", "101", 0) : ("111", 0, 200, 1.3),
        ("010", "101", 1) : ("000", 0, 200, 1.3),
        ("010", "110", 0) : ("000", 1, 200, 1.3),
        ("010", "110", 1) : ("001", 1, 200, 1.3),
        ("010", "111", 0) : ("001", 1, 200, 1.3),
        ("010", "111", 1) : ("010", 1, 200, 1.3),
        ("011", "000", 0) : ("011", 0, 200, 1.3),
        ("011", "000", 1) : ("100", 0, 200, 1.3),
        ("011", "001", 0) : ("100", 0, 200, 1.3),
        ("011", "001", 1) : ("101", 0, 200, 1.3),
        ("011", "010", 0) : ("101", 1, 200, 1.3),
        ("011", "010", 1) : ("110", 1, 200, 1.3),
        ("011", "011", 0) : ("110", 1, 200, 1.3),
        ("011", "011", 1) : ("111", 1, 200, 1.3),
        ("011", "100", 0) : ("111", 0, 200, 1.3),
        ("011", "100", 1) : ("000", 0, 200, 1.3),
        ("011", "101", 0) : ("000", 0, 200, 1.3),
        ("011", "101", 1) : ("001", 0, 200, 1.3),
        ("011", "110", 0) : ("001", 1, 200, 1.3),
        ("011", "110", 1) : ("010", 1, 200, 1.3),
        ("011", "111", 0) : ("010", 1, 200, 1.3),
        ("011", "111", 1) : ("011", 1, 200, 1.3),
        ("100", "000", 0) : ("100", 0, 200, 1.3),
        ("100", "000", 1) : ("101", 0, 200, 1.3),
        ("100", "001", 0) : ("101", 0, 200, 1.3),
        ("100", "001", 1) : ("110", 0, 200, 1.3),
        ("100", "010", 0) : ("110", 0, 200, 1.3),
        ("100", "010", 1) : ("111", 0, 200, 1.3),
        ("100", "011", 0) : ("111", 0, 200, 1.3),
        ("100", "011", 1) : ("000", 0, 200, 1.3),
        ("100", "100", 0) : ("000", 0, 200, 1.3),
        ("100", "100", 1) : ("001", 0, 200, 1.3),
        ("100", "101", 0) : ("001", 0, 200, 1.3),
        ("100", "101", 1) : ("010", 0, 200, 1.3),
        ("100", "110", 0) : ("010", 0, 200, 1.3),
        ("100", "110", 1) : ("011", 0, 200, 1.3),
        ("100", "111", 0) : ("011", 0, 200, 1.3),
        ("100", "111", 1) : ("100", 0, 200, 1.3),
        ("101", "000", 0) : ("101", 0, 200, 1.3),
        ("101", "000", 1) : ("110", 0, 200, 1.3),
        ("101", "001", 0) : ("110", 0, 200, 1.3),
        ("101", "001", 1) : ("111", 0, 200, 1.3),
        ("101", "010", 0) : ("111", 0, 200, 1.3),
        ("101", "010", 1) : ("000", 0, 200, 1.3),
        ("101", "011", 0) : ("000", 0, 200, 1.3),
        ("101", "011", 1) : ("001", 0, 200, 1.3),
        ("101", "100", 0) : ("001", 0, 200, 1.3),
        ("101", "100", 1) : ("010", 0, 200, 1.3),
        ("101", "101", 0) : ("010", 0, 200, 1.3),
        ("101", "101", 1) : ("011", 0, 200, 1.3),
        ("101", "110", 0) : ("011", 0, 200, 1.3),
        ("101", "110", 1) : ("100", 0, 200, 1.3),
        ("101", "111", 0) : ("100", 0, 200, 1.3),
        ("101", "111", 1) : ("101", 0, 200, 1.3),
        ("110", "000", 0) : ("110", 0, 200, 1.3),
        ("110", "000", 1) : ("111", 0, 200, 1.3),
        ("110", "001", 0) : ("111", 0, 200, 1.3),
        ("110", "001", 1) : ("000", 0, 200, 1.3),
        ("110", "010", 0) : ("000", 1, 200, 1.3),
        ("110", "010", 1) : ("001", 1, 200, 1.3),
        ("110", "011", 0) : ("001", 1, 200, 1.3),
        ("110", "011", 1) : ("010", 1, 200, 1.3),
        ("110", "100", 0) : ("010", 0, 200, 1.3),
        ("110", "100", 1) : ("011", 0, 200, 1.3),
        ("110", "101", 0) : ("011", 0, 200, 1.3),
        ("110", "101", 1) : ("100", 0, 200, 1.3),
        ("110", "110", 0) : ("100", 1, 200, 1.3),
        ("110", "110", 1) : ("101", 1, 200, 1.3),
        ("110", "111", 0) : ("101", 1, 200, 1.3),
        ("110", "111", 1) : ("110", 1, 200, 1.3),
        ("111", "000", 0) : ("111", 0, 200, 1.3),
        ("111", "000", 1) : ("000", 0, 200, 1.3),
        ("111", "001", 0) : ("000", 0, 200, 1.3),
        ("111", "001", 1) : ("001", 0, 200, 1.3),
        ("111", "010", 0) : ("001", 1, 200, 1.3),
        ("111", "010", 1) : ("010", 1, 200, 1.3),
        ("111", "011", 0) : ("010", 1, 200, 1.3),
        ("111", "011", 1) : ("011", 1, 200, 1.3),
        ("111", "100", 0) : ("011", 0, 200, 1.3),
        ("111", "100", 1) : ("100", 0, 200, 1.3),
        ("111", "101", 0) : ("100", 0, 200, 1.3),
        ("111", "101", 1) : ("101", 0, 200, 1.3),
        ("111", "110", 0) : ("101", 1, 200, 1.3),
        ("111", "110", 1) : ("110", 1, 200, 1.3),
        ("111", "111", 0) : ("110", 1, 200, 1.3),
        ("111", "111", 1) : ("111", 1, 200, 1.3),
    }

    return truth_table[a, b, c]

# ### N-bit Adder Function
#
# The MyNbitAdder function is designed to perform N-bit addition. Approximation takes place from lower bits to higher ones and the amount of approximated bits can be configured with 'approx_until' parameter. THe adder can also work with negative numbers as inputs. The 'n' parameter defines the bit length of the internally represented binary numbers.

# In[32]:

def multiBitAdder(a,b, nstages = 4, approx_until = 0):

    # Ensure that a and b are within range of signed integer
    # a = (a + 2**((nstages * 3) - 1)) % 2**(nstages * 3) - 2**((nstages * 3) - 1)
    # b = (b + 2**((nstages * 3) - 1)) % 2**(nstages * 3) - 2**((nstages * 3) - 1)

    #convert to binary and cut off the first two indices (they dont belong to the number but indicate that it is binary)
    # Eventually fill with 0 to the full length of n
    a_bin = bin(a & ((1 << (nstages * 3)) - 1))[2:].zfill(nstages * 3)
    b_bin = bin(b & ((1 << (nstages * 3)) - 1))[2:].zfill(nstages * 3)

    # print(a_bin)
    # print(b_bin)

    #reverse order bits for the adder
    # rev_a , rev_b = list(a_bin[::-1]), list(b_bin[::-1])
    rev_a = [a_bin[i:i+3] for i in range(0, len(a_bin), 3)][::-1]
    rev_b = [b_bin[i:i+3] for i in range(0, len(b_bin), 3)][::-1]

    # print(rev_a)
    # print(rev_b)

    bit_vector = ""
    carry_over   = 0
    total_sum    = 0
    total_energy = 0
    total_proctime = 0

    #we want to do a bitwise addition
    for index, (sa, sb) in enumerate(zip(rev_a, rev_b)):

        if index < approx_until:
            #use approx_adder
            sum_element, carry_over, energy, proctime = approxAdder(sa, sb, int(carry_over))
        else:
            #use exact_adder
            sum_element, carry_over, energy, proctime = exactAdder(sa, sb, int(carry_over))

        # print(f"{index}: {sa} + {sb} = {sum_element} -> {carry_over}")
        bit_vector = sum_element + bit_vector
        total_energy += energy
        total_proctime += proctime

    # print(bit_vector)

    # for index in bit_vector:
    #     total_sum += pow(2,index)*sum_element
    total_sum = int(bit_vector,2)
    # print(total_sum)

    if total_sum >= 2**((nstages * 3)-1):
        total_sum -= 2**(nstages * 3)

    # print(total_sum)

    return total_sum, total_energy, total_proctime
