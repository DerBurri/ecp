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
        ("000", "000", 0) : ("000", 0, 3551.72, 3),
        ("000", "000", 1) : ("001", 0, 3548.19, 3),
        ("000", "001", 0) : ("001", 0, 3640.16, 3),
        ("000", "001", 1) : ("010", 0, 3641.45, 3),
        ("000", "010", 0) : ("010", 0, 3572.25, 3),
        ("000", "010", 1) : ("011", 0, 3574.59, 3),
        ("000", "011", 0) : ("011", 0, 3601.3 , 3),
        ("000", "011", 1) : ("100", 0, 3598.35, 3),
        ("000", "100", 0) : ("100", 0, 3594.4 , 3),
        ("000", "100", 1) : ("101", 0, 3590.86, 3),
        ("000", "101", 0) : ("101", 0, 3683.04, 3),
        ("000", "101", 1) : ("110", 0, 3684.34, 3),
        ("000", "110", 0) : ("110", 0, 3615.07, 3),
        ("000", "110", 1) : ("111", 0, 3617.43, 3),
        ("000", "111", 0) : ("111", 0, 3644.06, 3),
        ("000", "111", 1) : ("000", 1, 3641.1 , 3),
        ("001", "000", 0) : ("001", 0, 3611.07, 3),
        ("001", "000", 1) : ("010", 0, 3607.71, 3),
        ("001", "001", 0) : ("010", 0, 3700.54, 3),
        ("001", "001", 1) : ("011", 0, 3701.81, 3),
        ("001", "010", 0) : ("011", 0, 3632.53, 3),
        ("001", "010", 1) : ("100", 0, 3634.89, 3),
        ("001", "011", 0) : ("100", 0, 3661.69, 3),
        ("001", "011", 1) : ("101", 0, 3658.71, 3),
        ("001", "100", 0) : ("101", 0, 3653.76, 3),
        ("001", "100", 1) : ("110", 0, 3650.4 , 3),
        ("001", "101", 0) : ("110", 0, 3743.41, 3),
        ("001", "101", 1) : ("111", 0, 3744.68, 3),
        ("001", "110", 0) : ("111", 0, 3675.35, 3),
        ("001", "110", 1) : ("000", 1, 3677.7 , 3),
        ("001", "111", 0) : ("000", 1, 3704.42, 3),
        ("001", "111", 1) : ("001", 1, 3701.46, 3),
        ("010", "000", 0) : ("010", 0, 3682.6 , 3),
        ("010", "000", 1) : ("011", 0, 3679.01, 3),
        ("010", "001", 0) : ("011", 0, 3769.36, 3),
        ("010", "001", 1) : ("100", 0, 3770.75, 3),
        ("010", "010", 0) : ("100", 0, 3747.66, 3),
        ("010", "010", 1) : ("101", 0, 3750.02, 3),
        ("010", "011", 0) : ("101", 0, 3775.71, 3),
        ("010", "011", 1) : ("110", 0, 3772.9 , 3),
        ("010", "100", 0) : ("110", 0, 3785.55, 3),
        ("010", "100", 1) : ("111", 0, 3781.98, 3),
        ("010", "101", 0) : ("111", 0, 3872.51, 3),
        ("010", "101", 1) : ("000", 1, 3873.88, 3),
        ("010", "110", 0) : ("000", 1, 3790.48, 3),
        ("010", "110", 1) : ("001", 1, 3792.83, 3),
        ("010", "111", 0) : ("001", 1, 3818.44, 3),
        ("010", "111", 1) : ("010", 1, 3815.64, 3),
        ("011", "000", 0) : ("011", 0, 3969.04, 3),
        ("011", "000", 1) : ("100", 0, 3660.23, 3),
        ("011", "001", 0) : ("100", 0, 3750.62, 3),
        ("011", "001", 1) : ("101", 0, 3752.01, 3),
        ("011", "010", 0) : ("101", 0, 3669.39, 3),
        ("011", "010", 1) : ("110", 0, 3671.75, 3),
        ("011", "011", 0) : ("110", 0, 3794.89, 3),
        ("011", "011", 1) : ("111", 0, 3694.62, 3),
        ("011", "100", 0) : ("111", 0, 3706.5 , 3),
        ("011", "100", 1) : ("000", 1, 3702.94, 3),
        ("011", "101", 0) : ("000", 1, 3793.52, 3),
        ("011", "101", 1) : ("001", 1, 3794.89, 3),
        ("011", "110", 0) : ("001", 1, 3712.2 , 3),
        ("011", "110", 1) : ("010", 1, 3714.56, 3),
        ("011", "111", 0) : ("010", 1, 3740.15, 3),
        ("011", "111", 1) : ("011", 1, 3737.35, 3),
        ("100", "000", 0) : ("100", 0, 3668.93, 3),
        ("100", "000", 1) : ("101", 0, 3665.54, 3),
        ("100", "001", 0) : ("101", 0, 3758.4 , 3),
        ("100", "001", 1) : ("110", 0, 3759.66, 3),
        ("100", "010", 0) : ("110", 0, 3690.38, 3),
        ("100", "010", 1) : ("111", 0, 3692.74, 3),
        ("100", "011", 0) : ("111", 0, 3719.52, 3),
        ("100", "011", 1) : ("000", 1, 3716.58, 3),
        ("100", "100", 0) : ("000", 1, 3711.6 , 3),
        ("100", "100", 1) : ("001", 1, 3708.24, 3),
        ("100", "101", 0) : ("001", 1, 3801.27, 3),
        ("100", "101", 1) : ("010", 1, 3802.55, 3),
        ("100", "110", 0) : ("010", 1, 3733.19, 3),
        ("100", "110", 1) : ("011", 1, 3735.56, 3),
        ("100", "111", 0) : ("011", 1, 3762.26, 3),
        ("100", "111", 1) : ("100", 1, 3759.31, 3),
        ("101", "000", 0) : ("101", 0, 3096.8 , 3),
        ("101", "000", 1) : ("110", 0, 3587.29, 3),
        ("101", "001", 0) : ("110", 0, 3680.14, 3),
        ("101", "001", 1) : ("111", 0, 3681.8 , 3),
        ("101", "010", 0) : ("111", 0, 3612.1 , 3),
        ("101", "010", 1) : ("000", 1, 3614.46, 3),
        ("101", "011", 0) : ("000", 1, 3641.27, 3),
        ("101", "011", 1) : ("001", 1, 3638.32, 3),
        ("101", "100", 0) : ("001", 1, 3633.33, 3),
        ("101", "100", 1) : ("010", 1, 3629.94, 3),
        ("101", "101", 0) : ("010", 1, 3723   , 3),
        ("101", "101", 1) : ("011", 1, 3724.28, 3),
        ("101", "110", 0) : ("011", 1, 3654.91, 3),
        ("101", "110", 1) : ("100", 1, 3657.28, 3),
        ("101", "111", 0) : ("100", 1, 3684.01, 3),
        ("101", "111", 1) : ("101", 1, 3681.04, 3),
        ("110", "000", 0) : ("110", 0, 3722.47, 3),
        ("110", "000", 1) : ("111", 0, 3718.9 , 3),
        ("110", "001", 0) : ("111", 0, 3809.25, 3),
        ("110", "001", 1) : ("000", 1, 3810.61, 3),
        ("110", "010", 0) : ("000", 1, 3727.26, 3),
        ("110", "010", 1) : ("001", 1, 3729.61, 3),
        ("110", "011", 0) : ("001", 1, 3755.33, 3),
        ("110", "011", 1) : ("010", 1, 3752.51, 3),
        ("110", "100", 0) : ("010", 1, 3765.15, 3),
        ("110", "100", 1) : ("011", 1, 3761.61, 3),
        ("110", "101", 0) : ("011", 1, 3852.12, 3),
        ("110", "101", 1) : ("100", 1, 3853.48, 3),
        ("110", "110", 0) : ("100", 1, 3770.08, 3),
        ("110", "110", 1) : ("101", 1, 4125.72, 3),
        ("110", "111", 0) : ("101", 1, 3798.07, 3),
        ("110", "111", 1) : ("110", 1, 3795.24, 3),
        ("111", "000", 0) : ("111", 0, 3643.4 , 3),
        ("111", "000", 1) : ("000", 1, 3639.85, 3),
        ("111", "001", 0) : ("000", 1, 3730.23, 3),
        ("111", "001", 1) : ("001", 1, 3731.62, 3),
        ("111", "010", 0) : ("001", 1, 3648.98, 3),
        ("111", "010", 1) : ("010", 1, 3651.33, 3),
        ("111", "011", 0) : ("010", 1, 3677.03, 3),
        ("111", "011", 1) : ("011", 1, 3674.22, 3),
        ("111", "100", 0) : ("011", 1, 3686.11, 3),
        ("111", "100", 1) : ("100", 1, 3682.53, 3),
        ("111", "101", 0) : ("100", 1, 3773.11, 3),
        ("111", "101", 1) : ("101", 1, 3774.49, 3),
        ("111", "110", 0) : ("101", 1, 3691.8 , 3),
        ("111", "110", 1) : ("110", 1, 3694.16, 3),
        ("111", "111", 0) : ("110", 1, 3719.77, 3),
        ("111", "111", 1) : ("111", 1, 3716.96, 3),
    }

    return truth_table[a, b, c]

# ## Approximate Adder Function
#
# The output result deviates from the exact solution.
#

# In[31]:

def approxAdder(a, b, c):
    truth_table = {
        ("000", "000", 0) : ("000", 0, 3524.43, 3),
        ("000", "000", 1) : ("001", 0, 3523.25, 3),
        ("000", "001", 0) : ("001", 0, 3550.87, 3),
        ("000", "001", 1) : ("010", 0, 3547.47, 3),
        ("000", "010", 0) : ("010", 0, 3524.43, 3),
        ("000", "010", 1) : ("011", 0, 3523.25, 3),
        ("000", "011", 0) : ("011", 0, 3550.87, 3),
        ("000", "011", 1) : ("100", 0, 3547.47, 3),
        ("000", "100", 0) : ("100", 0, 3569.85, 3),
        ("000", "100", 1) : ("101", 0, 3568.76, 3),
        ("000", "101", 0) : ("101", 0, 3595.61, 3),
        ("000", "101", 1) : ("110", 0, 3592.36, 3),
        ("000", "110", 0) : ("110", 0, 3569.85, 3),
        ("000", "110", 1) : ("111", 0, 3568.76, 3),
        ("000", "111", 0) : ("111", 0, 3595.61, 3),
        ("000", "111", 1) : ("000", 0, 3592.36, 3),
        ("001", "000", 0) : ("001", 0, 3414.19, 3),
        ("001", "000", 1) : ("010", 0, 3412.8 , 3),
        ("001", "001", 0) : ("010", 0, 3441.17, 3),
        ("001", "001", 1) : ("011", 0, 3437.65, 3),
        ("001", "010", 0) : ("011", 0, 3414.19, 3),
        ("001", "010", 1) : ("100", 0, 3412.8 , 3),
        ("001", "011", 0) : ("100", 0, 3441.17, 3),
        ("001", "011", 1) : ("101", 0, 3437.65, 3),
        ("001", "100", 0) : ("101", 0, 3459.54, 3),
        ("001", "100", 1) : ("110", 0, 3458.24, 3),
        ("001", "101", 0) : ("110", 0, 3485.88, 3),
        ("001", "101", 1) : ("111", 0, 3482.48, 3),
        ("001", "110", 0) : ("111", 0, 3459.54, 3),
        ("001", "110", 1) : ("000", 0, 3458.24, 3),
        ("001", "111", 0) : ("000", 0, 3485.88, 3),
        ("001", "111", 1) : ("001", 0, 3482.48, 3),
        ("010", "000", 0) : ("010", 0, 3461.63, 3),
        ("010", "000", 1) : ("011", 0, 3460.38, 3),
        ("010", "001", 0) : ("011", 0, 3488.08, 3),
        ("010", "001", 1) : ("100", 0, 3484.6 , 3),
        ("010", "010", 0) : ("100", 1, 3461.63, 3),
        ("010", "010", 1) : ("101", 1, 3460.38, 3),
        ("010", "011", 0) : ("101", 1, 3488.08, 3),
        ("010", "011", 1) : ("110", 1, 3484.6 , 3),
        ("010", "100", 0) : ("110", 0, 3507.03, 3),
        ("010", "100", 1) : ("111", 0, 3505.88, 3),
        ("010", "101", 0) : ("111", 0, 3532.81, 3),
        ("010", "101", 1) : ("000", 0, 3529.48, 3),
        ("010", "110", 0) : ("000", 1, 3507.03, 3),
        ("010", "110", 1) : ("001", 1, 3505.88, 3),
        ("010", "111", 0) : ("001", 1, 3532.81, 3),
        ("010", "111", 1) : ("010", 1, 3529.48, 3),
        ("011", "000", 0) : ("011", 0, 3141.21, 3),
        ("011", "000", 1) : ("100", 0, 3144.42, 3),
        ("011", "001", 0) : ("100", 0, 3376.36, 3),
        ("011", "001", 1) : ("101", 0, 3372.84, 3),
        ("011", "010", 0) : ("101", 1, 3349.38, 3),
        ("011", "010", 1) : ("110", 1, 3348   , 3),
        ("011", "011", 0) : ("110", 1, 3376.36, 3),
        ("011", "011", 1) : ("111", 1, 3372.84, 3),
        ("011", "100", 0) : ("111", 0, 3394.73, 3),
        ("011", "100", 1) : ("000", 0, 3393.44, 3),
        ("011", "101", 0) : ("000", 0, 3421.07, 3),
        ("011", "101", 1) : ("001", 0, 3417.67, 3),
        ("011", "110", 0) : ("001", 1, 3394.73, 3),
        ("011", "110", 1) : ("010", 1, 3393.44, 3),
        ("011", "111", 0) : ("010", 1, 3421.07, 3),
        ("011", "111", 1) : ("011", 1, 3417.67, 3),
        ("100", "000", 0) : ("100", 0, 3504   , 3),
        ("100", "000", 1) : ("101", 0, 3502.82, 3),
        ("100", "001", 0) : ("101", 0, 3530.44, 3),
        ("100", "001", 1) : ("110", 0, 3527.03, 3),
        ("100", "010", 0) : ("110", 0, 3504   , 3),
        ("100", "010", 1) : ("111", 0, 3502.82, 3),
        ("100", "011", 0) : ("111", 0, 3530.44, 3),
        ("100", "011", 1) : ("000", 0, 3527.03, 3),
        ("100", "100", 0) : ("000", 0, 3549.41, 3),
        ("100", "100", 1) : ("001", 0, 3548.32, 3),
        ("100", "101", 0) : ("001", 0, 3575.18, 3),
        ("100", "101", 1) : ("010", 0, 3571.91, 3),
        ("100", "110", 0) : ("010", 0, 3549.41, 3),
        ("100", "110", 1) : ("011", 0, 3548.32, 3),
        ("100", "111", 0) : ("011", 0, 3575.18, 3),
        ("100", "111", 1) : ("100", 0, 3571.91, 3),
        ("101", "000", 0) : ("101", 0, 3393.75, 3),
        ("101", "000", 1) : ("110", 0, 3392.39, 3),
        ("101", "001", 0) : ("110", 0, 3420.57, 3),
        ("101", "001", 1) : ("111", 0, 3417.22, 3),
        ("101", "010", 0) : ("111", 0, 3393.75, 3),
        ("101", "010", 1) : ("000", 0, 3374.67, 3),
        ("101", "011", 0) : ("000", 0, 3420.74, 3),
        ("101", "011", 1) : ("001", 0, 3417.22, 3),
        ("101", "100", 0) : ("001", 0, 3439.11, 3),
        ("101", "100", 1) : ("010", 0, 3437.82, 3),
        ("101", "101", 0) : ("010", 0, 3465.42, 3),
        ("101", "101", 1) : ("011", 0, 3462.04, 3),
        ("101", "110", 0) : ("011", 0, 3439.11, 3),
        ("101", "110", 1) : ("100", 0, 3437.82, 3),
        ("101", "111", 0) : ("100", 0, 3465.42, 3),
        ("101", "111", 1) : ("101", 0, 3462.04, 3),
        ("110", "000", 0) : ("110", 0, 3437.23, 3),
        ("110", "000", 1) : ("111", 0, 3436.06, 3),
        ("110", "001", 0) : ("111", 0, 3463.69, 3),
        ("110", "001", 1) : ("000", 0, 3460.25, 3),
        ("110", "010", 0) : ("000", 1, 3437.23, 3),
        ("110", "010", 1) : ("001", 1, 3436.06, 3),
        ("110", "011", 0) : ("001", 1, 3480.91, 3),
        ("110", "011", 1) : ("010", 1, 3460.25, 3),
        ("110", "100", 0) : ("010", 0, 3482.64, 3),
        ("110", "100", 1) : ("011", 0, 3481.56, 3),
        ("110", "101", 0) : ("011", 0, 3508.42, 3),
        ("110", "101", 1) : ("100", 0, 3505.15, 3),
        ("110", "110", 0) : ("100", 1, 3482.64, 3),
        ("110", "110", 1) : ("101", 1, 3481.56, 3),
        ("110", "111", 0) : ("101", 1, 3508.42, 3),
        ("110", "111", 1) : ("110", 1, 3505.15, 3),
        ("111", "000", 0) : ("111", 0, 3328.96, 3),
        ("111", "000", 1) : ("000", 0, 3327.59, 3),
        ("111", "001", 0) : ("000", 0, 3355.95, 3),
        ("111", "001", 1) : ("001", 0, 3352.43, 3),
        ("111", "010", 0) : ("001", 1, 3328.96, 3),
        ("111", "010", 1) : ("010", 1, 3327.59, 3),
        ("111", "011", 0) : ("010", 1, 3355.95, 3),
        ("111", "011", 1) : ("011", 1, 3352.43, 3),
        ("111", "100", 0) : ("011", 0, 3374.32, 3),
        ("111", "100", 1) : ("100", 0, 3373.02, 3),
        ("111", "101", 0) : ("100", 0, 3400.63, 3),
        ("111", "101", 1) : ("101", 0, 3397.26, 3),
        ("111", "110", 0) : ("101", 1, 3374.32, 3),
        ("111", "110", 1) : ("110", 1, 3373.02, 3),
        ("111", "111", 0) : ("110", 1, 3400.63, 3),
        ("111", "111", 1) : ("111", 1, 3397.26, 3),
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
