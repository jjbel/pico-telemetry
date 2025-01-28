import machine
# import picozero
 
class DataGetter:
    def __init__(self):
        # self.ldr_pin = machine.ADC(machine.Pin(pin))
        self.count = 0
        
    def get_data(self):
        # return round(self.get_raw_value()/65535*100,2)
        # volt = (3.3/65535) * self.get_raw_value()
        # temperature = 27 - (volt - 0.706)/0.001721
        # return temperature
        self.count += 1
        return self.count
