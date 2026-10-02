import matplotlib.pyplot as pl
U50 = sorted([0.1, 0.665, 0.445, 0.55, 0.055, 0.27, 0.695])
I50 = [42.6, 40.9, 33.8, 27.4, 16.65, 6, 3.25][::-1]
U30 = sorted([0.685, 0.325, 0.095, 0.365, 0.05, 0.45])
I30 = sorted([48, 22.7, 6.6, 25.4, 3.5, 31.7])
U20 = sorted([0.625, 0.06, 0.325, 0.02, 0.47, 0.25])
I20 = sorted([47.06, 4.35, 24.5, 1.4, 35.2, 18.6])
UI50 = 0 * 7
UU50 = 0 * 7
UI30 = 0 * 6
UU30 = 0 * 6
UI20 = 0 * 6
UU20 = 0 * 6
R50 = 0
R30 = 0
R20 = 0
for i in range (len(U50)):
    UI50 += U50[i] * I50[i] * 1000
    UU50 += I50[i] ** 2
    U50[i] *= 1000
R50 = UI50 / UU50
for i in range (len(U30)):
    UI30 += U30[i] * I30[i] * 1000
    UU30 += I30[i] ** 2
    U30[i] *= 1000
R30 = UI30 / UU30
for i in range (len(U20)):
    UI20 += U20[i] * I20[i] * 1000
    UU20 += I20[i] ** 2
    U20[i] *= 1000
R20 = UI20 / UU20
for i in range (len(U50)):
    sd50 = (U50[i] - R50 * I50[i]) ** 2
for i in range (len(U30)):
    sd30 = (U30[i] - R30 * I30[i]) ** 2
for i in range (len(U20)):
    sd20 = (U20[i] - R20 * I20[i]) ** 2
d50 = (sd50 / 6) ** 0.5
d30 = (sd30 / 5) ** 0.5
d20 = (sd20 / 5) ** 0.5
print(d50, d30, d20)
pl.errorbar(I50, U50, xerr = 0, yerr = d50, color = "green", marker = "o", label = f"50cm\nk = {R50}", ecolor = "black", alpha = 0.75, linewidth = 0.5)
pl.errorbar(I30, U30, color = "red", xerr = 0, yerr = d30, marker = "o", label = f"30 cm\nk = {R30}", ecolor = "black", alpha = 0.75, linewidth = 0.5)
pl.errorbar(I20, U20, color = "blue", xerr = 0, yerr = d20, marker = "o", label = f"20 cm\nk = {R20}", ecolor = "black", alpha = 0.75, linewidth = 0.5)
pl.xlabel("I, мА", loc = "right")
pl.ylabel("U, мB", loc = "top")
pl.legend()
pl.show()