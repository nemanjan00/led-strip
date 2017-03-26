import alsaaudio, numpy, struct, serial

def rgb_int2tuple(rgbint):
    return (rgbint // 256 // 256 % 256, rgbint // 256 % 256, rgbint % 256)

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
inp.setchannels(1)
inp.setrate(44100)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(1024)

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=0.5)

i = 0

while True:
    i = i + 1

    l, data = inp.read()
    a = numpy.fromstring(data, dtype='int16')

    current = numpy.abs(a).mean()

    if i % 5 == 0:
        i = 0

        if current > 12000:
            current = 12000

        #current = current / 12000 * 16777215;

        current =  rgb_int2tuple(current)

        ser.write(str(current[0] / 12000 * 16777215))
        ser.write(" ")
        ser.write(str(current[1] / 12000 * 16777215))
        ser.write(" ")
        ser.write(str(current[2] / 12000 * 16777215))
        ser.write("\n")

