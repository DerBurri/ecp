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
    
    def full_add(self, a, b, c, s1, s2):
        ## Add Algorithm
        self.set_zero(s1) # s1 = 0
        self.set_zero(s2) # s2 = 0

        # a -> s1
        self.imply(a, s1) 
        # b -> s2
        self.imply(b, s2)
        # s1 -> b
        self.imply(s1, b)
        # a -> s2
        self.imply(a, s2)
        # a = 0
        self.set_zero(a)
        # b -> a
        self.imply(b, a)
        # s2 ->  a
        self.imply(s2, a)

        # s1 = 0
        self.set_zero(s1)
        # c -> s1
        self.imply(c, s1)
        # s2 -> c
        self.imply(s2, c)
        # a -> s1
        self.imply(a, s1)

        # a = 0
        self.set_zero(a)
        # s1 -> a
        self.imply(s1, a)

        # s2 = 0
        self.set_zero(s2)
        # c -> s2
        self.imply(c, s2)
        # b -> s2
        self.imply(b, s2)
        # b -> c
        self.imply(b, c)
        # c -> a # sum
        self.imply(c, a)

        # c = 0
        self.set_zero(c)
        # s2 -> c # carry
        self.imply((a and b), c)
    
    def print_conf_tocsv(self):
        for m in self.memristors:
            m.print_conf_tocsv()
