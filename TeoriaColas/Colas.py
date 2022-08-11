import numpy as np
import matplotlib.pyplot as plt


class Cola():
    def __init__(self, lam, mu, sig, n):
        self.lam = lam  # Tasa llegada: clientes/hora
        self.mu = mu  # Tasa servicio: clientes/hora
        self.sig = sig  # Desviación estándar: horas
        self.rend = {}
        self.poisson = np.random.poisson(lam, n)
        self.normal = np.random.normal(mu, sig, n)

    def calcular_f(self):
        self.rend['p'] = self.lam/self.mu
        self.rend['p0'] = 1-self.rend['p']
        self.rend['lq'] = (self.lam**2*self.sig**2 +
                           self.rend['p']**2)/(2*self.rend['p0'])
        self.rend['ls'] = self.rend['lq']+self.rend['p']
        self.rend['ws'] = self.rend['ls']/self.lam
        self.rend['wq'] = self.rend['lq']/self.lam
        return self.rend

    def graph(self):
        nor = np.linspace(self.normal.min(), self.normal.max(), 100)
        cont = np.zeros(100)
        for i in range(len(self.normal)):
            k = 0
            for j in range(len(nor)-1):
                if(self.normal[i] >= nor[j+1]):
                    k += 1
                else:
                    cont[k] += 1
                    break

        cont = map(lambda x: x/len(self.normal), cont)

        poi = np.arange(self.poisson.min(), self.poisson.max(), 1)

        plt.subplot(2, 1, 1)
        plt.bar(poi, list(
            map(lambda x: list(self.poisson).count(x)/len(self.poisson), poi))),
        plt.legend(["Poisson"])
        plt.grid(axis='y')
        plt.ylabel('Probabilidad')
        plt.xlabel('Clientes ingresados por hora')
        plt.subplot(2, 1, 2)
        plt.plot(nor, list(cont), 'r'),
        plt.legend(["Normal"])
        plt.grid()
        plt.ylabel('Probabilidad')
        plt.xlabel('Clientes atendidos por hora')
        plt.show()

    def statistic(self):

        t_e_l = list(map(lambda x: 1/x*60, self.poisson))
        for i in range(len(t_e_l)):
            if t_e_l[i] == np.inf:
                t_e_l[i] = 60*self.lam
        m_l = [t_e_l[0]]
        for i in range(1, len(t_e_l)):
            m_l.append(m_l[i-1]+t_e_l[i])

        t_i_s = [m_l[0]]
        t_s = list(map(lambda x: 1/x*60, self.normal))
        t_t_s = []

        for i in range(1, len(self.normal)):
            t_t_s.append(t_i_s[i-1]+t_s[i-1])
            t_i_s.append(max(m_l[i], t_t_s[i-1]))
        t_t_s.append(t_i_s[-1]+t_s[-1])

        t_e = []

        for i in range(len(t_i_s)):
            t_e.append(t_i_s[i]-m_l[i])

        res = {}
        res['telp'] = [np.array(t_e_l).mean(), 'min',
                       'Tiempo entre llegada promedio']
        res['mul'] = [m_l[-1]/60, 'horas', 'Momento ultima llegada']
        res['tius'] = [t_i_s[-1]/60, 'horas', 'Tiempo inicio del ultimo servicio']
        res['tsp'] = [np.array(t_s).mean(), 'min',
                      'Tiempo de servicio promedio']
        res['ttus'] = [t_t_s[i]/60, 'horas',
                       'Tiempo terminacion ultimo servicio']
        res['tep'] = [np.array(t_e).mean(), 'min', 'Tiempo espera promedio']
        res['tte'] = [np.array(t_e).sum()/60, 'horas',
                      'Tiempo total de espera']
        res['teo'] = [np.array(t_s).sum()/60, 'horas', 'Tiempo en operacion']
        res['po'] = [res['teo'][0]/res['ttus']
                     [0], '%', 'Porcentaje de operacion']
        #print("\n---------\n", res)
        return res
