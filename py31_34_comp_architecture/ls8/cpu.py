"""CPU functionality."""

import sys

"""Op Code Constants"""
NOP = 0b00000000
HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
ADD = 0b10100000
MUL = 0b10100010


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 7 + [0xF4]
        self.ram = [0] * 256
        self.pc = 0
        self.fl = 0
        self.halted = True
        self.disp = {
            NOP: self._nop,
            HLT: self._hlt,
            LDI: self._ldi,
            PRN: self._prn,
            ADD: self._add,
            MUL: self._mul,
        }

    def _nop():
        pass

    def _hlt(self):
        self.halted = True

    def _ldi(self, reg_num, reg_val):
        self.reg[reg_num] = reg_val

    def _prn(self, reg_num):
        print(self.reg[reg_num])

    def _add(self, reg_a, reg_b):
        self.reg[reg_a] += self.reg[reg_b]

    def _mul(self, reg_a, reg_b):
        self.reg[reg_a] *= self.reg[reg_b]

    def load(self):
        """Load a program into memory."""

        if len(sys.argv) != 2:
            print("Usage: ls8.py prog_name")
            sys.exit()

        address = 0

        try:
            with open("examples/" + sys.argv[1] + ".ls8") as f:
                for line in f:
                    line = line.strip()

                    if line == "" or line[0] == "#":
                        continue

                    str_val = line.split("#")[0]

                    try:
                        value = int(str_val, 2)
                    except ValueError:
                        print(f"Invalid number: {str_val}")
                        sys.exit()

                    self.ram[address] = value
                    address += 1

        except FileNotFoundError:
            print(f"File not found: {sys.argv[1]}")
            sys.exit()

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == ADD:
            self.reg[reg_a] += self.reg[reg_b]

        elif op == MUL:
            self.reg[reg_a] *= self.reg[reg_b]

        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(
            f"TRACE: %02X | %02X %02X %02X |"
            % (
                self.pc,
                # self.fl,
                # self.ie,
                self.ram_read(self.pc),
                self.ram_read(self.pc + 1),
                self.ram_read(self.pc + 2),
            ),
            end="",
        )

        for i in range(8):
            print(" %02X" % self.reg[i], end="")

        print()

    def ram_write(self, value, address):
        self.ram[address] = value

    def ram_read(self, address):
        return self.ram[address]

    def run(self):
        """Run the CPU."""
        self.halted = False
        while not self.halted:
            ir = self.ram[self.pc]
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            # to be safe, use the bitwise `AND` to
            # mask bits we don't care about before right shift
            num_operands = (ir & 0b11000000) >> 6

            if num_operands == 0:
                self.disp[ir]()

            elif num_operands == 1:
                self.disp[ir](operand_a)

            elif num_operands == 2:
                self.disp[ir](operand_a, operand_b)

            else:
                print(f"Unknown op_code: {ir}")
                sys.exit()

            # add 1 for the op code
            instruction_len = num_operands + 1
            # increment the prog_counter dynamically
            self.pc += instruction_len
