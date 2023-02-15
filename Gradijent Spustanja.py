import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def plot_gradient():
    
    fig = plt.figure(figsize=(10,8))
    ax=fig.gca(projection='3d')
    ax.set_title('3D surfice plot of ' + 'f=5*x1^4+(x2-3)^3+2*x2^4')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    x1=np.arange(-10,10,0.05)
    x2=np.arange(-10,10,0.05)

    x1, x2 = np.meshgrid(x1, x2)
    f=5*x1**4+(x2-3)**3+2*x2**4
    surface=ax.plot_surface(x1, x2, f, cmap=cm.coolwarm, linewidth=0)
    fig.colorbar(surface, shrink=0.5)
    
    plt.show()
    
def plot_decent(X, Y):
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(X, Y)
    ax.set_title("Tacke spustanja")
    ax.set_xlabel("X Osa")
    ax.set_ylabel("Y Osa")
    plt.show()
    

def metod_sjecice(x, d):
    Nmax=100
    izt=0
    k=0
    at=0.001
    ast=0
    an=100
    epsilon=0.00001
    tacka=x+ast*d
    izs= np.matmul(np.transpose(fun_grad(tacka)), d)
    while abs(an-at)>epsilon and k<Nmax:
        k=k+1
        if k>1:
            ast=at
            at=an
            izs=izt

        tacka=x+at*d;
        izt=np.matmul(np.transpose(fun_grad(tacka)), d)
        an=at-(at-ast)/(izt-izs)*izt
    return an


def fun_grad(x):
    g=np.array([ [20*x.item(0)**3],[8*x.item(1)**3  + 3*(x.item(1) - 3)**2] ])
    return g
    

def gradien_decent(x, y):
    xs = np.array([[x],[y]])
    N=xs.size
    xn=np.ones((N,1), dtype=int)
    epsilon=0.00001
    Nmax=500
    k=0
    X=[]
    Y=[]
    while np.linalg.norm(xn-xs)/max(1,np.linalg.norm(xs))>=epsilon and k<Nmax:
        k=k+1
        if k>1:
            xs=xn
        g=fun_grad(xs)
        alfa=metod_sjecice(xs, -g)
        xn=xs-alfa*g
        X.append(xn.item(0))
        Y.append(xn.item(1))
    print(k)
    return X, Y


X, Y=gradien_decent(1,3)
plot_gradient()
plot_decent(X, Y)





