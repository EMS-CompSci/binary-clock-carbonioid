from datetime import datetime
from datetime import time
import math

class Clock:
    def __init__(self):
        pass

    def denary_to_binary_bits(self, num, pad=8):
        """
        Convert `num` to a list of binary bits and pad with `pad` zeroes (so that the total length of the list is `pad`)
        """
        # Avoid math domain error by ending early on num=0
        if num == 0:
            return [0]*pad
        
        # Get number of bits we need
        msb = math.floor(math.log2(num))
        bits = []

        # Convert value to binary
        current_value = num
        for i in range(msb, -1, -1):
            val = 2**i
            if current_value // val >= 1:
                bits.append(1)
                current_value -= val
            else:
                bits.append(0)
        
        # Pad value
        if len(bits) < pad:
            bits = ([0]*(pad-len(bits)))+bits
        
        return bits

    def time_as_binary(self):
        """
        Convert the hour, minute and second values to binary and return each of the tens and units column as a 
        separate values.

        Returns:
            List[List[List[int, List[int]]]] ([[hours_tens, hours_ones], [minutes_tens, minutes_ones], ...])
        """

        t = datetime.now()
        time_values = t.hour, t.minute, t.second

        binary_values = []
        for value in time_values:
            tens = value // 10
            units = value % 10
            binary_values.append([self.denary_to_binary_bits(tens, pad=4), self.denary_to_binary_bits(units, pad=4)])
        
        # Convert to binary and pad with zeroes
        return binary_values
