r = input().split()
u = input()
r_out = 1/(1/float(r[0]) + 1/float(r[1]) + 1/float(r[2]) + 1/float(r[3]))

print("%.2f" % r_out)

print("%.2f %.2f %.2f %.2f %.2f" % (float(u)/r_out, float(u)/float(r[0]), float(u)/float(r[1]), float(u)/float(r[2]), float(u)/float(r[3])) )
