"""
Module contains functions to symbolically execute REIL instructions

Top Level Interface:
state.step(): symbollically execute a single instruction on the state
state.execute(): symbolically execute basic block on the state
"""

from handlers import *
from reil.definitions import *

class state:
    def __init__(self):
        """
        Class to represent a single symbolic state of program

        Attributes:
        #registers = dictionary of Z3 BitVecRef/BitVecVal
        #temp_registers = dictionary of Z3 BitVecRef/BitVecVal
        #memory = dictionary of Z3 BitVecRef/BitVecVal
        #Solver: allows for solving by using z3, might be refactored to elsewhere

        """
        self.registers = {} 
        self.temp_registers = {} #Temporary registers used by REIL
        self.memory = {}
        self.solver = Solver()

    
    def update_reg(self,reg, expr):
        """
        If register reg exists in state, update it, if not, add it
        Expr is a Z3 bit vector
        Updates state
        """
        if reg.name in self.registers:
            self.registers[reg.name] = expr
        else:
            self.registers.update({reg.name:expr})

    def update_temp(self,reg, expr):
        """Update temporary register reg to expr """
        if reg.name in self.temp_registers:
            self.temp_registers[reg.name] = expr
        else:
            self.temp_registers.update({reg.name:expr})


    def update_mem(self,addr, expr):
        """Update memory at addr to expr """
        if str(addr.value) in self.memory:
            self.memory[str(addr.value)] = expr
        else:
            self.memory.update({str(addr.value):expr})



    def update_state(self,output,expr):
        """Update state variable output refers to"""
        if type(output) == RegisterOperand:
            self.update_reg(output, expr)
        elif type(output) == TemporaryOperand:
            self.update_temp(output, expr)
        elif type(output) == ImmediateOperand:
            self.update_mem(output, expr)
        

    def fetch_reg(self, reg):
        """Returns register if it exists, else returns fresh BitVec"""
        if reg.name in self.registers:
            return self.registers[reg.name]
        else:
            return BitVec(reg.name,reg.size)

    def fetch_temp(self, reg):
        """Returns temporary register if it exists, else returns fresh BitVec"""
        if reg.name in self.temp_registers:
            return self.temp_registers[reg.name]
        else:
            return BitVec(reg.name,reg.size)

    def fetch_mem(self, addr):
        """Returns memory cell if it exists, else returns fresh BitVec"""
        if addr in self.memory:
            return self.memory[str(addr.value)]
        else:
            return BitVec(str(addr.value), addr.size)

    

    def fetch_op_mem(self, op):
        """
        Fetch operand from current state, interpret immediate values as memory accesses

        Immediate values are interpreted as memory accesses only in ldm (load from memory)
        """
        if type(op) == RegisterOperand:
            return self.fetch_reg(op)
        elif type(op) == TemporaryOperand:
            return self.fetch_temp(op)
        elif type(op) == ImmediateOperand:
            return self.fetch_mem(op)
        return 0

    def fetch_op_lit(self, op):
        """
        Fetch operand from current state, interpret immediate values as literals

        This is called in all handlers but ldm(load from memory)
        """
        if type(op) == RegisterOperand:
            return self.fetch_reg(op)
        elif type(op) == TemporaryOperand:
            return self.fetch_temp(op)
        elif type(op) == ImmediateOperand:
            return BitVecVal(op.value, op.size)
        return 0


    def step(self, il_ins):
        """Symbolically execute a single REIL instruction """
        ins_handler[il_ins.opcode](self, il_ins)


    def execute(self, instructions):
        """
        Execute a basic block of instructions over the state
        Alters the state of the state object (self)
        """
        for ins in instructions:
            for il_ins in ins.il_instructions:
                self.step(il_ins)










    
                

