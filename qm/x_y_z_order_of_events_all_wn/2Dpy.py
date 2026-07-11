import math
import numpy
import pandas
from matplotlib import pyplot

hetero = False

# hetero=True
inputfile1="2t2d_input.csv"

left_large = True
dynamic = True

# file read
spec1 = pandas.read_csv(inputfile1, header=0, index_col=0).T
#if hetero == False: inputfile2 = inputfile1
#spec2 = pandas.read_csv(inputfile2, header=0, index_col=0).T

# synchronous correlation
sync = pandas.DataFrame(spec1.values.T @ spec1.values / (len(spec1) - 1))
sync.index = spec1.columns
sync.columns = spec1.columns
sync = sync.T
sync.to_csv(inputfile1[: len(inputfile1) - 4] + "_sync.csv")

# Hilbert-Noda transformation matrix
noda = numpy.zeros((len(spec1), len(spec1)))
for i in range(len(spec1)):
    for j in range(len(spec1)):
        if i != j: noda[i, j] = 1 / math.pi / (j - i)

# asynchronouse correlation
asyn = pandas.DataFrame(spec1.values.T @ noda @ spec1.values / (len(spec1) - 1))
asyn.index = spec1.columns
asyn.columns = spec1.columns
asyn = asyn.T
asyn.to_csv(inputfile1[: len(inputfile1) - 4] + "_async.csv")

cod=numpy.multiply(sync,asyn)
sgn=numpy.sign(cod)
sgn.to_csv("sgn.csv")
sgn[sgn<0] = 0
sgn.T.sum().to_csv("ref_gaussians.csv")





