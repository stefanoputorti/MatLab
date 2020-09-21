import numpy as np
import scipy.stats as ss
from scipy.stats import norm
import matplotlib.pyplot as plt

## VaR di un opzione

T = 1 # Maturity
S0 = 100 # Spot Price
K = 100 # Strike Price
sg = 0.3 # annual volatility
rf = 0.01 # risk free rate
mu = 0 # mean log-return
##############################################################################
##### Definizione formule di B&S e Greeks
##############################################################################
def BSVanilla(S,K,r,sg,T, option = "call"):
    d1 = (np.log(S/K)+(r + (sg**2)/2)*T)/ (sg * np.sqrt(T))
    d2 = d1 - sg * np.sqrt(T)
    gamma = ss.norm.pdf(d1,0,1) / (S0 * sg * np.sqrt(T))
    if option == "call" :
        BS = S * ss.norm.cdf(d1,0.0,1.0) - K * np.exp(-r * T) *\
                           ss.norm.cdf(d2,0.0,1.0)
        delta = ss.norm.cdf(d1,0.0,1.0)
        theta = - (S*sg*ss.norm.pdf(d1))/(2*np.sqrt(T)) - r*K*np.exp( -r*T)*ss.norm.cdf(d2)
    if option == "put" :
        BS = K * np.exp(-r * T)*ss.norm.cdf(-d2,0.0,1.0) - S * \
                         ss.norm.cdf(-d1,0.0,1.0)
        delta = -ss.norm.cdf(- d1,0.0,1.0)
        theta = -(S*sg*norm.pdf(d1)) / (2*np.sqrt(T))+ r*K * np.exp(-r*T) * ss.norm.cdf(-d2)
    return BS, delta, gamma, theta

print(BSVanilla(S0,K,rf,sg,1,option="call"))
call = BSVanilla(S0,K,rf,sg,1,option="call")[0]
delta = BSVanilla(S0,K,rf,sg,1,option="call")[1]
gamma = BSVanilla(S0,K,rf,sg,1,option="call")[2]
theta = BSVanilla(S0,K,rf,sg,1,option="call")[3]
#############################################################################
# Montecarlo call option price
#############################################################################
nsim = 100000
Z = np.random.randn(1,nsim)
S_n = S0 * np.exp((rf - 0.5*sg**2) * T + sg * np.sqrt(T)*Z)
Cn = np.exp(-rf * T) * np.maximum(S_n - K,0)
MCBSCallPrice = Cn.mean()
MCstd_error = Cn.std() / np.sqrt(nsim)
print(MCBSCallPrice)
print(MCstd_error)
##############################################################################
# Calculate the prob. that call price will decrease by in 20 days
##############################################################################
nsim = 50000
horizon20d = 20/250
sg20 = sg *np.sqrt(horizon20d)
Z = np.random.randn(1, nsim)
# simulation stock price after 20 days
Sn = S0 * np.exp((rf - (sg**2)/2) * horizon20d + sg20 * Z)
# determine call price after 20 days
SimCallPrice = BSVanilla(Sn,K,rf,sg,T - horizon20d, option = "call")
r = (SimCallPrice/call) - 1
x = r < - 0.1
Prob = np.sum(x)/nsim * 100
print(Prob)
##############################################################################
# Calculate VAR 99% at different time horizon
##############################################################################
## Exact method
horizon = [1/250, 10/250, 20/250, 30/250, 60/250, 90/250]
alpha = 0.99
z = norm.ppf(1-0.99, loc = 0, scale = 1)
nhor = len(horizon)
media = np.zeros(nhor)
vol= np.zeros(nhor)
r_VaR= np.zeros(nhor)
P_worst= np.zeros(nhor)
P_call= np.zeros(nhor)
VaR_exact= np.zeros(nhor)

for i in range(nhor):
    media[i] = mu * horizon[i]
    vol[i] = sg * np.sqrt(horizon[i])
    r_VaR[i] = - (media[i] + vol[i] * z)
    P_worst[i] = S0 * np.exp(-r_VaR[i])
    P_call[i] = BSVanilla(P_worst[i],K,rf,sg,T - horizon[i], option = "call")[0]
    VaR_exact[i] = call - P_call[i]
print("VaR Esatto")
print(VaR_exact)
## Montecarlo Full Revaluation
nsim = 500
media = np.zeros(nhor)
vol= np.zeros(nhor)
rt_i = np.zeros((int(nsim),nhor))
S_i = np.zeros((int(nsim),nhor))
P_Call_MC = np.zeros((int(nsim),nhor))
PL_MC = np.zeros((int(nsim),nhor))
VaR_MC_FULL = np.zeros(nhor)
Z = np.random.randn(nsim,1)
for i in range(nhor):
    media[i] = mu * horizon[i]
    vol[i] = sg * np.sqrt(horizon[i])
for j in range(nhor):
    for i in range(nsim):
        rt_i[i,j] = media [j] + vol[j] * Z[i]
        S_i[i,j] = S0 * np.exp(rt_i[i,j])
        P_Call_MC[i,j] = BSVanilla(S_i[i,j],K,rf,sg,T - horizon[j],\
                                   option = "call")[0]
        PL_MC[i,j] = P_Call_MC[i,j] - call
    VaR_MC_FULL[j] = - np.quantile(PL_MC[:,j], (1-alpha))
print("VaR MC Full")
print(VaR_MC_FULL)
## Montecarlo delta
dP = np.zeros((int(nsim),nhor))
PL_linear = np.zeros((int(nsim),nhor))
VaR_MC_Delta = np.zeros(nhor)

for j in range(nhor):
    for i in range(nsim):
        dP[i,j] = np.exp(rt_i[i,j]) - 1
        PL_linear[i,j] = theta * horizon[j] + delta * S0 * dP[i,j]
    VaR_MC_Delta[j] = - np.quantile(PL_linear[:,j],(1-alpha))
print("VaR MC Delta")
print(VaR_MC_Delta)
# Montecarlo Delta / Gamma
dP = np.zeros((int(nsim),nhor))
PL_Quad = np.zeros((int(nsim),nhor))
VaR_MC_DeltaGamma = np.zeros(nhor)
for j in range(nhor):
    for i in range(nsim):
        dP[i,j] = np.exp(rt_i[i,j]) - 1
        PL_Quad[i,j] = theta * horizon[j] + delta * S0 * dP[i,j] + 0.5 * gamma \
                        * (S0**2) * dP[i,j]**2
    VaR_MC_DeltaGamma[j] = - np.quantile(PL_Quad[:,j],(1-alpha))
print("VaR MC Delta-Gamma")
print(VaR_MC_DeltaGamma)
# Taylor 1st Approx
r = -(media + vol * z)
dPtaylor1 = np.exp(r) - 1
VaR_Linear_Taylor = np.zeros(nhor)
for i in range(nhor):
    VaR_Linear_Taylor[i] = theta * horizon[i] + delta * S0 * dPtaylor1[i]
print("VaR 1st App. Taylor")
print(VaR_Linear_Taylor)
# Taylor 2nd Approx
VaR_Quad_Taylor = np.zeros(nhor)
dPtaylor2 = np.exp(r) - 1
for i in range(nhor):
    VaR_Quad_Taylor[i] = theta * horizon[i] + delta * S0 * dPtaylor2[i] + 0.5 * gamma *\
                  (S0**2) * (dPtaylor2[i]**2)
print("VaR 2nd App. Taylor")
print(VaR_Quad_Taylor)


## Plot

fig1 = plt.figure(1)
plt.plot(horizon,VaR_exact,"k",label="Exact")
plt.plot(horizon,VaR_MC_FULL, label="MC Full Revaluation")
plt.plot(horizon,VaR_MC_Delta, label="MC Delta")
plt.plot(horizon,VaR_MC_DeltaGamma, label="MC Delta-Gamma")
plt.plot(horizon,VaR_Linear_Taylor, label="Linear Approx.")
plt.plot(horizon,VaR_Quad_Taylor, label="Quadratic Approx.")
plt.title("Comparation Method of VaR")
plt.legend()
plt.ylabel("VaR")
plt.xlabel("Time Horizon")
plt.grid()
plt.tight_layout()
plt.show()
