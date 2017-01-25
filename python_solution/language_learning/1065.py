r = input()
total_sec = int(r)

sec = total_sec % 60
min = ((total_sec - sec) /60) % 60
hour = (((total_sec - sec) /60 - min)/60) %24

print("%d:%d:%d" % (hour,min,sec))
