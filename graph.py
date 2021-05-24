import matplotlib.pyplot as plt
import random
import math
import numpy

dist = []
rssi = []
# ple = random.uniform(1.6, 1.8)
ple = 1.7
standard_deviation = random.uniform(10, 12)
ple = random.uniform(1.6, 1.8)
standard_deviation = random.uniform(2, 4)
for i in range(0, 16):
    dst = i
    dist.append(dst)
    avg_rss = 0
    for i in range(10000):
        avg_rss +=  -35 -10 * ple * math.log10(dst+1) + numpy.random.normal(0, standard_deviation)
    avg_rss = avg_rss / 10000
    print(dst,": ", avg_rss)
    rssi.append(avg_rss)

#plt.plot(dist, rssi, linewidth=2, color = 'r')
#plt.show()

# 1 :  -34.96596299049885
# 2 :  -47.22179171000779
# 3 :  -54.46284033982756
# 4 :  -59.595091405587475
# 5 :  -63.584725097600625
# 6 :  -66.8047159850161
# 7 :  -69.53357760543064
# 8 :  -71.91774979498788
# 9 :  -73.97894271864395
# 10 :  -75.92070923236913
# 11 :  -77.50098107101974
# 12 :  -79.05671264822625
# 13 :  -80.5227140946218
# 14 :  -81.83216920926783
# 15 :  -82.99460173083266
for i in rssi:
    dst = math.pow(10, -(i + 35) / 17) - 1
    print(dst)
