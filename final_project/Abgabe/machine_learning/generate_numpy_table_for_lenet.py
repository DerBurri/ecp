from functools import reduce
import numpy as np
# ## Approximate Adder Function
#
# The output result deviates from the exact solution.
#



#In 8 Bit Adder, lower 3 bits are implemented approximated. Higher 5 Bit calculate exact
def My_12BitAdder(a,b,approx_until=1, nstages=4):
    a_bin = bin(a & ((1 << (nstages * 3)) - 1))[2:].zfill(nstages * 3)
    b_bin = bin(b & ((1 << (nstages * 3)) - 1))[2:].zfill(nstages * 3)

    # print(a_bin)
    # print(b_bin)

    #reverse order bits for the adder
    # rev_a , rev_b = list(a_bin[::-1]), list(b_bin[::-1])
    rev_a = [a_bin[i:i+3] for i in range(0, len(a_bin), 3)][::-1]
    rev_b = [b_bin[i:i+3] for i in range(0, len(b_bin), 3)][::-1]

    bit_vector = ""
    carry_over  = 0
    total_sum   = 0
    total_energy_consumption = 0
    total_delay = 0

    #we want to do a bitwise addition
    for index, (bit1, bit2) in enumerate( zip(rev_a, rev_b) ):

        if index < approx_until:
            #use approx_adder
            #print("used approx adder")
            sum_element, carry_over , _energy, _delay = approxAdder_3bit(int(bit1,2), int(bit2,2), int(carry_over) )             
            #print(sum_element)

        else:
            #use exact_adder
            #print("used exact adder")
            #print(bit1, bit2, carry_over)
            sum_element, carry_over, _energy,_delay = exactAdder_3bit(int(bit1,2), int(bit2,2), int(carry_over) )
            #print(sum_element)
            #print("carry ", carry_over)

        
        bit_vector = sum_element + bit_vector
        total_energy_consumption += _energy
        total_delay += _delay

    total_sum = int(bit_vector,2)

    if total_sum >= 2**((nstages * 3)-1):
        total_sum -= 2**(nstages * 3)
    return total_sum, total_energy_consumption, total_delay

def My_12BitSubtractor(a, b,nstages=4,approx_until=1):
    # convert to binary
    a_bin = bin(a & ((1 << (nstages * 3)) - 1))[2:].zfill(nstages * 3)
    b_bin = bin(b & ((1 << (nstages * 3)) - 1))[2:].zfill(nstages * 3)
    # calculate 2's complement of b
    b_bin = ''.join('1' if bit == '0' else '0' for bit in b_bin)
    b_bin = bin(int(b_bin, 2) + 1)[2:].zfill(nstages * 3)

    # add a and 2's complement of b
    result, energy ,delay= My_12BitAdder(int(a_bin, 2), int(b_bin, 2),approx_until=approx_until,nstages=nstages)

    return np.int16(result), energy, delay

def My_12BitMultiplier(a, b, approx_until=1,nstages=4):
    # Convert inputs to two's complement representation if negative
    a = a if a >= 0 else pow(2,nstages*3) + a
    b = b if b >= 0 else pow(2,nstages*3) + b

    total_result = 0
    total_energy_consumption = 0
    total_delay = 0
    
    for _ in range(b):

        total_result,energy,delay = My_12BitAdder(total_result,a,approx_until=approx_until,nstages=nstages)
        total_energy_consumption += energy
        total_delay += delay

    # Prevent overflow
    total_result = total_result if total_result < pow(2,nstages*3) else total_result - pow(2,nstages*3)

    return np.int16(total_result), total_energy_consumption, total_delay

#In 8 Bit Adder, lower 3 bits are implemented approximated. Higher 5 Bit calculate exact
def My_12BitAdder(a,b,approx_until=1, nstages=4):
    a_bin = bin(a & ((1 << (nstages * 3)) - 1))[2:].zfill(nstages * 3)
    b_bin = bin(b & ((1 << (nstages * 3)) - 1))[2:].zfill(nstages * 3)

    # print(a_bin)
    # print(b_bin)

    #reverse order bits for the adder
    # rev_a , rev_b = list(a_bin[::-1]), list(b_bin[::-1])
    rev_a = [a_bin[i:i+3] for i in range(0, len(a_bin), 3)][::-1]
    rev_b = [b_bin[i:i+3] for i in range(0, len(b_bin), 3)][::-1]

    bit_vector = ""
    carry_over  = 0
    total_sum   = 0
    total_energy_consumption = 0
    total_delay = 0

    #we want to do a bitwise addition
    for index, (bit1, bit2) in enumerate( zip(rev_a, rev_b) ):

        if index < approx_until:
            #use approx_adder
            sum_element, carry_over , _energy, _delay = approxAdder_3bit(int(bit1,2), int(bit2,2), int(carry_over) ) 
        else:
            #use exact_adder
            sum_element, carry_over, _energy,_delay = exactAdder_3bit(int(bit1,2), int(bit2,2), int(carry_over) )
        
        bit_vector = sum_element + bit_vector
        total_energy_consumption += _energy
        total_delay += _delay

    total_sum = int(bit_vector,2)

    if total_sum >= 2**((nstages * 3)-1):
        total_sum -= 2**(nstages * 3)
    return total_sum, total_energy_consumption, total_delay

def My_12BitSubtractor(a, b,nstages=4,approx_until=1):
    # convert to binary
    a_bin = bin(a & ((1 << (nstages * 3)) - 1))[2:].zfill(nstages * 3)
    b_bin = bin(b & ((1 << (nstages * 3)) - 1))[2:].zfill(nstages * 3)
    # calculate 2's complement of b
    b_bin = ''.join('1' if bit == '0' else '0' for bit in b_bin)
    b_bin = bin(int(b_bin, 2) + 1)[2:].zfill(nstages * 3)

    # add a and 2's complement of b
    result,energy ,delay= My_12BitAdder(int(a_bin, 2), int(b_bin, 2),approx_until)

    return result, energy, delay

def My_12BitMultiplier(a, b, approx_until=1,nstages=4):
    # Convert inputs to two's complement representation
    a = a if a >= 0 else pow(2,nstages*3) + a
    b = b if b >= 0 else pow(2,nstages*3) + b

    total_result = 0
    total_energy_consumption = 0
    total_delay = 0
    
    for _ in range(b):

        total_result,energy,delay = My_12BitAdder(total_result,a,approx_until,nstages=nstages)
        total_energy_consumption += energy
        total_delay += delay

    # Prevent overflow
    total_result = total_result if total_result < pow(2,nstages*3) else total_result - pow(2,nstages*3)

    return total_result, total_energy_consumption, total_delay

# Generate Numpy Multiplier array
array = np.zeros((256,256))

def calculate_multiplier(i, j):
    array[i+128,j+128],_,_= My_12BitMultiplier(i,j,nstages=5,approx_until=3)
    print(i,j,array[i+128,j+128])
    return array[i+128,j+128]

def generate_array():
    Parallel(n_jobs=-1)(delayed(calculate_multiplier)(i, j) for i in range(-128,128) for j in range(-128,-128))
    return array

array = generate_array()  
#np.save('multiplier_table_neu.npy', array)

print(My_12BitMultiplier(128,128,nstages=5,approx_until=0))