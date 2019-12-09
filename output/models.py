class Bit:

    def __init__ (self,value):
        self.value = value

    def __str__(self):
        return "1" if self.value else "0"

class ParityBit(Bit):

    def __init__(self,value = None):
        super().__init__(value)
        self.related_bits = []

    def add_bit(self,bit):
        self.related_bits.append(bit)

    def calculate_value(self,parity):
        value = parity

        for bit in self.related_bits:
            if bit.value == True:
                value = not value

        self.value = value

        return value

if __name__ == '__main__':
    main()
