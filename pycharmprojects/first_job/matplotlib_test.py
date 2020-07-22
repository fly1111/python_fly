import numpy as np
import matplotlib.pyplot as plt

def main():

    x = np.linspace(-np.pi*2,np.pi*2,256,endpoint=True)
    c,s = np.cos(x),np.sin(x)
    plt.figure(1)
    plt.plot(x,c,color='blue',linewidth=1.0,linestyle='solid',label='COS',alpha=0.8)
    plt.plot(x,s,'r--',label="SIN")
    plt.title('BBB')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position(('data',0))
    ax.spines['bottom'].set_position(('data',0))
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.xticks([-np.pi,-np.pi/2,-np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$',r'$+\pi/2$',r'$+\pi$'])
    plt.yticks(np.linspace(-1,1,5,endpoint=True))
    for label in ax.get_xticklabels()+ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.2))

    plt.show()
if __name__ == '__main__':
    main()
