import random
import math
import GA_Func as GAF
import matplotlib.pyplot as plt
import numpy as np


pop_size = 100
cover_rate = 0.5 #교배확률
mut_rate = 1
gen_size = 100

new_pop = []
chrom = []

result = []

max_fx = []
min_fx = []
ave_fx = []
max_coord_pop = []

def main(pop=[]):
    tmp =[]
    new_pop = []
    global mut_rate
    

    
    if len(pop) == 0:
        for i in range(pop_size):
            chrom = []
            for i in range(12):
                chrom.append(random.randint(0,1))
            pop.append(chrom)
            new_mut_rate = mut_rate

    else:
        new_mut_rate = mut_rate / (max_fx[-1]**2)


    for i in range(pop_size):
        tmp.append(GAF.bin2dec(pop[i]))
        tmp.append(GAF.dec2coord(tmp[0]))
        tmp.append(GAF.calcfx(tmp[1]))
        tmp.append(0)
        tmp.append(0)

        result.append(tmp)
        tmp = []



    tot = 0
    for i in range(pop_size):
        tot += result[i][2]

    for i in range(pop_size):
        result[i][3] = result[i][2] / tot

    for i in range(pop_size):
        if i == 0:
            result[i][4] = 0 + result[i][3]
        else:
            result[i][4] = result[i-1][4] + result[i][3]

    #Selection
    while len(new_pop) <= pop_size:
        rnd = random.random()
        for i in range(pop_size):
            if len(new_pop) <= pop_size:
                
                if i == pop_size - 1:
                    if (rnd >= result[i][4] and rnd < 1):
                        new_pop.append(pop[i])

                elif i == 0:
                    if (rnd >= 0 and rnd < result[i][4]):
                        new_pop.append(pop[i])
                    

                else:
                    if (rnd >= result[i-1][4] and rnd < result[i][4]):
                        new_pop.append(pop[i])

    for i in range(0, pop_size, 2):
        a = []
        b = []
        c = []
        d = []
        #절단점
        rnd = random.randint(1,10)
        if random.random() <= cover_rate:
            a = new_pop[i][0:rnd]
            b = new_pop[i + 1][0:rnd]
            c = new_pop[i][rnd:]
            d = new_pop[i+1][rnd:]

            new_pop[i] = a + d
            new_pop[i+1] = b + c

    for i in range(pop_size):
        if random.random() <= new_mut_rate:
            pos = random.randint(0,11)
            if new_pop[i][pos] == 0:
                new_pop[i][pos] = 1
            else:
                new_pop[i][pos] = 0
    
    fx=[]
    coord_pop = []
    for i in range(pop_size):
        dec = GAF.bin2dec(new_pop[i])
        coord = GAF.dec2coord(dec)
        coord_pop.append(GAF.dec2coord(dec))
        fx.append(GAF.calcfx(coord))
        
    max_fx.append(max(fx))
    count = fx.count(max(fx))
    max_coord_pop.append(coord_pop[count])
    
    
    min_fx.append(min(fx))
    ave_fx.append(np.average(fx))
    
    return new_pop

for i in range(gen_size):
    if i == 0:
        pop = main()
    else:
        result = []
        pop = main(pop)

for i in range(pop_size):
        dec = GAF.bin2dec(pop[i])
        coord = GAF.dec2coord(dec)
        fx = GAF.calcfx(coord)
        

plt.subplot(2,2,1)
plt.plot(max_fx,"b-",label = "MAX_FIT")
plt.legend()
plt.plot(ave_fx,"g-", label = "AVERAGE_FIT")
plt.legend()
plt.xlabel('GEN_SIZE')
plt.ylabel('Fitness')
plt.title('MAX Graph')

plt.subplot(2,2,2)
plt.plot(min_fx,"r-", label = "MIN_FIT")
plt.legend()
plt.plot(ave_fx,"g-", label = "AVERAGE_FIT")
plt.legend()
plt.xlabel('GEN_SIZE')
plt.ylabel('Fitness')
plt.title('MIN Graph')

plt.subplot(2,2,3)
plt.plot(ave_fx,"g-", label = "AVERAGE_FIT")
plt.legend()
plt.xlabel('GEN_SIZE')
plt.ylabel('Fitness')
plt.plot(max_fx,"b-",label = "MAX_FIT")
plt.legend()
plt.plot(min_fx,"r-", label = "MIN_FIT")
plt.legend()
plt.title('TOTAL Graph')

plt.subplot(2,2,4)
x = np.arange(-1.0,2,0.001)
plt.plot(x, x * np.sin(10*np.pi * x)+ 3.5,"b-")

plt.show()

        


