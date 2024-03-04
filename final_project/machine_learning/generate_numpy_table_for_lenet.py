import numpy as np
#Generate Numpy Multiplier array

def My_16BitMultiplier(a, b, approx_until=3):
     # Convert inputs to two's complement representation
    a = a if a >= 0 else 65536 + a
    b = b if b >= 0 else 65536 + b

    result = 0
    total_energy_consumption = 0
    for _ in range(b):
        result, energy_consumption = My_16BitAdder(result, a, approx_until)
        total_energy_consumption += energy_consumption

    # Prevent overflow
    result = result if result <= 65535 else result - 65536

    # Check if result is negative and revert 2's complement
    if result & (1 << 15):
        result = -(65536 - result)

    return result, total_energy_consumption

def My_16BitAdder(a,b,approx_until=3):
    # convert to binary
    a_bin, b_bin = bin(a)[2:], bin(b)[2:]

    #reverse order of bytes for the adder
    rev_a , rev_b = list(a_bin[::-1]), list(b_bin[::-1])
    
    rev_a = rev_a + max(0, len(rev_b)-len(rev_a)) * [0]
    rev_b = rev_b + max(0, len(rev_a)-len(rev_b)) * [0]

    carry_over  = 0
    total_sum   = 0

    total_energy_consumption = 0

    #we want to do a bitwise addition
    for index, (bit1, bit2) in enumerate( zip(rev_a, rev_b) ):

        if index < approx_until:
            #use approx_adder
            sum_element, carry_over , _energy = ApproxAdder(int(bit1), int(bit2), int(carry_over) ) 
        else:
            #use exact_adder
            sum_element, carry_over, _energy = ExactAdder(int(bit1), int(bit2), int(carry_over) )
            
        total_sum += pow(2,index)*sum_element
        total_energy_consumption += _energy

    total_sum += pow(2,index+1)*carry_over

    # If there is an overflow, ignore it
    if total_sum >= 65536:
        total_sum -= 65536
    return total_sum, total_energy_consumption


def integer_sqrt(n: int) -> int:
    assert n >= 0, "sqrt works for only non-negative inputs"
    if n < 2:
        return n
    # Recursive call:
    small_cand = integer_sqrt(n >> 2) << 1
    large_cand = small_cand + 1
    if large_cand * large_cand > n:
        return small_cand
    else:
        return large_cand

def ApproxAdder(a, b, c):
    if a==0 and b==0 and c==0:
        s=0
        c_out=0
        energy_consumption = 0
    elif a==0 and b==0 and c==1:
        s=1
        c_out=0
        energy_consumption = 0
    elif a==0 and b==1 and c==0:
        s=1
        c_out=0
        energy_consumption = 0
    elif a==0 and b==1 and c==1:
        s=0
        c_out=0
        energy_consumption = 0
    elif a==1 and b==0 and c==0:
        s=1
        c_out=0
        energy_consumption = 0
    elif a==1 and b==0 and c==1:
        s=0
        c_out=0
        energy_consumption = 0
    elif a==1 and b==1 and c==0:
        s=0
        c_out=1
        energy_consumption = 0
    elif a==1 and b==1 and c==1:
        s=1
        c_out=1
        energy_consumption = 0

    return s, c_out, energy_consumption

def ExactAdder(a, b, c):
    energy_consumption = 0
    if a==0 and b==0 and c==0:
        s=0
        c_out=0
        energy_consumption = 0
    elif a==0 and b==0 and c==1:
        s=1
        c_out=0
        energy_consumption = 0
    elif a==0 and b==1 and c==0:
        s=1
        c_out=0
        energy_consumption = 0
    elif a==0 and b==1 and c==1:
        s=0
        c_out=1
        energy_consumption = 0
    elif a==1 and b==0 and c==0:
        s=1
        c_out=0
        energy_consumption = 0
    elif a==1 and b==0 and c==1:
        s=0
        c_out=1
        energy_consumption = 0
    elif a==1 and b==1 and c==0:
        s=0
        c_out=1
        energy_consumption = 0
    elif a==1 and b==1 and c==1:
        s=1
        c_out=1
        energy_consumption = 0

    return s, c_out, energy_consumption


#Generate Numpy Multiplier array
array = np.zeros((256,256))
def generate_array():
    for i in range(-128,128):
        print("Row ", i)
        for j in range(-128,128):
            print("Column ", j)
            array[i+128,j+128],_= My_16BitMultiplier(i,j)
    return array


array = generate_array()  
np.save('multiplier_table.npy', array)