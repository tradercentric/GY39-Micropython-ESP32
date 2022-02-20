from machine import Pin, SoftI2C

MCU_I2C_ADDR = 0X5b

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

h_lux_h = int.from_bytes(i2c.readfrom_mem(MCU_I2C_ADDR, 0x00, 1), 'big', False)
h_lux_l = int.from_bytes(i2c.readfrom_mem(MCU_I2C_ADDR, 0x01, 1), 'big', False)
l_lux_h = int.from_bytes(i2c.readfrom_mem(MCU_I2C_ADDR, 0x02, 1), 'big', False)
l_lux_l = int.from_bytes(i2c.readfrom_mem(MCU_I2C_ADDR, 0x03, 1), 'big', False)
lux = ((h_lux_h << 24) | (h_lux_l << 16) | (l_lux_h << 8) | l_lux_l) / 100
print(f'lux = {lux} lux')

t_h = int.from_bytes(i2c.readfrom_mem(MCU_I2C_ADDR, 0x04, 1), 'big', False)
t_l = int.from_bytes(i2c.readfrom_mem(MCU_I2C_ADDR, 0x05, 1), 'big', False)
temperature = ((t_h << 8) | t_l) / 100
print(f'temperature = {temperature} c')

h_p_h = int.from_bytes(i2c.readfrom_mem(MCU_I2C_ADDR, 0x06, 1), 'big', False)
h_p_l = int.from_bytes(i2c.readfrom_mem(MCU_I2C_ADDR, 0x07, 1), 'big', False)
l_p_h = int.from_bytes(i2c.readfrom_mem(MCU_I2C_ADDR, 0x08, 1), 'big', False)
l_p_l = int.from_bytes(i2c.readfrom_mem(MCU_I2C_ADDR, 0x09, 1), 'big', False)
pressure = ((h_p_h << 24) | (h_p_l << 16) | (l_p_h << 8) | l_p_l) / 100
print(f'pressure = {pressure} pa')

hum_h = int.from_bytes(i2c.readfrom_mem(MCU_I2C_ADDR, 0x0a, 1), 'big', False)
hum_l = int.from_bytes(i2c.readfrom_mem(MCU_I2C_ADDR, 0x0b, 1), 'big', False)
humidity = ((hum_h << 8) | hum_l) / 100
print(f'humidity = {humidity} %')

e_h = int.from_bytes(i2c.readfrom_mem(MCU_I2C_ADDR, 0x0c, 1), 'big', False)
e_l = int.from_bytes(i2c.readfrom_mem(MCU_I2C_ADDR, 0x0d, 1), 'big', False)
elevation = ((e_h << 8) | e_l)
print(f'elevation = {elevation} m')
