import utime    # 导入时间控制库
import ujson    
import gc

from machine import I2C, Pin, SPI   # 导入I2C设备库
from machine import UART, Pin       # 导入machine库中的pin库
import st7789   # 导入屏幕设备库
import ahtx0    # 导入aht20库

import network  # 导入网络库依赖
from simple import MQTTClient   # 导入MQTT依赖

global flag     # 声明全局变量flag

# 连接网络
def connectWIFI():
    print('Connecting wifi...')     # 打印连接网络状态信息
    sta_wlan = network.WLAN(network.STA_IF)     # 设定站点模式
    sta_wlan.active(True)       # 传入激活参数
    sta_wlan.connect('fhe142', '18042475359', security=network.AUTH_PSK)    #设定网络信息
    while(sta_wlan.config() == '0.0.0.0'):  # 获取设备IP地址，判断网络是否连接
        utime.sleep(1)  # 未连接等待一秒重试
    print('Connected...')   # 连接成功打印信息

connectWIFI()   # 调用连接网络的方法


#mqtt配置
SERVER = '118.31.53.253'    # 输入mqtt服务器的地址
CLIENT_ID = 'wttw'          # 连入mqtt的设备名称
TOPIC1 = b'asks'            # waffle订阅的mqtt主题-请求
TOPIC2 = b'temp'            # waffle订阅的mqtt主题-温度
TOPIC3 = b'add'             # waffle订阅的mqtt主题-建议

def mqtt_callback(topic, msg):
    if len(msg) > 8:    # 判断接收到时间戳信息
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag     # 声明全局变量flag
        flag = 1001
    elif msg == b'true':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 1101
    elif msg == b'false':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 1102
    elif msg == b'17':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 17
    elif msg == b'18':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 18
    elif msg == b'19':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 19
    elif msg == b'20':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 20
    elif msg == b'21':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 21
    elif msg == b'22':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 22
    elif msg == b'23':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 23
    elif msg == b'24':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 24
    elif msg == b'25':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 25
    elif msg == b'26':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 26
    elif msg == b'27':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 27
    elif msg == b'28':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 28
    elif msg == b'29':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 29
    elif msg == b'30':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 30
    elif msg == b'115':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 115
    elif msg == b'113':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 113
    elif msg == b'111':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 111
    elif msg == b'112':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 112
    elif msg == b'131':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 131
    elif msg == b'132':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 132
    elif msg == b'101':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 101
    elif msg == b'102':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 102
    elif msg == b'126':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 126
    elif msg == b'1':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 1
    elif msg == b'2':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 2
    elif msg == b'3':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 3
    elif msg == b'4':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 4
    elif msg == b'5':
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))
        global flag
        flag = 5
    else:
        print('topic: {}'.format(topic))
        print('msg: {}'.format(msg))

client = MQTTClient(CLIENT_ID, SERVER)  # 实例化MQTT设备对象  
client.set_callback(mqtt_callback)      # 调用mqtt_callback方法
client.connect()
client.subscribe(TOPIC1)                # 订阅TOPIC1

# 收集环境温湿度并上传
i2c = I2C(0, sda=Pin(13), scl=Pin(14), freq=100000) # 实例化I2C对象，设定I2C0号组，13、14号银奖
sensor = ahtx0.AHT20(i2c)                           # 实例化传感器对象

uart=UART(1,baudrate=115200,parity=0,tx=Pin(0),rx=Pin(1),timeout=10)    # 实例化UART对象

pin5 = Pin(5, dir=Pin.IN,pull=Pin.PULL_DOWN)    # 实例化GPIO对象

spi = SPI(0, baudrate=40000000, polarity=1, phase=0, bits=8, endia=0, sck=Pin(6), mosi=Pin(8))  # 实例化SPI对象
display = st7789.ST7789(spi, 240, 240, reset=Pin(11, func=Pin.GPIO, dir=Pin.OUT), dc=Pin(7, func=Pin.GPIO, dir=Pin.OUT))    # 实例化屏幕设备对象
display.init()  # 初始化屏幕显示

while True:
    client.check_msg()  # 查看是否有数据传入,有的话就执行 mqtt_callback
    f = pin5.value()    # 读取GPIO电平
    print (f)
    if f == 0:  # 判断GPIO输入低电平时，响应关闭指令
        data18 = "\x68\x08\x00\xFF\x12\x01\x12\x16"
        uart.write(data18)
    if flag == 1001:    # 接收到温度请求的响应
        print('Temperature: ' + str(sensor.temperature))
        mesg = str(sensor.temperature)[0:5]     # 格式化温度数据
        display.fill(st7789.color565(0,0,0))    # 以黑色填充屏幕
        # 在屏幕上绘制温度数据
        display.draw_string(0, 0, 'Temp: %.2f' % (sensor.temperature), color=st7789.color565(66, 133, 244), bg=st7789.color565(66, 133, 244), size=3, vertical=False, rotate=st7789.ROTATE_0, spacing=1)
        print(mesg)
        client.publish(TOPIC2, mesg) #通过mqtt上传温度数据
        if sensor.temperature <= 25: #温度低于25摄氏度，进行温度控制提示
            adv = round(sensor.temperature,0)+1
            client.publish(TOPIC3,str(adv))
        else:
            client.publish(TOPIC3,"None")
    if  flag == 1101:   # 响应开启指令
        data18 = "\x68\x08\x00\xFF\x12\x00\x11\x16"
        uart.write(data18)
    if flag == 1102:    # 响应关闭指令
        data19 = "\x68\x08\x00\xFF\x12\x01\x12\x16"
        uart.write(data19)
    if flag == 17:      # 响应温度调节指令
        data21 = "\x68\x08\x00\xFF\x12\x03\x14\x16"
        uart.write(data21)
    if flag == 18:
        data21 = "\x68\x08\x00\xFF\x12\x04\x15\x16"
        uart.write(data21)
    if flag == 19:
        data21 = "\x68\x08\x00\xFF\x12\x05\x16\x16"
        uart.write(data21)
    if flag == 20:
        data21 = "\x68\x08\x00\xFF\x12\x06\x17\x16"
        uart.write(data21)
    if flag == 21:
        data21 = "\x68\x08\x00\xFF\x12\x07\x18\x16"
        uart.write(data21)
    if flag == 22:
        data21 = "\x68\x08\x00\xFF\x12\x08\x19\x16"
        uart.write(data21)
    if flag == 23:
        data21 = "\x68\x08\x00\xFF\x12\x09\x1A\x16"
        uart.write(data21)
    if flag == 24:
        data21 = "\x68\x08\x00\xFF\x12\x0A\x1B\x16"
        uart.write(data21)
    if flag == 25:
        data21 = "\x68\x08\x00\xFF\x12\x0B\x1C\x16"
        uart.write(data21)
    if flag == 26:
        data21 = "\x68\x08\x00\xFF\x12\x0C\x1D\x16"
        uart.write(data21)
    if flag == 27:
        data21 = "\x68\x08\x00\xFF\x12\x0D\x1E\x16"
        uart.write(data21)
    if flag == 28:
        data21 = "\x68\x08\x00\xFF\x12\x0E\x1F\x16"
        uart.write(data21)
    if flag == 29:
        data21 = "\x68\x08\x00\xFF\x12\x0F\x20\x16"
        uart.write(data21)
    if flag == 30:
        data21 = "\x68\x08\x00\xFF\x12\x10\x21\x16"
        uart.write(data21)
    if flag == 115:     # 响应风速模式调节指令
        data21 = "\x68\x08\x00\xFF\x12\x17\x28\x16"
        uart.write(data21)
    if flag == 113:
        data21 = "\x68\x08\x00\xFF\x12\x13\x24\x16"
        uart.write(data21)
    if flag == 112:
        data21 = "\x68\x08\x00\xFF\x12\x14\x25\x16"
        uart.write(data21)
    if flag == 111:
        data21 = "\x68\x08\x00\xFF\x12\x16\x27\x16"
        uart.write(data21)
    if flag == 131:     # 响应扫风开启指令
        data21 = "\x68\x08\x00\xFF\x12\x1E\x2F\x16"
        uart.write(data21)
    if flag == 132:     # 响应扫风关闭指令
        data21 = "\x68\x08\x00\xFF\x12\x1F\x30\x16"
        uart.write(data21)
    if flag == 101:     # 响应ECO-ON指令
        data21 = "\x68\x08\x00\xFF\x12\x11\x22\x16"
        uart.write(data21)
    if flag == 102:     # 响应ECO-OFF指令
        data21 = "\x68\x08\x00\xFF\x12\x12\x23\x16"
        uart.write(data21)
    if flag == 126:     # 响应风速自动控制指令
        data21 = "\x68\x08\x00\xFF\x12\x1D\x2E\x16"
        uart.write(data21)
    if flag == 1:       # 响应风速挡位控制
        data21 = "\x68\x08\x00\xFF\x12\x18\x29\x16"
        uart.write(data21)
    if flag == 2:
        data21 = "\x68\x08\x00\xFF\x12\x19\x2A\x16"
        uart.write(data21)
    if flag == 3:
        data21 = "\x68\x08\x00\xFF\x12\x1A\x2B\x16"
        uart.write(data21)
    if flag == 4:
        data21 = "\x68\x08\x00\xFF\x12\x1B\x2C\x16"
        uart.write(data21)
    if flag == 5:
        data21 = "\x68\x08\x00\xFF\x12\x1C\x2D\x16"
        uart.write(data21)
    flag = 0        # 在每次响应指令后，初始化flag
    
