import random
import statistics
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np
from scipy.stats import sem
# import the graph in dictionary key : Neighborhood of key
distance_between_cop_n_robber = int(input('Distance between cop and robber '))
ex = []
th = []
co = []
for k in range(distance_between_cop_n_robber+1):
    number_of_iteration = 100000
    Time_taken = []
    start = []
    for i in range(k + 1) :
        r = (k - i, i)
        rn = (k - i, -i)
        nr = (-k + i, i)
        nrn = (-k + i, -i)
        start.append(r)
        start.append(rn)
        start.append(nr)
        start.append(nrn)

    start = list( dict.fromkeys(start) )

    for i in range(number_of_iteration):
    # Initial position of cop and robber
        i = 0
        c_x = 0
        c_y = 0
        cop = (c_x,c_y)
        robber = random.choice(start)
        (r_x,r_y) = robber
        #print("Initial position of cop is ", cop)
        #print("Initial position of robber is ", robber)
        # Game play
        while i >= 0:
            if cop == robber:
         #       print("Robber go to cop")
                break
            i += 1
    # Cop strategies
            diff_x = abs(c_x - r_x)
            diff_y = abs(c_y - r_y)
            if diff_x >= diff_y and c_x - r_x > 0: c_x = c_x - 1
            elif diff_x >= diff_y and c_x - r_x < 0: c_x = c_x + 1
            elif diff_y >= diff_x and c_y - r_y > 0: c_y = c_y - 1
            else : c_y = c_y + 1
            cop = (c_x,c_y)
          #  print("position of cop in turn {} is ".format(i), cop)
            if cop == robber :
           #     print("Cop catch the robber")
                break
    #Robber move
            (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
            r_x = r_x + dx
            r_y = r_y + dy
            robber = (r_x,r_y)
        #    print("position of robber in turn {} is ".format(i), robber)
        #print('The time taken until the game end ', i)
        Time_taken.append(i)
        #print('######################################################')
    Expected_capture_time = statistics.mean(Time_taken)
    print("The expected capture time of a graph G with distance {} is ".format(k) , Expected_capture_time)
    print("The Standard Error is ", sem(Time_taken))
    if k % 2 == 1:
        cdct = k + (1 / 2)*(0.5772156649 + np.log((k+1)/2))
    elif k == 0: cdct = 0
    else:
        cdct = k + 2 + (1 / 2)*(0.5772156649 + np.log(k/2))
    Sum = 0
    if k % 2 == 1:
        for m in range(1, int((k+1)/2)):
            Sum = Sum + 2/(4*m+1)
        dct = k + Sum
    elif k == 0:
        dct = 0
    else :
        for m in range(1, int(k/2)):
            Sum = Sum + 2/(4*m+3)
        dct = k + 2 + Sum
    print('the Theoretical result is', dct)
    co.append(cdct)
    th.append(dct)
    ex.append(Expected_capture_time)
    err = dct - Expected_capture_time
    print('The error is ', err)
    print('######################################################')

expoint = np.array(ex)
#yerrpoint = np.array(yerrs)
xpoint = list(range(distance_between_cop_n_robber+1))
#plt.errorbar(xpoint, ex, yerr=yerrpoint, fmt='.k')
plt.plot(xpoint, ex, label='result from simulation')
plt.plot(xpoint, th, label='result from theorem')
plt.plot(xpoint, co, label='result from corollary')
plt.xlim(0, 100)
#plt.ylim(5,25)
plt.fill_between((10,20), 5, 25, facecolor='green', alpha=0.2) # blocked area for first axes
plt.fill_between((80,90), 75, 95, facecolor='orange', alpha=0.2) # blocked area for second axes
plt.legend()

plt.show()

#fig = plt.figure(figsize=(6, 5))
#plt.subplots_adjust(bottom = 0., left = 0, top = 1., right = 1)

# Create first axes, the top-left plot with green plot
#sub1 = fig.add_subplot(1,2,1) # two rows, two columns, fist cell
#sub1.plot(xpoint, ex)
#sub1.plot(xpoint, th)
#sub1.plot(xpoint, co)
#sub1.set_xlim(10, 20)
#sub1.set_ylim(5, 25)

# Create second axes, the top-left plot with orange plot
#sub2 = fig.add_subplot(1,2,2) # two rows, two columns, second cell
#sub2.plot(xpoint, ex)
#sub2.plot(xpoint, th)
#sub2.plot(xpoint, co)
#sub2.set_xlim(80, 90)
#sub2.set_ylim(75, 95)

# Create third axes, a combination of third and fourth cell
#sub3 = fig.add_subplot(1,2,(1,2)) # two rows, two columns, combined third and fourth cell
#sub3.plot(xpoint, ex, label='result from simulation')
#sub3.plot(xpoint, th, label='result from theorem')
#sub3.plot(xpoint, co, label='result from corollary')
#sub3.set_xlim(0, 100)
# Create blocked area in third axes
#sub3.fill_between((10,20), 5, 25, facecolor='green', alpha=0.2) # blocked area for first axes
#sub3.fill_between((80,90), 75, 95, facecolor='orange', alpha=0.2) # blocked area for second axes

#plt.legend(bbox_to_anchor=(1.05, 1.04))
#plt.show()