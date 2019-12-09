from models import *

class BitHandler:

    def __init__(self,parity,bits):
        self.parity = parity
        self.recived = bits
        self.bits = self.create_new_structure(bits)
        self.error = self.compare_bits()

    def create_new_structure(self, bits):

        new_frase = []
        exp = 0
        while len(bits) > 0:

            if (len(new_frase)) == (2**exp - 1):
                new_frase.append(ParityBit(bool(int(bits[0]))))
                exp += 1
                bits = bits[1:]
            else :
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

    def compare_bits(self):
        error_bits = []
        for i in range(len(self.bits)):
            if self.bits[i] != self.recived[i]:
                error_bits.append(i+1)

        if not error_bits:
            return "there is no error in the data that was entered"

        error = sum(error_bits)

        if error > len(self.bits):
            return "the algorithm can`t fint the error"
        else :
            return "there is an error at the bit {:d}".format(error)


if __name__ == '__main__':
    main()
