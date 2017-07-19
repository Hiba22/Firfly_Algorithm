from math import sin , pi
import numpy


class Michaelwicz_function:
    def compute(self, decision_variable, dimensions):
        Result = 0
        OverallResult = 0
        for dim in range(0,dimensions):
           X = decision_variable[dim]
           Result = sin(decision_variable[dim]) * (sin(dim*decision_variable[dim]**2 / pi ))** (10*2)
           OverallResult = OverallResult + Result

        return -(OverallResult)

if __name__ == '__main__':
    t = Michaelwicz_function()
    values = numpy.random.uniform(0,1,2)
    tt = t.compute(values,2)

    print(tt)