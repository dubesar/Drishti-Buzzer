import serial
ser=serial.Serial('COM3',9600)
c=0
while True:
    if(ser.inWaiting()):
        fh=open("buzzer.txt","a")
        txt=ser.read()
        c+=len(txt)
        fh.write(txt)
        if(c>=4):
            fh.write('\n')
        fh.close()
