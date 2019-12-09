from models import *

class BitHandler:

    def __init__(self,parity,bits):
        self.parity = parity
        self.bits = self.create_new_structure(bits)

    def create_new_structure(self, bits):

        new_frase = [ParityBit(),ParityBit()]
        exp = 2
        while len(bits) > 0:

            if (len(new_frase)) == (2**exp - 1):
                new_frase.append(ParityBit())
                exp += 1


            bit = Bit(bool(int(bits[0])))

            new_frase.append(bit)

            position = len(new_frase)

            frase = bin(position)[2:][::-1]
            aux = 0

            for num in frase:
                if int(num) :
                    new_frase[2**aux - 1].add_bit(bit)
                aux += 1

            aux = 0

            bits = bits[1:]

        for bit in new_frase:
            try :
                bit.calculate_value(self.parity)
            except:
                pass

        return  "".join(map(lambda x: str(x), new_frase))

if __name__ == '__main__':
    main()
