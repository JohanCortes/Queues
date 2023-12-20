from statistics import NormalDist, correlation, pstdev, pvariance, quantiles
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot


class Poblacion():
    def __init__(self, data, n):
        self.data = data
        self.n = n

    def cal(self, key, interval):
        d = []
        for i in self.data:
            d.append(i[key][0])
            if(key == 'po'):
                d[-1] *= 100
        m = np.mean(d)
        min = np.min(d)
        max = np.max(d)
        des = pstdev(d)
        var = pvariance(d)
        dist = NormalDist(m, des)
        i1 = (1-interval)/2
        i2 = (1-interval)/2+interval
        IC = [dist.inv_cdf(i1), dist.inv_cdf(i2)]
        tdist = ''
        corr = 0

        qu = [q for q in quantiles(d, n=100)]
        dist = {'Normal': [q for q in quantiles(np.random.normal(m, des, self.n), n=100)],
                'Exponencial': [q for q in quantiles(np.random.exponential(1/m, self.n), n=100)],
                "Weibull": [q for q in quantiles(np.random.weibull(m, self.n), n=100)],
                "Gamma": [q for q in quantiles(np.random.gamma(m, des, self.n), n=100)],
                "Lognormal": [q for q in quantiles(np.random.lognormal(m, des, self.n), n=100)],
                "Beta": [q for q in quantiles(np.random.beta(m, des, self.n), n=100)],
                "Chi-cuadrado": [q for q in quantiles(np.random.chisquare(m, self.n), n=100)]}

        for k in dist:
            c = correlation(qu, dist[k])
            if(c > corr):
                corr = c
                tdist = k

        self.key = key
        self.unidades = self.data[0][key][1]
        self.opcion = self.data[0][key][2]
        self.d = d
        self.m = m
        self.min = min
        self.max = max
        self.des = des
        self.var = var
        self.IC = IC
        self.tdist = tdist
        self.corr = corr
        return self.min, self.max, self.m, self.des, self.var, [str(self.IC[0])[0:8], str(self.IC[1])[0:8]], self.tdist, self.corr

    def graph(self):
        d = np.array(self.d)
        f = np.linspace(d.min(), d.max(), 10)
        cont = np.zeros(10)
        for i in range(len(d)):
            k = 0
            for j in range(len(f)-1):
                if(d[i] >= f[j+1]):
                    k += 1
                else:
                    cont[k] += 1
                    break

        cont = list(map(lambda x: x/len(d), cont))
        plt.subplot(2, 1, 1)
        plt.plot(f, cont, 'r')
        """ plt.fill_between(f,cont,
                         0, where=(f>=self.IC[0]) & (f<=self.IC[1]), color='blue', alpha=0.2) """
        #plt.fill_betweenx([0,max(cont)], self.IC[0],self.IC[1],  color='blue', alpha=0.2)
        plt.axvline(self.IC[0], color='blue', linewidth=1, linestyle='dashed')
        plt.axvline(self.IC[1], color='blue', linewidth=1, linestyle='dashed')
        plt.legend(["Distribución", 'IC1 = '+str(self.IC[0])[0:-8],
                   'IC2 = ' + str(self.IC[1])[0:-8]])
        plt.ylim(0)
        plt.grid()
        plt.ylabel('Probabilidad')
        plt.xlabel(self.data[0][self.key][2] +
                   ' ('+self.data[0][self.key][1]+')')

        plt.subplot(2, 1, 2)
        plt.axhline(y=self.m, color='red', linewidth=2)
        plt.axhline(y=self.IC[0], color='blue', linestyle='--')
        plt.axhline(y=self.IC[1], color='blue', linestyle='--')
        plt.axis([0, self.n+1, self.m-(((self.m-self.min)+(self.max-self.m))),
                 self.m+(((self.m-self.min)+(self.max-self.m)))])
        plt.plot(list(range(1, self.n+1)), d,
                 color='green', marker='o', linestyle=' ')
        plt.fill_between([0, self.n+1], self.IC[0],
                         self.IC[1], color='orange', alpha=0.2)
        plt.grid()
        plt.ylabel(self.data[0][self.key][2] +
                   ' ('+self.data[0][self.key][1]+')')
        plt.xlabel('Iteración')
        plt.legend(['μ = '+str(self.m)[0:-8], 'IC1 = '+str(self.IC[0])[0:-8],
                   'IC2 = ' + str(self.IC[1])[0:-8]])
        plt.show()

    def graph_tdist(self):
        qqplot(np.array(self.d), line='s')
        plt.show()
