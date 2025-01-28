# import machine
# import picozero
from gc import mem_free
 
class DataGetter:
    def __init__(self):
        # self.ldr_pin = machine.ADC(machine.Pin(pin))
        self.count = 0
        print(mem_free())
        
        # no space for full csv file, so only kept altitude data
        with open('sample_data_trimmed2.csv') as file:
            print(mem_free())
            text = file.read()
            print(mem_free())
            self.lines = text.splitlines()
            print(mem_free())

    def get_data(self):
        # return round(self.get_raw_value()/65535*100,2)
        # volt = (3.3/65535) * self.get_raw_value()
        # temperature = 27 - (volt - 0.706)/0.001721
        # return temperature
        self.count += 1
        return self.lines[self.count] if self.count < len(self.lines) else 0
