#!/usr/bin/env python3

import csv

def binary_adder_truth_table():
    rows = []
    python_format = []
    # Header row
    header = ['A2', 'A1', 'A0', 'B2', 'B1', 'B0', 'Cin', 'S2', 'S1', 'S0', 'Cout', 'Energy', 'Proc_time']
    rows.append(header)

    for a2 in range(2):
        for a1 in range(2):
            for a0 in range(2):
                for b2 in range(2):
                    for b1 in range(2):
                        for b0 in range(2):
                            for carry_in in range(2):
                                # Convert integers to binary strings
                                a_bin = format(a2, 'b') + format(a1, 'b') + format(a0, 'b')
                                b_bin = format(b2, 'b') + format(b1, 'b') + format(b0, 'b')
                                sum_out = bin(int(a_bin, 2) + int(b_bin, 2) + carry_in)[2:]
                                # Pad sum_out with leading zeros if necessary
                                sum_out = sum_out.zfill(3)
                                # Extract individual bits of sum_out
                                sum_out2, sum_out1, sum_out0 = sum_out[-3], sum_out[-2], sum_out[-1]
                                # Calculate carry_out
                                carry_out = '1' if len(sum_out) > 3 else '0'
                                # Append row to the table
                                rows.append([a2, a1, a0, b2, b1, b0, carry_in, sum_out2, sum_out1, sum_out0, carry_out, 200, 1.3])
                                python_format.append("(\"{}{}{}\", \"{}{}{}\", {}) : (\"{}{}{}\", {}, {}, {}),\n".format(a2,a1,a0, b2,b1,b0, carry_in, sum_out2, sum_out1, sum_out0, carry_out, 200, 1.3))

    return rows,python_format

def main():
    truth_table, py_table = binary_adder_truth_table()
    with open('raw_truth_table.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(truth_table)

    with open('py_truth_table.txt', mode='w') as file:
        file.writelines(py_table)

if __name__ == "__main__":
    main()
