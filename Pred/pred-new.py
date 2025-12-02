import pandas as pd
import numpy as np

def scd(x):
    return 1 / (np.pi * (1 + x**2))

df = pd.read_csv("new-patients.csv")

x1 = df["x1"].values
x2 = df["x2"].values
x3 = df["x3"].values
x4 = df["x4"].values
x5 = df["x5"].values
x6 = df["x6"].values
x7 = df["x7"].values
x8 = df["x8"].values

d1 = ((x1+x6)/x2) + np.abs((x2/x3) - (x5/x4))
d2 = ((x1**2)/(x3**3)) / np.sin(np.log(x7))
d3 = np.sin(x8**3) * ((x8/x4) * np.log(x4))
d4 = np.sin(x7/x5) * (np.cos(x1) + np.cos(x4))
d5 = np.abs(np.sin(x3+x8) - ((x7/x8) - np.sin(x8)))
d6 = (np.cos(x1)**3) / np.abs((x4/x3) - scd(x2))

c = np.array([
    0.5668014591E+02,
    0.1068129364E+05,
   -0.6212926032E-03,
   -0.5250159276E+01,
   -0.4725514326E+01,
   -0.1210215829E-02
])
c0 = 0.1352338282E+02

mPAP = c0 + c[0]*d1 + c[1]*d2 + c[2]*d3 + c[3]*d4 + c[4]*d5 + c[5]*d6

out = pd.DataFrame({"No": df["No"], "mPAP-pred": mPAP})
out.to_csv("new-results.csv", index=False)
