import re
import statistics
wynagrodzenie_XYZ = '21600 zł (wynagrodzenie prezesa ), 4350 zł, 3920 zł, 5590 zł, 3250 zł, 4010 zł'
wynagrodzenie_XYZ = re.findall('\d+',wynagrodzenie_XYZ)
wynagrodzenie = []
for x in wynagrodzenie_XYZ:
    wynagrodzenie.append(int(x))
Srednia = statistics.mean(wynagrodzenie)
Mediane = statistics.median(wynagrodzenie)
Odchylenie = statistics.stdev(wynagrodzenie)
print(Srednia, Mediane, Odchylenie)
