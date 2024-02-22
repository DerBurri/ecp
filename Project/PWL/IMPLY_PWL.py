v_0 = '0'
V_imply = '900m'

v_plus = '1'
v_minus = '-1'

class Memristor:

    charge_conf = ''
    switch_conf = ''

    def __init__(self, name, path='./'):
        self.name = name
        self.path = path
        self.charge_conf += '0u, 0\n'
        self.switch_conf += '0u, 0\n'
    
    def set_charge(self, time, step, charge):
        # write value to charge_conf
        self.charge_conf += str(time) + '.001u, ' + charge + '\n'
        self.charge_conf += str(time + step) + 'u, ' + charge + '\n'

    def set_switch(self, time, step, charge):
        # write value to switch_conf
        self.switch_conf += str(time) + '.001u, ' + charge + '\n'
        self.switch_conf += str(time + step) + 'u, ' + charge + '\n'

    def set_zero(self, time, step):
        # write pwl to set memristor to zero
        self.set_charge(time, step, v_minus)
        self.set_switch(time, step, v_plus)
    
    def set_condition(self, time, step):
        # write pwl to set memristor as condition for implication A --> X
        self.set_charge(time, step, V_imply)
        self.set_switch(time, step, v_plus)

    def set_consequence(self, time, step):
        # write pwl to set memristor as consequence for implication A --> X
        self.set_charge(time, step, v_plus)
        self.set_switch(time, step, v_plus)

    def set_idle(self, time, step):
        # write pwl to set memristor as idle (while other memristors are active)
        self.set_charge(time, step, v_0)
        self.set_switch(time, step, v_0)

    def print_conf_tocsv(self):
        # write charge_conf and switch_conf to csv files
        with open(self.path + self.name + '.csv', 'w') as f:
            print(self.charge_conf, file=f)
        with open(self.path + self.name + '_sw.csv', 'w') as f:
            print(self.switch_conf, file=f)

class SerialArchitecture:
    curr_time = 0
    
    def __init__(self, memristors, timestep=30):
        self.memristors = memristors
        self.timestep = timestep
    
    def getCurrentTime(self):
        return self.curr_time
    
    def set_zero(self, mem):
        # set selectet memristor to zero and all other memristors to idle
        for m in self.memristors:
            if m == mem:
                m.set_zero(self.curr_time, self.timestep)
            else:
                m.set_idle(self.curr_time, self.timestep)
        self.curr_time += self.timestep
    
    def set_one(self, mem):
        # set selectet memristor to one and all other memristors to idle (initialization as 1)
        for m in self.memristors:
            if m == mem:
                m.set_charge(self.curr_time, self.timestep, v_plus)
                m.set_switch(self.curr_time, self.timestep, v_plus)
            else:
                m.set_idle(self.curr_time, self.timestep)
        self.curr_time += self.timestep
    
    def imply(self, mem1, mem2):
        # set mem1 as condition and mem2 as consequence for implication mem1 --> mem2 and all other memristors to idle
        for m in self.memristors:
            if m == mem1:
                m.set_condition(self.curr_time, self.timestep)
            elif m == mem2:
                m.set_consequence(self.curr_time, self.timestep)
            else:
                m.set_idle(self.curr_time, self.timestep)
        self.curr_time += self.timestep
    
    def reset(self):
        # set all memristors to idle (close switches to prevent capacitance leakage)
        for m in self.memristors:
            m.set_idle(self.curr_time, self.timestep)
        self.curr_time += self.timestep
    
    def full_add(self, a, b, c, d, s1, s2, s3):
        ## Add Algorithm
        self.set_zero(s1) # s1 = 0
        self.set_zero(s2) # s2 = 0
        self.set_zero(s3) # s3 = 0

        # Stage 1: Calculate first level of carry and sum bits
        self.imply(a, s1)  # (a XOR b)
        self.imply(b, s1)  
        self.imply(a, b)   # (a AND b) -> carry_out to s2

        # Stage 2: Calculate second level carry and sum bits, taking previous carry into account 
        self.imply(c, s2)  # (c XOR s1)
        self.imply(s1, s2)
        self.imply(c, s1)  # (c AND s1) -> carry_out to s3 

        # Stage 3: Calculate third level carry and set sum, taking previous carry into account
        self.imply(d, s3)  # (d XOR s2)
        self.imply(s2, s3)
        self.imply(d, s2)  # (d AND s2) -> carry_out to c (output carry)

        # Stage 4: Set final sum bit
        self.imply(s3, a)   # Final sum to 'a'

        # Reset input memristors
        # This might be helpful in certain memristor models to prevent state drift
        self.set_zero(a)
        self.set_zero(b)
        self.set_zero(c)
        self.set_zero(d)

    def print_conf_tocsv(self):
        for m in self.memristors:
            m.print_conf_tocsv()

