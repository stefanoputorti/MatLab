import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import tkinter as tk
import numpy as np
from numpy import random
import requests #per counicare con API
import matplotlib.pyplot as plt
from tkinter import *
from finquant.portfolio import build_portfolio
from scipy import stats
import scipy.stats as ss
import seaborn as sns
import pylab as py
import statsmodels.api as sm
import matplotlib.mlab as mlab
from tabulate import tabulate
##############
### Seed
##############
# # date provvisorie
# start="2018-1-1"
# end="2020-9-10"

###############################################################################
### Creazione finestra di apertura ############################################
###############################################################################
window = tk.Tk()
window.geometry("700x750+830+0")
window.title("Scaricare Serie Storiche")
window.grid_columnconfigure(0, weight=10)
window.resizable(False, False)

###############################################################################
### Interimento ticker 1 e data inizio e fine #################################
###############################################################################
insert_label = tk.Label(window,text="Inserisci Ticker 1:",\
                            font=("Helvetica",10))
insert_label.grid(row=0,column=0, sticky="W", padx=10, pady=10)
text_input = tk.Entry()
text_input.grid(row=0, column=1, sticky="W", pady=10, padx=10)
###############################################################################
### Interimento ticker 2 e data inizio e fine #################################
###############################################################################
insert_label2 = tk.Label(window,text="Inserisci Ticker 2:",\
                            font=("Helvetica",10))
insert_label2.grid(row=1,column=0, sticky="NW", padx=10, pady=10)
text_input2 = tk.Entry()
text_input2.grid(row=1, column=1, sticky="N", pady=10, padx=10)
###############################################################################
### Interimento ticker 3 e data inizio e fine #################################
###############################################################################
insert_label3 = tk.Label(window,text="Inserisci Ticker 3:",\
                            font=("Helvetica",10))
insert_label3.grid(row=2,column=0, sticky="NW", padx=10, pady=10)
text_input3 = tk.Entry()
text_input3.grid(row=2, column=1, sticky="N", pady=10, padx=10)
###############################################################################
### Interimento ticker 4 e data inizio e fine #################################
###############################################################################
insert_label4 = tk.Label(window,text="Inserisci Ticker 4:",\
                            font=("Helvetica",10))
insert_label4.grid(row=3,column=0, sticky="NW", padx=10, pady=10)
text_input4 = tk.Entry()
text_input4.grid(row=3, column=1, sticky="N", pady=10, padx=10)
###############################################################################
### Interimento ticker 5 e data inizio e fine #################################
###############################################################################
insert_label5 = tk.Label(window,text="Inserisci Ticker 5:",\
                            font=("Helvetica",10))
insert_label5.grid(row=4,column=0, sticky="NW", padx=10, pady=10)
text_input5 = tk.Entry()
text_input5.grid(row=4, column=1, sticky="N", pady=10, padx=10)
###############################################################################
### Interimento StartDate #####################################################
###############################################################################
insert_labelS = tk.Label(window,text="Inserisci Data Inizio Rilevazione: (Y,M,D)",\
                            font=("Helvetica",10))
insert_labelS.grid(row=5,column=0, sticky="NW", padx=10, pady=10)
text_input6 = tk.Entry()
text_input6.grid(row=5, column=1, sticky="N", pady=10, padx=10)
text_input61 = tk.Entry()
text_input61.grid(row=5, column=2, sticky="N", pady=10, padx=10)
text_input62 = tk.Entry()
text_input62.grid(row=5, column=3, sticky="N", pady=10, padx=10)
###############################################################################
### InterimentoEndDate ########################################################
###############################################################################
insert_labelE = tk.Label(window,text="Inserisci Data Fine Rilevazione: (Y,M,D)",\
                          font=("Helvetica",10))
insert_labelE.grid(row=6,column=0, sticky="NW", padx=10, pady=10)
text_input7 = tk.Entry()
text_input7.grid(row=6, column=1, sticky="N", pady=10, padx=10)
text_input71 = tk.Entry()
text_input71.grid(row=6, column=2, sticky="N", pady=10, padx=10)
text_input72 = tk.Entry()
text_input72.grid(row=6, column=3, sticky="N", pady=10, padx=10)
###############################################################################
### Inserimento N° Azioni/ Composizione del portafoglio #######################
###############################################################################
N_Az1_label = tk.Label(window, text="Inserisci N. Azioni T1: ")
N_Az1_label.grid(row=0,column=2,sticky="WE",pady=10)
N_Az1_input = tk.Entry()
N_Az1_input.grid(row=0, column=3, sticky="N", pady=10, padx=10)
N_Az2_label = tk.Label(window, text="Inserisci N. Azioni T2: ")
N_Az2_label.grid(row=1,column=2,sticky="WE",pady=10)
N_Az2_input = tk.Entry()
N_Az2_input.grid(row=1, column=3, sticky="N", pady=10, padx=10)
N_Az3_label = tk.Label(window, text="Inserisci N. Azioni T3: ")
N_Az3_label.grid(row=2,column=2,sticky="WE",pady=10)
N_Az3_input = tk.Entry()
N_Az3_input.grid(row=2, column=3, sticky="N", pady=10, padx=10)
N_Az4_label = tk.Label(window, text="Inserisci N. Azioni T4: ")
N_Az4_label.grid(row=3,column=2,sticky="WE",pady=10)
N_Az4_input = tk.Entry()
N_Az4_input.grid(row=3, column=3, sticky="N", pady=10, padx=10)
N_Az5_label = tk.Label(window, text="Inserisci N. Azioni T5: ")
N_Az5_label.grid(row=4,column=2,sticky="WE",pady=10)
N_Az5_input = tk.Entry()
N_Az5_input.grid(row=4, column=3, sticky="N", pady=10, padx=10)
###############################################################################
### Funzione Analisi Preliminare ##############################################
###############################################################################
def Analisi_Preliminare():
    ##########################################################################
    ## Acquisizione Date Inizio e Fine Rilevazione ###########################
    ##########################################################################
    user_inputSA = text_input6.get()
    user_inputSM = text_input61.get()
    user_inputSD = text_input62.get()
    user_inputEA = text_input7.get()
    user_inputEM = text_input71.get()
    user_inputED = text_input72.get()
    start = user_inputSA + "-" + user_inputSM + "-" + user_inputSD
    end = user_inputEA + "-" + user_inputEM + "-" + user_inputED
    ###########################################################################
    ### Fine Acquisizione Date Inizio e Fine Rilevazione ######################
    ###########################################################################
    if text_input.get():
        if text_input2.get():
            if text_input3.get():
                if text_input4.get():
                    if text_input5.get():
                        user_input1 = text_input.get()
                        user_input2 = text_input2.get()
                        user_input3 = text_input3.get()
                        user_input4 = text_input4.get()
                        user_input5 = text_input5.get()
                        user_input = [user_input1, user_input2, user_input3,user_input4,user_input5]
                        df = web.DataReader(user_input, "yahoo", start, end).dropna()
                        data = df["Adj Close"]
                        LogReturn = np.log(data/data.shift(1))
                        Stat = LogReturn.describe()
                        CovMatrix = LogReturn.cov()
                        ################################################################
                        ## Plot Price & Daily LogReturn ################################
                        ################################################################
                        fig1 = plt.figure(1)
                        plt.subplot(231)
                        data.iloc[:,0].plot()
                        plt.title("%s Adj. Closing Price" % str.title(user_input[0]))
                        plt.ylabel("Price")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.subplot(232)
                        data.iloc[:,1].plot()
                        plt.title("%s Adj. Closing Price" % str.title(user_input[1]))
                        plt.ylabel("Price")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.subplot(233)
                        data.iloc[:,2].plot()
                        plt.title("%s Adj. Closing Price" % str.title(user_input[2]))
                        plt.ylabel("Price")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.subplot(234)
                        data.iloc[:,3].plot()
                        plt.title("%s Adj. Closing Price" % str.title(user_input[3]))
                        plt.ylabel("Price")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.subplot(235)
                        data.iloc[:,4].plot()
                        plt.title("%s Adj. Closing Price" % str.title(user_input[4]))
                        plt.ylabel("Price")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.tight_layout()
                        fig1.show()
                        ### Log-Return plot
                        fig2 = plt.figure(2)
                        plt.subplot(231)
                        LogReturn.iloc[:,0].plot()
                        plt.title("%s LogReturn" % str.title(user_input[0]))
                        plt.ylabel("LogReturn")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.subplot(232)
                        LogReturn.iloc[:,1].plot()
                        plt.title("%s LogReturn" % str.title(user_input[1]))
                        plt.ylabel("LogReturn")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.subplot(233)
                        LogReturn.iloc[:,2].plot()
                        plt.title("%s LogReturn" % str.title(user_input[2]))
                        plt.ylabel("LogReturn")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.subplot(234)
                        LogReturn.iloc[:,3].plot()
                        plt.title("%s LogReturn" % str.title(user_input[3]))
                        plt.ylabel("LogReturn")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.subplot(235)
                        LogReturn.iloc[:,4].plot()
                        plt.title("%s LogReturn" % str.title(user_input[4]))
                        plt.ylabel("LogReturn")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.tight_layout()
                        fig2.show()

                    else:
                        user_input1 = text_input.get()
                        user_input2 = text_input2.get()
                        user_input3 = text_input3.get()
                        user_input4 = text_input4.get()
                        user_input = [user_input1, user_input2, user_input3,user_input4]
                        df = web.DataReader(user_input, "yahoo", start, end).dropna()
                        data = df["Adj Close"]
                        LogReturn = np.log(data/data.shift(1))
                        Stat = LogReturn.describe()
                        CovMatrix = LogReturn.cov()
                        ################################################################
                        ## Plot Return, Daily Log e Daily Ret ##########################
                        ################################################################
                        fig3 = plt.figure(3)
                        plt.subplot(221)
                        data.iloc[:,0].plot()
                        plt.title("%s Adj. Closing Price" % str.title(user_input[0]))
                        plt.ylabel("Price")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.subplot(222)
                        data.iloc[:,1].plot()
                        plt.title("%s Adj. Closing Price" % str.title(user_input[1]))
                        plt.ylabel("Price")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.subplot(223)
                        data.iloc[:,2].plot()
                        plt.title("%s Adj. Closing Price" % str.title(user_input[2]))
                        plt.ylabel("Price")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.subplot(224)
                        data.iloc[:,3].plot()
                        plt.title("%s Adj. Closing Price" % str.title(user_input[3]))
                        plt.ylabel("Price")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.tight_layout()
                        fig3.show()
                        ### Log-Return plot
                        fig4 = plt.figure(4)
                        plt.subplot(221)
                        LogReturn.iloc[:,0].plot()
                        plt.title("%s LogReturn" % str.title(user_input[0]))
                        plt.ylabel("LogReturn")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.subplot(222)
                        LogReturn.iloc[:,1].plot()
                        plt.title("%s LogReturn" % str.title(user_input[1]))
                        plt.ylabel("LogReturn")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.subplot(223)
                        LogReturn.iloc[:,2].plot()
                        plt.title("%s LogReturn" % str.title(user_input[2]))
                        plt.ylabel("LogReturn")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.subplot(224)
                        LogReturn.iloc[:,3].plot()
                        plt.title("%s LogReturn" % str.title(user_input[3]))
                        plt.ylabel("LogReturn")
                        plt.xlabel("Date")
                        plt.grid()
                        plt.tight_layout()
                        fig4.show()
                else:
                    user_input1 = text_input.get()
                    user_input2 = text_input2.get()
                    user_input3 = text_input3.get()
                    user_input = [user_input1, user_input2, user_input3]
                    df = web.DataReader(user_input, "yahoo", start, end).dropna()
                    data = df["Adj Close"]
                    LogReturn = np.log(data/data.shift(1))
                    Stat = LogReturn.describe()
                    CovMatrix = LogReturn.cov()
                    StatA = Stat.to_numpy()
                    Skew = LogReturn.skew().to_numpy()
                    Kurt = LogReturn.kurtosis().to_numpy()
                    ################################################################
                    ## Plot Return, Daily Log e Daily Ret ##########################
                    ################################################################
                    fig5 = plt.figure(5)
                    plt.subplot(221)
                    data.iloc[:,0].plot()
                    plt.title("%s Adj. Closing Price" % str.title(user_input[0]))
                    plt.ylabel("Price")
                    plt.xlabel("Date")
                    plt.grid()
                    plt.subplot(222)
                    data.iloc[:,1].plot()
                    plt.title("%s Adj. Closing Price" % str.title(user_input[1]))
                    plt.ylabel("Price")
                    plt.xlabel("Date")
                    plt.grid()
                    plt.subplot(223)
                    data.iloc[:,2].plot()
                    plt.title("%s Adj. Closing Price" % str.title(user_input[2]))
                    plt.ylabel("Price")
                    plt.xlabel("Date")
                    plt.grid()
                    plt.tight_layout()
                    fig5.show()
                    ### Log-Return plot
                    fig6 = plt.figure(6)
                    plt.subplot(221)
                    LogReturn.iloc[:,0].plot()
                    plt.title("%s LogReturn" % str.title(user_input[0]))
                    plt.ylabel("LogReturn")
                    plt.xlabel("Date")
                    plt.grid()
                    plt.subplot(222)
                    LogReturn.iloc[:,1].plot()
                    plt.title("%s LogReturn" % str.title(user_input[1]))
                    plt.ylabel("LogReturn")
                    plt.xlabel("Date")
                    plt.grid()
                    plt.subplot(223)
                    LogReturn.iloc[:,2].plot()
                    plt.title("%s LogReturn" % str.title(user_input[2]))
                    plt.ylabel("LogReturn")
                    plt.xlabel("Date")
                    plt.grid()
                    plt.tight_layout()
                    fig6.show()
            else:
                user_input1 = text_input.get()
                user_input2 = text_input2.get()
                user_input = [user_input1, user_input2]
                df = web.DataReader(user_input, "yahoo", start, end).dropna()
                data = df["Adj Close"]
                LogReturn = np.log(data/data.shift(1))
                Stat = LogReturn.describe()
                CovMatrix = LogReturn.cov()
                StatA = Stat.to_numpy()
                Skew = LogReturn.skew().to_numpy()
                Kurt = LogReturn.kurtosis().to_numpy()
                ###################################################################
                ## Plot Return, Daily Log e Daily Ret #############################
                ###################################################################
                fig7 = plt.figure(7)
                plt.subplot(221)
                data.iloc[:,0].plot()
                plt.title("%s Adj. Closing Price" % str.title(user_input[0]))
                plt.ylabel("Price")
                plt.xlabel("Date")
                plt.grid()
                plt.subplot(222)
                data.iloc[:,1].plot()
                plt.title("%s Adj. Closing Price" % str.title(user_input[1]))
                plt.ylabel("Price")
                plt.xlabel("Date")
                plt.grid()
                plt.subplot(223)
                LogReturn.iloc[:,0].plot()
                plt.title("%s LogReturn" % str.title(user_input[0]))
                plt.ylabel("LogReturn")
                plt.xlabel("Date")
                plt.grid()
                plt.subplot(224)
                LogReturn.iloc[:,1].plot()
                plt.title("%s LogReturn" % str.title(user_input[1]))
                plt.ylabel("LogReturn")
                plt.xlabel("Date")
                plt.grid()
                plt.tight_layout()
                fig7.show()
        else:
            user_input = text_input.get()  #variabile con dentro il ticker
            df = web.DataReader(user_input, "yahoo", start, end).dropna()
            data = df["Adj Close"]
            LogReturn = np.log(data/data.shift(1))
            Stat = LogReturn.describe()
            # print(data1.head())
            ###################################################################
            ## Plot Return, Daily Log e Daily Ret #############################
            ###################################################################
            fig8 = plt.figure(8)
            plt.subplot(211)
            data.plot()
            plt.title("%s Adj. Closing Price" % str.title(user_input))
            plt.ylabel("Price")
            plt.xlabel("Date")
            plt.grid()
            plt.subplot(212)
            LogReturn.plot()
            plt.title("%s LogReturn" % str.title(user_input))
            plt.ylabel("LogReturn")
            plt.xlabel("Date")
            plt.grid()
            plt.tight_layout()
            fig8.show()
    else:
        pass
    ### Visualizzazione Statistiche Principali
    Win_Stat = Tk()
    Win_Stat.title("Statistiche Singoli Titoli")
    Win_Stat.grid_columnconfigure(0, weight=10)
    Win_Stat.resizable(False, False)
    Label1=Label(Win_Stat,text = "#########  Statistiche Titoli Scelti  #########")
    Label1.grid(row=1,column=1,columnspan=6)
    Label11=Label(Win_Stat)
    Label11["text"] = Stat
    Label11.grid(row=2,column=1,columnspan=6, rowspan=9)
    Label2=Label(Win_Stat,text = "################################################")
    Label2.grid(row=12,column=1,columnspan=6)
    Label21=Label(Win_Stat)
    Label2=Label(Win_Stat,text = "########  Matrice Varianze e Covarianze  #########")
    Label2.grid(row=13,column=1,columnspan=6)
    Label21=Label(Win_Stat)
    Label21["text"] = CovMatrix
    Label21.grid(row=14,column=1,columnspan=6, rowspan=9)
def Analisi_Portafoglio():
    ###########################################################################
    ### Acquisizione Date Inizio e Fine Rilevazione ###########################
    ###########################################################################
    user_inputSA = text_input6.get()
    user_inputSM = text_input61.get()
    user_inputSD = text_input62.get()
    user_inputEA = text_input7.get()
    user_inputEM = text_input71.get()
    user_inputED = text_input72.get()
    start = user_inputSA + "-" + user_inputSM + "-" + user_inputSD
    end = user_inputEA + "-" + user_inputEM + "-" + user_inputED
    ##########################################################################
    ## Fine Acquisizione Date Inizio e Fine Rilevazione ######################
    ##########################################################################
    if N_Az1_input.get():
        if N_Az2_input.get():
            if N_Az3_input.get():
                if N_Az4_input.get():
                    if N_Az5_input.get():               ## Portafoglio composto da 5 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        n5 = int(N_Az5_input.get())
                        nt = n1 + n2 + n3 + n4 + n5
                        wn = np.array([n1, n2 ,n3 ,n4 ,n5])
                        w = wn / nt
                        if text_input.get():
                            if text_input2.get():
                                if text_input3.get():
                                    if text_input4.get():
                                        if text_input5.get():
                                            user_input1 = text_input.get()
                                            user_input2 = text_input2.get()
                                            user_input3 = text_input3.get()
                                            user_input4 = text_input4.get()
                                            user_input5 = text_input5.get()
                                            user_input = [user_input1, user_input2, user_input3,user_input4,user_input5]
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:                            ## Portafoglio composto da 4 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        nt = n1 + n2 + n3 + n4
                        wn = np.array([n1, n2 ,n3 ,n4])
                        w = wn / nt
                        user_input1 = text_input.get()
                        user_input2 = text_input2.get()
                        user_input3 = text_input3.get()
                        user_input4 = text_input4.get()
                        user_input = [user_input1, user_input2, user_input3,user_input4]
                else:                                 ## Portafoglio composto da 3 titoli
                    n1 = int(N_Az1_input.get())
                    n2 = int(N_Az2_input.get())
                    n3 = int(N_Az3_input.get())
                    nt = n1 + n2 + n3
                    wn = np.array([n1, n2 ,n3])
                    w = wn / nt
                    user_input1 = text_input.get()
                    user_input2 = text_input2.get()
                    user_input3 = text_input3.get()
                    user_input = [user_input1, user_input2, user_input3]
            else:                                     ## Portafoglio composto da 2 titoli
                n1 = int(N_Az1_input.get())
                n2 = int(N_Az2_input.get())
                nt = n1 + n2
                wn = np.array([n1, n2])
                w = wn / nt
                user_input1 = text_input.get()
                user_input2 = text_input2.get()
                user_input = [user_input1, user_input2]
        else:
            n1 = int(N_Az1_input.get())
            nt = n1
            wn = np.array([n1])
            w = wn / nt
            user_input1 = text_input.get()
            user_input = [user_input1]
    else:
        pass
    nAsset = len(user_input)
    df = web.DataReader(user_input, "yahoo", start, end).dropna()
    data = df["Adj Close"]
    LogReturn = np.log(data/data.shift(1))
    CovMatrix = LogReturn.cov()
    port = data.dot(wn)
    Port_Logret = np.log(port/port.shift(1)).dropna()
    ### varie stat del Portafoglio
    Stat = Port_Logret.describe()
    Skew = Port_Logret.skew()
    Kurt =Port_Logret.kurtosis()
    Mean = Port_Logret.mean()
    Std = Port_Logret.std()
    Variance = Std**2
    #############################################################################
    ### Grafici Vari  ###########################################################
    #############################################################################
    fig1 = plt.figure(1)
    plt.subplot(221)
    port.plot()
    plt.title("Historical Returns of Portfolio")
    plt.ylabel("Price")
    plt.xlabel("Date")
    plt.grid()
    plt.subplot(222)
    plt.title("Portfolio Distribution vs Normal Distribution")
    Port_Logret.hist(bins= 100, density=False, label="Historical Dist")
    x = np.linspace(Mean - 3*Std, Mean + 3*Std,100)
    plt.plot(x, ss.norm.pdf(x, Mean, Std), color="red", label="Normal Dist")
    plt.grid()
    plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
    ###################################
    ### Test Autocorrelation   ########
    ###################################
    plt.subplot(223)
    plt.acorr(Port_Logret, maxlags = 20)
    plt.xlabel("Lags")
    plt.ylabel("Sample Autocorrelation")
    plt.title("Portfolio Autocorrelation of Log-Return")
    plt.xlim([0,20])
    plt.grid()
    plt.subplot(224)
    plt.acorr(Port_Logret**2, maxlags = 20)
    plt.xlabel("Lags")
    plt.ylabel("Sample Autocorrelation")
    plt.title("Portfolio Autocorrelation of Log-Return^2")
    plt.xlim([0,20])
    plt.grid()
    plt.tight_layout()
    fig1.show()
    ###################################
    ### Ljung-Box Q - Test   ##
    ###################################
    LB_Qtest = sm.stats.acorr_ljungbox(Port_Logret,lags=[1,5,9,10], return_df=True)
    print(LB_Qtest)
    ##############################################################################
    ### Test Normalità  ##########################################################
    ##############################################################################
    ###################################
    ## Shapiro-Wilk test LV Conf 95%
    ###################################
    shapiro = stats.shapiro(Port_Logret)
    shapiro_pvalue = shapiro.pvalue
    shapiro_stat = shapiro.statistic
    if shapiro_pvalue <= 0.05:
        Test_Shapiro = "P_value Shapiro Test " + str(shapiro_pvalue)+"  <= 0.05 (Lv. Conf. 95%)." + "\nIpotesi Nulla e' rigettata, non puo essere considerata come distribuzione normale"
    else:
        Test_Shapiro = "P_value Shapiro Test " + str(shapiro_pvalue)+"  > 0.05 (Lv. Conf. 95%)." + "\nIpotesi Nulla accettata, puo essere considerata come distribuzione normale"
    print(Test_Shapiro)
    ###################################
    ### Jarque e Bera Test   ##
    ###################################
    jarque_bera_test = stats.jarque_bera(Port_Logret)
    JB = jarque_bera_test.statistic
    Chi_square = ss.chi2.ppf(1-.05, df=2)
    if JB <= Chi_square:
        JB_Test = "Il test Jarque e Bera restituisce un valore pari a: " + str(JB) + "\nInferiore al critical value di una Chi-Quadro con 2 gradi di liberta' a Lv di Confidenza del 95% [" + str(Chi_square) + "]\n Ipotesi normalita' accettata"
    else:
        JB_Test = "Il test Jarque e Bera restituisce un valore pari a: " + str(JB) + "\nSuperiore al critical value di una Chi-Quadro con 2 gradi di liberta' a Lv di Confidenza del 95% [" + str(Chi_square) + "]\n Ipotesi normalita' rifiutata"

    print(JB_Test)
    ###################################
    ### Variance Ratio  ##
    ###################################
    n=10
    a = port[n:len(port):n]
    b = port[0:len(port)-n:n]
    cumlogret_port = np.log(a / b.shift(1)).dropna()
    var_cumlogret = (cumlogret_port.std())**2
    VRatioTest = var_cumlogret / (n * Variance)
    VRatioT = "Il test Variance Ratio restituisce un valore pari a: " + str(VRatioTest)+ " ! "
    print(VRatioT)
    ###################################
    ### Quantile-Quantile pyplot  #####
    ###################################
    sm.qqplot(Port_Logret, line="45",loc=Mean, scale=Std)
    plt.grid()
    plt.title("Quantile-Quantile Plot (QQ-Plot)")
    plt.tight_layout()
    py.show()
def VaR90():
    ##########################################################################
    ## Acquisizione Date Inizio e Fine Rilevazione ###########################
    ##########################################################################
    user_inputSA = text_input6.get()
    user_inputSM = text_input61.get()
    user_inputSD = text_input62.get()
    user_inputEA = text_input7.get()
    user_inputEM = text_input71.get()
    user_inputED = text_input72.get()
    start = user_inputSA + "-" + user_inputSM + "-" + user_inputSD
    end = user_inputEA + "-" + user_inputEM + "-" + user_inputED
    ##########################################################################
    ## Fine Acquisizione Date Inizio e Fine Rilevazione ######################
    ##########################################################################
    if N_Az1_input.get():
        if N_Az2_input.get():
            if N_Az3_input.get():
                if N_Az4_input.get():
                    if N_Az5_input.get():               ## Portafoglio composto da 5 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        n5 = int(N_Az5_input.get())
                        nt = n1 + n2 + n3 + n4 + n5
                        wn = np.array([n1, n2 ,n3 ,n4 ,n5])
                        w = wn / nt
                        if text_input.get():
                            if text_input2.get():
                                if text_input3.get():
                                    if text_input4.get():
                                        if text_input5.get():
                                            user_input1 = text_input.get()
                                            user_input2 = text_input2.get()
                                            user_input3 = text_input3.get()
                                            user_input4 = text_input4.get()
                                            user_input5 = text_input5.get()
                                            user_input = [user_input1, user_input2, user_input3,user_input4,user_input5]
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:                            ## Portafoglio composto da 4 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        nt = n1 + n2 + n3 + n4
                        wn = np.array([n1, n2 ,n3 ,n4])
                        w = wn / nt
                        user_input1 = text_input.get()
                        user_input2 = text_input2.get()
                        user_input3 = text_input3.get()
                        user_input4 = text_input4.get()
                        user_input = [user_input1, user_input2, user_input3, user_input4]

                else:                                 ## Portafoglio composto da 3 titoli
                    n1 = int(N_Az1_input.get())
                    n2 = int(N_Az2_input.get())
                    n3 = int(N_Az3_input.get())
                    nt = n1 + n2 + n3
                    wn = np.array([n1, n2 ,n3])
                    w = wn / nt
                    user_input1 = text_input.get()
                    user_input2 = text_input2.get()
                    user_input3 = text_input3.get()
                    user_input = [user_input1, user_input2, user_input3]
            else:                                     ## Portafoglio composto da 2 titoli
                n1 = int(N_Az1_input.get())
                n2 = int(N_Az2_input.get())
                nt = n1 + n2
                wn = np.array([n1, n2])
                w = wn / nt
                user_input1 = text_input.get()
                user_input2 = text_input2.get()
                user_input = [user_input1, user_input2]
        else:
            n1 = int(N_Az1_input.get())
            nt = n1
            wn = np.array([n1])
            user_input1 = text_input.get()
            user_input = [user_input1]
    else:
        pass
    df = web.DataReader(user_input, "yahoo", start, end).dropna()
    data = df["Adj Close"]
    LogReturn = np.log(data/data.shift(1))
    port = data.dot(wn)
    Port_Logret = np.log(port/port.shift(1)).dropna()
    Mean = Port_Logret.mean()
    Std = Port_Logret.std()
    ## VaR Historical Base
    VaR90_Hbase = - Port_Logret.quantile(0.1)
    ## VaR Gaussiano
    VaR90_Norm = - ss.norm.ppf(1-0.9, Mean, Std)
    ## VaR Historical Bootstrap
    VaR90_HBoots = BootsVaR(0.9,Port_Logret)
    tabella_VaR = tabulate([["90%", VaR90_Hbase,VaR90_Norm,VaR90_HBoots]], \
                           headers=["Confidence Level", "Value at Risk Hist. Base", "Value at Risk Normal", "Value at Risk Hist. Bootstrap"])
    print(tabella_VaR)

    return VaR90_Hbase,VaR90_Norm,VaR90_HBoots
def VaR95():
    ##########################################################################
    ## Acquisizione Date Inizio e Fine Rilevazione ###########################
    ##########################################################################
    user_inputSA = text_input6.get()
    user_inputSM = text_input61.get()
    user_inputSD = text_input62.get()
    user_inputEA = text_input7.get()
    user_inputEM = text_input71.get()
    user_inputED = text_input72.get()
    start = user_inputSA + "-" + user_inputSM + "-" + user_inputSD
    end = user_inputEA + "-" + user_inputEM + "-" + user_inputED
    ##########################################################################
    ## Fine Acquisizione Date Inizio e Fine Rilevazione ######################
    ##########################################################################
    if N_Az1_input.get():
        if N_Az2_input.get():
            if N_Az3_input.get():
                if N_Az4_input.get():
                    if N_Az5_input.get():               ## Portafoglio composto da 5 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        n5 = int(N_Az5_input.get())
                        nt = n1 + n2 + n3 + n4 + n5
                        wn = np.array([n1, n2 ,n3 ,n4 ,n5])
                        w = wn / nt
                        if text_input.get():
                            if text_input2.get():
                                if text_input3.get():
                                    if text_input4.get():
                                        if text_input5.get():
                                            user_input1 = text_input.get()
                                            user_input2 = text_input2.get()
                                            user_input3 = text_input3.get()
                                            user_input4 = text_input4.get()
                                            user_input5 = text_input5.get()
                                            user_input = [user_input1, user_input2, user_input3,user_input4,user_input5]
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:                            ## Portafoglio composto da 4 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        nt = n1 + n2 + n3 + n4
                        wn = np.array([n1, n2 ,n3 ,n4])
                        w = wn / nt
                        user_input1 = text_input.get()
                        user_input2 = text_input2.get()
                        user_input3 = text_input3.get()
                        user_input4 = text_input4.get()
                        user_input = [user_input1, user_input2, user_input3, user_input4]

                else:                                 ## Portafoglio composto da 3 titoli
                    n1 = int(N_Az1_input.get())
                    n2 = int(N_Az2_input.get())
                    n3 = int(N_Az3_input.get())
                    nt = n1 + n2 + n3
                    wn = np.array([n1, n2 ,n3])
                    w = wn / nt
                    user_input1 = text_input.get()
                    user_input2 = text_input2.get()
                    user_input3 = text_input3.get()
                    user_input = [user_input1, user_input2, user_input3]
            else:                                     ## Portafoglio composto da 2 titoli
                n1 = int(N_Az1_input.get())
                n2 = int(N_Az2_input.get())
                nt = n1 + n2
                wn = np.array([n1, n2])
                w = wn / nt
                user_input1 = text_input.get()
                user_input2 = text_input2.get()
                user_input = [user_input1, user_input2]
        else:
            n1 = int(N_Az1_input.get())
            nt = n1
            wn = np.array([n1])
            user_input1 = text_input.get()
            user_input = [user_input1]
    else:
        pass
    df = web.DataReader(user_input, "yahoo", start, end).dropna()
    data = df["Adj Close"]
    LogReturn = np.log(data/data.shift(1))
    port = data.dot(wn)
    Port_Logret = np.log(port/port.shift(1)).dropna()
    Mean = Port_Logret.mean()
    Std = Port_Logret.std()
    ## VaR Historical Base
    VaR95_Hbase = - Port_Logret.quantile(0.05)
    ## VaR Gaussiano
    VaR95_Norm = - ss.norm.ppf(1-0.95, Mean, Std)
    ## VaR Historical Bootstrap
    VaR95_HBoots = BootsVaR(0.95,Port_Logret)
    tabella_VaR = tabulate([["95%", VaR95_Hbase,VaR95_Norm,VaR95_HBoots]], \
                           headers=["Confidence Level", "Value at Risk Hist. Base", "Value at Risk Normal", "Value at Risk Hist. Bootstrap"])
    print(tabella_VaR)
    return VaR95_Hbase,VaR95_Norm,VaR95_HBoots
def VaR99():
    ###########################################################################
    ## Acquisizione Date Inizio e Fine Rilevazione ###########################
    ##########################################################################
    user_inputSA = text_input6.get()
    user_inputSM = text_input61.get()
    user_inputSD = text_input62.get()
    user_inputEA = text_input7.get()
    user_inputEM = text_input71.get()
    user_inputED = text_input72.get()
    start = user_inputSA + "-" + user_inputSM + "-" + user_inputSD
    end = user_inputEA + "-" + user_inputEM + "-" + user_inputED
    ##########################################################################
    ## Fine Acquisizione Date Inizio e Fine Rilevazione ######################
    ##########################################################################
    if N_Az1_input.get():
        if N_Az2_input.get():
            if N_Az3_input.get():
                if N_Az4_input.get():
                    if N_Az5_input.get():               ## Portafoglio composto da 5 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        n5 = int(N_Az5_input.get())
                        nt = n1 + n2 + n3 + n4 + n5
                        wn = np.array([n1, n2 ,n3 ,n4 ,n5])
                        w = wn / nt
                        if text_input.get():
                            if text_input2.get():
                                if text_input3.get():
                                    if text_input4.get():
                                        if text_input5.get():
                                            user_input1 = text_input.get()
                                            user_input2 = text_input2.get()
                                            user_input3 = text_input3.get()
                                            user_input4 = text_input4.get()
                                            user_input5 = text_input5.get()
                                            user_input = [user_input1, user_input2, user_input3,user_input4,user_input5]
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:                            ## Portafoglio composto da 4 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        nt = n1 + n2 + n3 + n4
                        wn = np.array([n1, n2 ,n3 ,n4])
                        w = wn / nt
                        user_input1 = text_input.get()
                        user_input2 = text_input2.get()
                        user_input3 = text_input3.get()
                        user_input4 = text_input4.get()
                        user_input = [user_input1, user_input2, user_input3, user_input4]

                else:                                 ## Portafoglio composto da 3 titoli
                    n1 = int(N_Az1_input.get())
                    n2 = int(N_Az2_input.get())
                    n3 = int(N_Az3_input.get())
                    nt = n1 + n2 + n3
                    wn = np.array([n1, n2 ,n3])
                    w = wn / nt
                    user_input1 = text_input.get()
                    user_input2 = text_input2.get()
                    user_input3 = text_input3.get()
                    user_input = [user_input1, user_input2, user_input3]
            else:                                     ## Portafoglio composto da 2 titoli
                n1 = int(N_Az1_input.get())
                n2 = int(N_Az2_input.get())
                nt = n1 + n2
                wn = np.array([n1, n2])
                w = wn / nt
                user_input1 = text_input.get()
                user_input2 = text_input2.get()
                user_input = [user_input1, user_input2]
        else:
            n1 = int(N_Az1_input.get())
            nt = n1
            wn = np.array([n1])
            user_input1 = text_input.get()
            user_input = [user_input1]
    else:
        pass
    df = web.DataReader(user_input, "yahoo", start, end).dropna()
    data = df["Adj Close"]
    LogReturn = np.log(data/data.shift(1))
    port = data.dot(wn)
    Port_Logret = np.log(port/port.shift(1)).dropna()
    Mean = Port_Logret.mean()
    Std = Port_Logret.std()
    ## VaR Historical Base
    VaR99_Hbase = - Port_Logret.quantile(0.01)
    ## VaR Gaussiano
    VaR99_Norm = - ss.norm.ppf(1-0.99, Mean, Std)
    ## VaR Historical Bootstrap
    VaR99_HBoots = BootsVaR(0.99,Port_Logret)
    tabella_VaR = tabulate([["99%", VaR99_Hbase,VaR99_Norm,VaR99_HBoots]], \
                           headers=["Confidence Level", "Value at Risk Hist. Base", "Value at Risk Normal", "Value at Risk Hist. Bootstrap"])
    print(tabella_VaR)
    return VaR99_Hbase,VaR99_Norm,VaR99_HBoots
def RW_VaR90():
    ##########################################################################
    ## Acquisizione Date Inizio e Fine Rilevazione ###########################
    ##########################################################################
    user_inputSA = text_input6.get()
    user_inputSM = text_input61.get()
    user_inputSD = text_input62.get()
    user_inputEA = text_input7.get()
    user_inputEM = text_input71.get()
    user_inputED = text_input72.get()
    start = user_inputSA + "-" + user_inputSM + "-" + user_inputSD
    end = user_inputEA + "-" + user_inputEM + "-" + user_inputED
    ##########################################################################
    ## Fine Acquisizione Date Inizio e Fine Rilevazione ######################
    ###########################################################################
    if N_Az1_input.get():
        if N_Az2_input.get():
            if N_Az3_input.get():
                if N_Az4_input.get():
                    if N_Az5_input.get():               ## Portafoglio composto da 5 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        n5 = int(N_Az5_input.get())
                        nt = n1 + n2 + n3 + n4 + n5
                        wn = np.array([n1, n2 ,n3 ,n4 ,n5])
                        w = wn / nt
                        if text_input.get():
                            if text_input2.get():
                                if text_input3.get():
                                    if text_input4.get():
                                        if text_input5.get():
                                            user_input1 = text_input.get()
                                            user_input2 = text_input2.get()
                                            user_input3 = text_input3.get()
                                            user_input4 = text_input4.get()
                                            user_input5 = text_input5.get()
                                            user_input = [user_input1, user_input2, user_input3,user_input4,user_input5]
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:                            ## Portafoglio composto da 4 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        nt = n1 + n2 + n3 + n4
                        wn = np.array([n1, n2 ,n3 ,n4])
                        w = wn / nt
                        user_input1 = text_input.get()
                        user_input2 = text_input2.get()
                        user_input3 = text_input3.get()
                        user_input4 = text_input4.get()
                        user_input = [user_input1, user_input2, user_input3, user_input4]
                else:                                 ## Portafoglio composto da 3 titoli
                    n1 = int(N_Az1_input.get())
                    n2 = int(N_Az2_input.get())
                    n3 = int(N_Az3_input.get())
                    nt = n1 + n2 + n3
                    wn = np.array([n1, n2 ,n3])
                    w = wn / nt
                    user_input1 = text_input.get()
                    user_input2 = text_input2.get()
                    user_input3 = text_input3.get()
                    user_input = [user_input1, user_input2, user_input3]
            else:                                     ## Portafoglio composto da 2 titoli
                n1 = int(N_Az1_input.get())
                n2 = int(N_Az2_input.get())
                nt = n1 + n2
                wn = np.array([n1, n2])
                w = wn / nt
                user_input1 = text_input.get()
                user_input2 = text_input2.get()
                user_input = [user_input1, user_input2]
        else:
            n1 = int(N_Az1_input.get())
            nt = n1
            wn = np.array([n1])
            user_input1 = text_input.get()
            user_input = [user_input1]
    else:
        pass
    def VaR90(p,m,s):
        VaR90_Hbase = - p.quantile(0.1)
        VaR90_Norm = - ss.norm.ppf(1-0.9, m, s)
        VaR90_Boots = BootsVaR(0.9,p)
        return VaR90_Boots,VaR90_Norm,VaR90_Hbase
    df = web.DataReader(user_input, "yahoo", start, end).dropna()
    data = df["Adj Close"]
    LogReturn = np.log(data/data.shift(1))
    port = data.dot(wn)
    Port_Logret = np.log(port/port.shift(1)).dropna()
    s=6*20
    n = len(Port_Logret)
    P = Port_Logret.to_numpy()
    R_VaR90_B = np.zeros(n-s)
    R_VaR90_N = np.zeros(n-s)
    R_VaR90_HB = np.zeros(n-s)
    for i in range(n-s):
        sample_range = np.arange(0,s) + i
        sample_ret = Port_Logret[sample_range]
        [R_VaR90_B[i],R_VaR90_N[i],R_VaR90_HB[i]] = VaR90(sample_ret, sample_ret.mean(), sample_ret.std())
    plt.clf()
    fig9 = plt.figure(9)
    plt.plot(-R_VaR90_B, color="purple", label="Bootstrap VaR")
    plt.plot(-R_VaR90_N, color="black", label ="Normal VaR")
    plt.plot(-R_VaR90_HB, color="green", label="Historical VaR")
    plt.plot(P[s:n],"ro", markersize= 1)
    plt.title("Rolling Window VaR C.LvL 90%")
    plt.ylabel("VaR-LogReturn")
    plt.xlabel("N° Osservazione")
    plt.legend()
    plt.grid()
    plt.xlim(0)
    fig9.show()
def RW_VaR95():
    ##########################################################################
    ## Acquisizione Date Inizio e Fine Rilevazione ###########################
    ##########################################################################
    user_inputSA = text_input6.get()
    user_inputSM = text_input61.get()
    user_inputSD = text_input62.get()
    user_inputEA = text_input7.get()
    user_inputEM = text_input71.get()
    user_inputED = text_input72.get()
    start = user_inputSA + "-" + user_inputSM + "-" + user_inputSD
    end = user_inputEA + "-" + user_inputEM + "-" + user_inputED
    ##########################################################################
    ## Fine Acquisizione Date Inizio e Fine Rilevazione ######################
    ###########################################################################
    if N_Az1_input.get():
        if N_Az2_input.get():
            if N_Az3_input.get():
                if N_Az4_input.get():
                    if N_Az5_input.get():               ## Portafoglio composto da 5 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        n5 = int(N_Az5_input.get())
                        nt = n1 + n2 + n3 + n4 + n5
                        wn = np.array([n1, n2 ,n3 ,n4 ,n5])
                        w = wn / nt
                        if text_input.get():
                            if text_input2.get():
                                if text_input3.get():
                                    if text_input4.get():
                                        if text_input5.get():
                                            user_input1 = text_input.get()
                                            user_input2 = text_input2.get()
                                            user_input3 = text_input3.get()
                                            user_input4 = text_input4.get()
                                            user_input5 = text_input5.get()
                                            user_input = [user_input1, user_input2, user_input3,user_input4,user_input5]
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:                            ## Portafoglio composto da 4 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        nt = n1 + n2 + n3 + n4
                        wn = np.array([n1, n2 ,n3 ,n4])
                        w = wn / nt
                        user_input1 = text_input.get()
                        user_input2 = text_input2.get()
                        user_input3 = text_input3.get()
                        user_input4 = text_input4.get()
                        user_input = [user_input1, user_input2, user_input3, user_input4]
                else:                                 ## Portafoglio composto da 3 titoli
                    n1 = int(N_Az1_input.get())
                    n2 = int(N_Az2_input.get())
                    n3 = int(N_Az3_input.get())
                    nt = n1 + n2 + n3
                    wn = np.array([n1, n2 ,n3])
                    w = wn / nt
                    user_input1 = text_input.get()
                    user_input2 = text_input2.get()
                    user_input3 = text_input3.get()
                    user_input = [user_input1, user_input2, user_input3]
            else:                                     ## Portafoglio composto da 2 titoli
                n1 = int(N_Az1_input.get())
                n2 = int(N_Az2_input.get())
                nt = n1 + n2
                wn = np.array([n1, n2])
                w = wn / nt
                user_input1 = text_input.get()
                user_input2 = text_input2.get()
                user_input = [user_input1, user_input2]
        else:
            n1 = int(N_Az1_input.get())
            nt = n1
            wn = np.array([n1])
            user_input1 = text_input.get()
            user_input = [user_input1]
    else:
        pass
    def VaR95(p,m,s):
        VaR95_Hbase = - p.quantile(0.05)
        VaR95_Norm = - ss.norm.ppf(1-0.95, m, s)
        VaR95_Boots = BootsVaR(0.95,p)
        return VaR95_Boots,VaR95_Norm,VaR95_Hbase
    df = web.DataReader(user_input, "yahoo", start, end).dropna()
    data = df["Adj Close"]
    LogReturn = np.log(data/data.shift(1))
    port = data.dot(wn)
    Port_Logret = np.log(port/port.shift(1)).dropna()
    s=6*20
    n = len(Port_Logret)
    P = Port_Logret.to_numpy()
    R_VaR95_B = np.zeros(n-s)
    R_VaR95_N = np.zeros(n-s)
    R_VaR95_HB = np.zeros(n-s)
    for i in range(n-s):
        sample_range = np.arange(0,s) + i
        sample_ret = Port_Logret[sample_range]
        [R_VaR95_B[i],R_VaR95_N[i],R_VaR95_HB[i]] = VaR95(sample_ret, sample_ret.mean(), sample_ret.std())
    plt.clf()
    fig10 = plt.figure(10)
    plt.plot(-R_VaR95_B, color="purple", label="Bootstrap VaR")
    plt.plot(-R_VaR95_N, color="black", label ="Normal VaR")
    plt.plot(-R_VaR95_HB, color="green", label="Historical VaR")
    plt.plot(P[s:n],"ro", markersize= 1)
    plt.title("Rolling Window VaR C.LvL 95%")
    plt.ylabel("VaR-LogReturn")
    plt.xlabel("N° Osservazione")
    plt.legend()
    plt.grid()
    plt.xlim(0)
    fig10.show()
def RW_VaR99():
    ##########################################################################
    ## Acquisizione Date Inizio e Fine Rilevazione ###########################
    ##########################################################################
    user_inputSA = text_input6.get()
    user_inputSM = text_input61.get()
    user_inputSD = text_input62.get()
    user_inputEA = text_input7.get()
    user_inputEM = text_input71.get()
    user_inputED = text_input72.get()
    start = user_inputSA + "-" + user_inputSM + "-" + user_inputSD
    end = user_inputEA + "-" + user_inputEM + "-" + user_inputED
    ##########################################################################
    ## Fine Acquisizione Date Inizio e Fine Rilevazione ######################
    ##########################################################################
    if N_Az1_input.get():
        if N_Az2_input.get():
            if N_Az3_input.get():
                if N_Az4_input.get():
                    if N_Az5_input.get():               ## Portafoglio composto da 5 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        n5 = int(N_Az5_input.get())
                        nt = n1 + n2 + n3 + n4 + n5
                        wn = np.array([n1, n2 ,n3 ,n4 ,n5])
                        w = wn / nt
                        if text_input.get():
                            if text_input2.get():
                                if text_input3.get():
                                    if text_input4.get():
                                        if text_input5.get():
                                            user_input1 = text_input.get()
                                            user_input2 = text_input2.get()
                                            user_input3 = text_input3.get()
                                            user_input4 = text_input4.get()
                                            user_input5 = text_input5.get()
                                            user_input = [user_input1, user_input2, user_input3,user_input4,user_input5]
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:                            ## Portafoglio composto da 4 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        nt = n1 + n2 + n3 + n4
                        wn = np.array([n1, n2 ,n3 ,n4])
                        w = wn / nt
                        user_input1 = text_input.get()
                        user_input2 = text_input2.get()
                        user_input3 = text_input3.get()
                        user_input4 = text_input4.get()
                        user_input = [user_input1, user_input2, user_input3, user_input4]
                else:                                 ## Portafoglio composto da 3 titoli
                    n1 = int(N_Az1_input.get())
                    n2 = int(N_Az2_input.get())
                    n3 = int(N_Az3_input.get())
                    nt = n1 + n2 + n3
                    wn = np.array([n1, n2 ,n3])
                    w = wn / nt
                    user_input1 = text_input.get()
                    user_input2 = text_input2.get()
                    user_input3 = text_input3.get()
                    user_input = [user_input1, user_input2, user_input3]
            else:                                     ## Portafoglio composto da 2 titoli
                n1 = int(N_Az1_input.get())
                n2 = int(N_Az2_input.get())
                nt = n1 + n2
                wn = np.array([n1, n2])
                w = wn / nt
                user_input1 = text_input.get()
                user_input2 = text_input2.get()
                user_input = [user_input1, user_input2]
        else:
            n1 = int(N_Az1_input.get())
            nt = n1
            wn = np.array([n1])
            user_input1 = text_input.get()
            user_input = [user_input1]
    else:
        pass
    def VaR99(p,m,s):
        VaR99_Hbase = - p.quantile(0.01)
        VaR99_Norm = - ss.norm.ppf(1-0.99, m, s)
        VaR99_Boots = BootsVaR(0.99,p)
        return VaR99_Boots,VaR99_Norm,VaR99_Hbase
    df = web.DataReader(user_input, "yahoo", start, end).dropna()
    data = df["Adj Close"]
    LogReturn = np.log(data/data.shift(1))
    port = data.dot(wn)
    Port_Logret = np.log(port/port.shift(1)).dropna()
    s=6*20
    n = len(Port_Logret)
    P = Port_Logret.to_numpy()
    R_VaR99_B = np.zeros(n-s)
    R_VaR99_N = np.zeros(n-s)
    R_VaR99_HB = np.zeros(n-s)
    for i in range(n-s):
        sample_range = np.arange(0,s) + i
        sample_ret = Port_Logret[sample_range]
        [R_VaR99_B[i],R_VaR99_N[i],R_VaR99_HB[i]] = VaR99(sample_ret, sample_ret.mean(), sample_ret.std())
    plt.clf()
    fig11 = plt.figure(11)
    plt.plot(-R_VaR99_B, color="purple", label="Bootstrap VaR")
    plt.plot(-R_VaR99_N, color="black", label ="Normal VaR")
    plt.plot(-R_VaR99_HB, color="green", label="Historical VaR")
    plt.plot(P[s:n],"ro", markersize= 1)
    plt.title("Rolling Window VaR C.LvL 99%")
    plt.ylabel("VaR-LogReturn")
    plt.xlabel("N° Osservazione")
    plt.legend()
    plt.grid()
    plt.xlim(0)
    fig11.show()
def BootsVaR(cl,p):
    nb= 10
    VaR_boot = np.zeros(nb)
    for j in range(nb):
        sim_ret = np.random.choice(p, size = len(p))
        VaR_boot[j] = - np.quantile(sim_ret,1-cl)
    return VaR_boot.mean()
def V_VaR90():
    ##########################################################################
    ## Acquisizione Date Inizio e Fine Rilevazione ###########################
    ##########################################################################
    user_inputSA = text_input6.get()
    user_inputSM = text_input61.get()
    user_inputSD = text_input62.get()
    user_inputEA = text_input7.get()
    user_inputEM = text_input71.get()
    user_inputED = text_input72.get()
    start = user_inputSA + "-" + user_inputSM + "-" + user_inputSD
    end = user_inputEA + "-" + user_inputEM + "-" + user_inputED
    ##########################################################################
    ## Fine Acquisizione Date Inizio e Fine Rilevazione ######################
    ##########################################################################
    if N_Az1_input.get():
        if N_Az2_input.get():
            if N_Az3_input.get():
                if N_Az4_input.get():
                    if N_Az5_input.get():   ## Portafoglio composto da 5 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        n5 = int(N_Az5_input.get())
                        nt = n1 + n2 + n3 + n4 + n5
                        wn = np.array([n1, n2 ,n3 ,n4 ,n5])
                        w = wn / nt
                        if text_input.get():
                            if text_input2.get():
                                if text_input3.get():
                                    if text_input4.get():
                                        if text_input5.get():
                                            user_input1 = text_input.get()
                                            user_input2 = text_input2.get()
                                            user_input3 = text_input3.get()
                                            user_input4 = text_input4.get()
                                            user_input5 = text_input5.get()
                                            user_input = [user_input1, \
                                                          user_input2, \
                                                          user_input3, \
                                                          user_input4, \
                                                          user_input5]
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:                  ## Portafoglio composto da 4 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        nt = n1 + n2 + n3 + n4
                        wn = np.array([n1, n2 ,n3 ,n4])
                        w = wn / nt
                        user_input1 = text_input.get()
                        user_input2 = text_input2.get()
                        user_input3 = text_input3.get()
                        user_input4 = text_input4.get()
                        user_input = [user_input1, user_input2, user_input3,\
                                      user_input4]
                else:                      ## Portafoglio composto da 3 titoli
                    n1 = int(N_Az1_input.get())
                    n2 = int(N_Az2_input.get())
                    n3 = int(N_Az3_input.get())
                    nt = n1 + n2 + n3
                    wn = np.array([n1, n2 ,n3])
                    w = wn / nt
                    user_input1 = text_input.get()
                    user_input2 = text_input2.get()
                    user_input3 = text_input3.get()
                    user_input = [user_input1, user_input2, user_input3]
            else:                          ## Portafoglio composto da 2 titoli
                n1 = int(N_Az1_input.get())
                n2 = int(N_Az2_input.get())
                nt = n1 + n2
                wn = np.array([n1, n2])
                w = wn / nt
                user_input1 = text_input.get()
                user_input2 = text_input2.get()
                user_input = [user_input1, user_input2]
        else:
            n1 = int(N_Az1_input.get())
            nt = n1
            wn = np.array([n1])
            user_input1 = text_input.get()
            user_input = [user_input1]
    else:
        pass
    def VaR90(p,m,s):
        VaR90_Hbase = - p.quantile(0.1)
        VaR90_Norm = - ss.norm.ppf(1-0.9, m, s)
        VaR90_Boots = BootsVaR(0.9,p)
        return VaR90_Boots,VaR90_Norm,VaR90_Hbase
    df = web.DataReader(user_input, "yahoo", start, end).dropna()
    data = df["Adj Close"]
    LogReturn = np.log(data/data.shift(1))
    port = data.dot(wn)
    Port_Logret = np.log(port/port.shift(1)).dropna()
    s=6*20
    n = len(Port_Logret)
    P = Port_Logret.to_numpy()
    R_VaR90_B = np.zeros(n-s)
    R_VaR90_N = np.zeros(n-s)
    R_VaR90_HB = np.zeros(n-s)
    for i in range(n-s):
        sample_range = np.arange(0,s) + i
        sample_ret = Port_Logret[sample_range]
        [R_VaR90_B[i],R_VaR90_N[i],R_VaR90_HB[i]] = VaR90(sample_ret,\
                                                          sample_ret.mean(),\
                                                          sample_ret.std())
    ############################################################################
    ##### Calcolo violazioni al  90% VaR Bootstrap
    vb = 0
    vn = 0
    n = len(Port_Logret)
    violB = np.zeros(n-s)
    violN = np.zeros(n-s)
    for i in range(n-s):
        if Port_Logret[s+i] < -R_VaR90_B[i]:
            vb = vb + 1
            violB[i] = 1
        else:
            vb = vb + 0
            violB[i] = 0

    for i in range(n-s):
        if Port_Logret[s+i] < -R_VaR90_N[i]:
            vn = vn + 1
            violN[i] = 1
        else:
            vn = vn + 0
            violN[i] = 0
    ## Print n violazioni
    # print("N Violazioni al Bootstrap VaR 90% : " + str(vb) + " ")
    # print("N Violazioni al Normal VaR 90% : " + str(vn) + " ")
    ##########################################################################
    ### Test di Kupiec #######################################################
    ##########################################################################
    Kupiec(Port_Logret,vb,vn,0.9)
    LRlogB = Kupiec(Port_Logret,vb,vn,0.9)[0]
    LRlogN = Kupiec(Port_Logret,vb,vn,0.9)[1]
    tbk = Kupiec(Port_Logret,vb,vn,0.9)[2]
    tnk = Kupiec(Port_Logret,vb,vn,0.9)[3]
    ##########################################################################
    ### Test di Christoffersen ###############################################
    ##########################################################################
    Christoffersen(violN,violB)
    LRindb = Christoffersen(violN,violB)[0]
    LRindg = Christoffersen(violN,violB)[1]
    cbk = Christoffersen(violN,violB)[2]
    cnk = Christoffersen(violN,violB)[3]
    ##########################################################################
    ### Test di Christoffersen ###############################################
    ##########################################################################
    Con_Coverage(LRindb,LRlogB,LRlogN,LRindg,0.90)
    ccbk = Con_Coverage(LRindb,LRlogB,LRlogN,LRindg,0.90)[0]
    ccnk = Con_Coverage(LRindb,LRlogB,LRlogN,LRindg,0.90)[1]
    ## Grafici violazioni#####################################################
    plt.clf()
    plt.subplot(121)
    plt.plot(violB)
    plt.title("Bootstrap VaR 90% Violations")
    plt.ylim([0,1])
    plt.xlim([0,n-s])
    plt.subplot(122)
    plt.plot(violN)
    plt.title("Normal VaR 90% Violations")
    plt.ylim([0,1])
    plt.xlim([0,n-s])
    plt.tight_layout()
    plt.show(block=False)
    ##########################################################################
    ### Stampa Test e Violazioni #############################################
    ##########################################################################
    table = [('Typo VaR 90%', 'N. Violazioni', "T. Kupiec", "Christoffersen",\
             "Conditional Coverage"),
             ("Gaussian", vn, tnk, cnk, ccnk),
             ("Bootstrap", vb, tbk, cbk, ccbk)]

    class TabulateLabel(tk.Label):
        def __init__(self, parent, table, **kwargs):
            super().__init__(parent,
                             font=('Consolas', 10),
                             justify=tk.LEFT, anchor='nw', **kwargs)

            text = tabulate(table, headers='firstrow', tablefmt='github', showindex=False,numalign="left")
            self.configure(text=text)


    class App(tk.Tk):
        def __init__(self):
            super().__init__()
            TabulateLabel(self, table=table, bg='white').grid(sticky='ew')

    if __name__ == "__main__":
        App().mainloop()
def V_VaR95():
    ##########################################################################
    ## Acquisizione Date Inizio e Fine Rilevazione ###########################
    ##########################################################################
    user_inputSA = text_input6.get()
    user_inputSM = text_input61.get()
    user_inputSD = text_input62.get()
    user_inputEA = text_input7.get()
    user_inputEM = text_input71.get()
    user_inputED = text_input72.get()
    start = user_inputSA + "-" + user_inputSM + "-" + user_inputSD
    end = user_inputEA + "-" + user_inputEM + "-" + user_inputED
    ##########################################################################
    ## Fine Acquisizione Date Inizio e Fine Rilevazione ######################
    ###########################################################################
    if N_Az1_input.get():
        if N_Az2_input.get():
            if N_Az3_input.get():
                if N_Az4_input.get():
                    if N_Az5_input.get():   ## Portafoglio composto da 5 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        n5 = int(N_Az5_input.get())
                        nt = n1 + n2 + n3 + n4 + n5
                        wn = np.array([n1, n2 ,n3 ,n4 ,n5])
                        w = wn / nt
                        if text_input.get():
                            if text_input2.get():
                                if text_input3.get():
                                    if text_input4.get():
                                        if text_input5.get():
                                            user_input1 = text_input.get()
                                            user_input2 = text_input2.get()
                                            user_input3 = text_input3.get()
                                            user_input4 = text_input4.get()
                                            user_input5 = text_input5.get()
                                            user_input = [user_input1, \
                                                          user_input2, \
                                                          user_input3, \
                                                          user_input4, \
                                                          user_input5]
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:                  ## Portafoglio composto da 4 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        nt = n1 + n2 + n3 + n4
                        wn = np.array([n1, n2 ,n3 ,n4])
                        w = wn / nt
                        user_input1 = text_input.get()
                        user_input2 = text_input2.get()
                        user_input3 = text_input3.get()
                        user_input4 = text_input4.get()
                        user_input = [user_input1, user_input2, user_input3,\
                                      user_input4]
                else:                      ## Portafoglio composto da 3 titoli
                    n1 = int(N_Az1_input.get())
                    n2 = int(N_Az2_input.get())
                    n3 = int(N_Az3_input.get())
                    nt = n1 + n2 + n3
                    wn = np.array([n1, n2 ,n3])
                    w = wn / nt
                    user_input1 = text_input.get()
                    user_input2 = text_input2.get()
                    user_input3 = text_input3.get()
                    user_input = [user_input1, user_input2, user_input3]
            else:                          ## Portafoglio composto da 2 titoli
                n1 = int(N_Az1_input.get())
                n2 = int(N_Az2_input.get())
                nt = n1 + n2
                wn = np.array([n1, n2])
                w = wn / nt
                user_input1 = text_input.get()
                user_input2 = text_input2.get()
                user_input = [user_input1, user_input2]
        else:
            n1 = int(N_Az1_input.get())
            nt = n1
            wn = np.array([n1])
            user_input1 = text_input.get()
            user_input = [user_input1]
    else:
        pass
    def VaR95(p,m,s):
        VaR95_Hbase = - p.quantile(0.05)
        VaR95_Norm = - ss.norm.ppf(1-0.95, m, s)
        VaR95_Boots = BootsVaR(0.95,p)
        return VaR95_Boots,VaR95_Norm,VaR95_Hbase
    df = web.DataReader(user_input, "yahoo", start, end).dropna()
    data = df["Adj Close"]
    LogReturn = np.log(data/data.shift(1))
    port = data.dot(wn)
    Port_Logret = np.log(port/port.shift(1)).dropna()
    s=6*20
    n = len(Port_Logret)
    P = Port_Logret.to_numpy()
    R_VaR95_B = np.zeros(n-s)
    R_VaR95_N = np.zeros(n-s)
    R_VaR95_HB = np.zeros(n-s)
    for i in range(n-s):
        sample_range = np.arange(0,s) + i
        sample_ret = Port_Logret[sample_range]
        [R_VaR95_B[i],R_VaR95_N[i],R_VaR95_HB[i]] = VaR95(sample_ret,\
                                                          sample_ret.mean(),\
                                                          sample_ret.std())
    ############################################################################
    ##### Calcolo violazioni al  95% VaR Bootstrap
    vb = 0
    vn = 0
    n = len(Port_Logret)
    violB = np.zeros(n-s)
    violN = np.zeros(n-s)
    for i in range(n-s):
        if Port_Logret[s+i] < -R_VaR95_B[i]:
            vb = vb + 1
            violB[i] = 1
        else:
            vb = vb + 0
            violB[i] = 0

    for i in range(n-s):
        if Port_Logret[s+i] < -R_VaR95_N[i]:
            vn = vn + 1
            violN[i] = 1
        else:
            vn = vn + 0
            violN[i] = 0
    ## Print n violazioni
    # print("N Violazioni al Bootstrap VaR 95% : " + str(vb) + " ")
    # print("N Violazioni al Normal VaR 95% : " + str(vn) + " ")
    ##########################################################################
    ### Test di Kupiec #######################################################
    ##########################################################################
    Kupiec(Port_Logret,vb,vn,0.95)
    LRlogB = Kupiec(Port_Logret,vb,vn,0.95)[0]
    LRlogN = Kupiec(Port_Logret,vb,vn,0.95)[1]
    tbk = Kupiec(Port_Logret,vb,vn,0.95)[2]
    tnk = Kupiec(Port_Logret,vb,vn,0.95)[3]
    ##########################################################################
    ### Test di Christoffersen ###############################################
    ##########################################################################
    Christoffersen(violN,violB)
    LRindb = Christoffersen(violN,violB)[0]
    LRindg = Christoffersen(violN,violB)[1]
    cbk = Christoffersen(violN,violB)[2]
    cnk = Christoffersen(violN,violB)[3]
    ##########################################################################
    ### Test di Christoffersen ###############################################
    ##########################################################################
    Con_Coverage(LRindb,LRlogB,LRlogN,LRindg,0.95)
    ccbk = Con_Coverage(LRindb,LRlogB,LRlogN,LRindg,0.95)[0]
    ccnk = Con_Coverage(LRindb,LRlogB,LRlogN,LRindg,0.95)[1]
    ## Grafici violazioni#####################################################
    plt.clf()
    plt.subplot(121)
    plt.plot(violB)
    plt.title("Bootstrap VaR 95% Violations")
    plt.ylim([0,1])
    plt.xlim([0,n-s])
    plt.subplot(122)
    plt.plot(violN)
    plt.title("Normal VaR 95% Violations")
    plt.ylim([0,1])
    plt.xlim([0,n-s])
    plt.tight_layout()
    plt.show(block=False)
    ##########################################################################
    ### Stampa Test e Violazioni #############################################
    ##########################################################################
    table = [('Typo VaR 95%', 'N. Violazioni', "T. Kupiec", "Christoffersen",\
             "Conditional Coverage"),
             ("Gaussian", vn, tnk, cnk, ccnk),
             ("Bootstrap", vb, tbk, cbk, ccbk)]

    class TabulateLabel(tk.Label):
        def __init__(self, parent, table, **kwargs):
            super().__init__(parent,
                             font=('Consolas', 10),
                             justify=tk.LEFT, anchor='nw', **kwargs)

            text = tabulate(table, headers='firstrow', tablefmt='github', showindex=False,numalign="left")
            self.configure(text=text)


    class App(tk.Tk):
        def __init__(self):
            super().__init__()
            TabulateLabel(self, table=table, bg='white').grid(sticky='ew')

    if __name__ == "__main__":
        App().mainloop()

    return vn, vb
def V_VaR99():
    ###########################################################################
    ## Acquisizione Date Inizio e Fine Rilevazione ###########################
    ##########################################################################
    user_inputSA = text_input6.get()
    user_inputSM = text_input61.get()
    user_inputSD = text_input62.get()
    user_inputEA = text_input7.get()
    user_inputEM = text_input71.get()
    user_inputED = text_input72.get()
    start = user_inputSA + "-" + user_inputSM + "-" + user_inputSD
    end = user_inputEA + "-" + user_inputEM + "-" + user_inputED
    ##########################################################################
    ### Fine Acquisizione Date Inizio e Fine Rilevazione ######################
    ###########################################################################
    if N_Az1_input.get():
        if N_Az2_input.get():
            if N_Az3_input.get():
                if N_Az4_input.get():
                    if N_Az5_input.get():   ## Portafoglio composto da 5 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        n5 = int(N_Az5_input.get())
                        nt = n1 + n2 + n3 + n4 + n5
                        wn = np.array([n1, n2 ,n3 ,n4 ,n5])
                        w = wn / nt
                        if text_input.get():
                            if text_input2.get():
                                if text_input3.get():
                                    if text_input4.get():
                                        if text_input5.get():
                                            user_input1 = text_input.get()
                                            user_input2 = text_input2.get()
                                            user_input3 = text_input3.get()
                                            user_input4 = text_input4.get()
                                            user_input5 = text_input5.get()
                                            user_input = [user_input1, \
                                                          user_input2, \
                                                          user_input3, \
                                                          user_input4, \
                                                          user_input5]
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:                  ## Portafoglio composto da 4 titoli
                        n1 = int(N_Az1_input.get())
                        n2 = int(N_Az2_input.get())
                        n3 = int(N_Az3_input.get())
                        n4 = int(N_Az4_input.get())
                        nt = n1 + n2 + n3 + n4
                        wn = np.array([n1, n2 ,n3 ,n4])
                        w = wn / nt
                        user_input1 = text_input.get()
                        user_input2 = text_input2.get()
                        user_input3 = text_input3.get()
                        user_input4 = text_input4.get()
                        user_input = [user_input1, user_input2, user_input3,\
                                      user_input4]
                else:                      ## Portafoglio composto da 3 titoli
                    n1 = int(N_Az1_input.get())
                    n2 = int(N_Az2_input.get())
                    n3 = int(N_Az3_input.get())
                    nt = n1 + n2 + n3
                    wn = np.array([n1, n2 ,n3])
                    w = wn / nt
                    user_input1 = text_input.get()
                    user_input2 = text_input2.get()
                    user_input3 = text_input3.get()
                    user_input = [user_input1, user_input2, user_input3]
            else:                          ## Portafoglio composto da 2 titoli
                n1 = int(N_Az1_input.get())
                n2 = int(N_Az2_input.get())
                nt = n1 + n2
                wn = np.array([n1, n2])
                w = wn / nt
                user_input1 = text_input.get()
                user_input2 = text_input2.get()
                user_input = [user_input1, user_input2]
        else:
            n1 = int(N_Az1_input.get())
            nt = n1
            wn = np.array([n1])
            user_input1 = text_input.get()
            user_input = [user_input1]
    else:
        pass
    def VaR99(p,m,s):
        VaR99_Hbase = - p.quantile(0.01)
        VaR99_Norm = - ss.norm.ppf(1-0.99, m, s)
        VaR99_Boots = BootsVaR(0.99,p)
        return VaR99_Boots,VaR99_Norm,VaR99_Hbase
    df = web.DataReader(user_input, "yahoo", start, end).dropna()
    data = df["Adj Close"]
    LogReturn = np.log(data/data.shift(1))
    port = data.dot(wn)
    Port_Logret = np.log(port/port.shift(1)).dropna()
    s = 6*20
    n = len(Port_Logret)
    P = Port_Logret.to_numpy()
    R_VaR99_B = np.zeros(n-s)
    R_VaR99_N = np.zeros(n-s)
    R_VaR99_HB = np.zeros(n-s)
    for i in range(n-s):
        sample_range = np.arange(0,s) + i
        sample_ret = Port_Logret[sample_range]
        [R_VaR99_B[i],R_VaR99_N[i],R_VaR99_HB[i]] = VaR99(sample_ret,\
                                                          sample_ret.mean(),\
                                                          sample_ret.std())
    ###########################################################################
    ##### Calcolo violazioni al  99% VaR Bootstrap
    vb = 0
    vn = 0
    n = len(Port_Logret)
    violB = np.zeros(n-s)
    violN = np.zeros(n-s)
    for i in range(n-s):
        if Port_Logret[s+i] < -R_VaR99_B[i]:
            vb = vb + 1
            violB[i] = 1
        else:
            vb = vb + 0
            violB[i] = 0

    for i in range(n-s):
        if Port_Logret[s+i] < -R_VaR99_N[i]:
            vn = vn + 1
            violN[i] = 1
        else:
            vn = vn + 0
            violN[i] = 0
    ## Print n violazioni
    # print("N Violazioni al Bootstrap VaR 99% : " + str(vb) + " ")
    # print("N Violazioni al Normal VaR 99% : " + str(vn) + " ")
    ##########################################################################
    ### Test di Kupiec #######################################################
    ##########################################################################
    Kupiec(Port_Logret,vb,vn,0.99)
    LRlogB = Kupiec(Port_Logret,vb,vn,0.99)[0]
    LRlogN = Kupiec(Port_Logret,vb,vn,0.99)[1]
    tbk = Kupiec(Port_Logret,vb,vn,0.99)[2]
    tnk = Kupiec(Port_Logret,vb,vn,0.99)[3]
    ##########################################################################
    ### Test di Christoffersen ###############################################
    ##########################################################################
    Christoffersen(violN,violB)
    LRindb = Christoffersen(violN,violB)[0]
    LRindg = Christoffersen(violN,violB)[1]
    cbk = Christoffersen(violN,violB)[2]
    cnk = Christoffersen(violN,violB)[3]
    ##########################################################################
    ### Test di Christoffersen ###############################################
    ##########################################################################
    Con_Coverage(LRindb,LRlogB,LRlogN,LRindg,0.99)
    ccbk = Con_Coverage(LRindb,LRlogB,LRlogN,LRindg,0.99)[0]
    ccnk = Con_Coverage(LRindb,LRlogB,LRlogN,LRindg,0.99)[1]
    ## Grafici violazioni#####################################################
    plt.clf()
    plt.subplot(121)
    plt.plot(violB)
    plt.title("Bootstrap VaR 99% Violations")
    plt.ylim([0,1])
    plt.xlim([0,n-s])
    plt.subplot(122)
    plt.plot(violN)
    plt.title("Normal VaR 99% Violations")
    plt.ylim([0,1])
    plt.xlim([0,n-s])
    plt.tight_layout()
    plt.show(block=False)
    ##########################################################################
    ### Stampa Test e Violazioni #############################################
    ##########################################################################
    table = [('Typo VaR 99%', 'N. Violazioni', "T. Kupiec", "Christoffersen",\
             "Conditional Coverage"),
             ("Gaussian", vn, tnk, cnk, ccnk),
             ("Bootstrap", vb, tbk, cbk, ccbk)]

    class TabulateLabel(tk.Label):
        def __init__(self, parent, table, **kwargs):
            super().__init__(parent,
                             font=('Consolas', 10),
                             justify=tk.LEFT, anchor='nw', **kwargs)

            text = tabulate(table, headers='firstrow', tablefmt='github', showindex=False,numalign="left")
            self.configure(text=text)


    class App(tk.Tk):
        def __init__(self):
            super().__init__()
            TabulateLabel(self, table=table, bg='white').grid(sticky='ew')

    if __name__ == "__main__":
        App().mainloop()

    return vn, vb

def Kupiec(P,vb,vn,a): #a = lc conf VaR,vb = viol boots , vn = viol norm
    nobs = len(P)
    at = 1 - (vb/nobs)
    signlv = 0.95
    val_crit = ss.chi2.ppf(signlv, df=1)
    LRlogB = -2 * (vb*np.log((1-a)/(1-at))+(nobs-vb)*np.log(a/at))
    if LRlogB < val_crit:
        # print("Log-likehood Kupiec e' inferiore al valore critico di significativita' "\
              # + str(val_crit) + " . Il modello Bootstrap a LvL Conf "+ str(a)+" e' accurato")
        tbk = True
    else:
        # print("Log-likehood Kupiec e' superiore al valore critico di significativita' "\
              # + str(val_crit) + " . Il modello Bootstrap a LvL Conf "+ str(a)+" non e' accurato")
        tbk = False
    ## Gaussiano
    at = 1 - (vn/nobs)
    LRlogN = -2 * (vn*np.log((1-a)/(1-at))+(nobs-vn)*np.log(a/at))
    if LRlogN < val_crit:
        # print("Log-likehood Kupiec e' inferiore al valore critico di significativita' "\
        #       + str(val_crit) + " . Il modello Normal a LvL Conf "+ str(a)+" e' accurato")
        tnk = True
    else:
        # print("Log-likehood Kupiec e' superiore al valore critico di significativita' "\
        #       + str(val_crit) + " . Il modello Normal a LvL Conf "+ str(a)+" non e' accurato")
        tnk = False
    return LRlogB,LRlogN,tbk,tnk
def Christoffersen(violN,violB):
    ##### Test di Christoffersen
    alpha = 0.95
    val_crit = ss.chi2.ppf(alpha, df=1)
    n00=0;n10=0;n01=0;n11=0;phi=0;phi0=0;phi1=0;
    a=0;b=0;c=0;d=0;
    ## Gaussiano
    nobs = len(violN)
    for i in (range(nobs-1)):
        x = violN[i]
        y = violN[i+1]
        N = x + y
        T = x - y
        if N == 0:
            a = 1
        if N == 2:
            b = 1
        if T == -1:
            c = 1
        if T == 1:
            d = 1
        n00 = a + n00
        n11 = b + n11
        n01 = c + n01
        n10 = d + n10
        a = 0;b = 0;c = 0;d = 0;N = 0;T = 0;
    phi0 = n01/(n00 + n01)
    phi1 = n11/(n10 + n11)
    phi = (n01 +  n11)/(n00 + n11 + n01 + n10)
    A = ((1 - phi)**(n00 + n10)) * ((phi)**(n01 + n11))
    B = ((1 - phi0)**n00) * (phi0**n01) * ((1 - phi1)**(n10)) * (phi1**n11)
    LRindg = - 2*np.log(A/B)
    if LRindg < val_crit:
        # print("Christoffersen Gaussiano superato, LR = "+str(LRindg)+" < CV = " + str(val_crit))
        cnk = True
    else:
        # print("Christoffersen Gaussiano fallito, LR = "+str(LRindg)+"  > CV = " + str(val_crit))
        cnk = False
    ## Bootstrap
    alpha = 0.95
    val_crit = ss.chi2.ppf(alpha, df=1)
    n00=0;n10=0;n01=0;n11=0;phi=0;phi0=0;phi1=0;
    a=0;b=0;c=0;d=0;
    nobs = len(violB)
    for i in (range(nobs-1)):
        x = violB[i]
        y = violB[i+1]
        N = x + y
        T = x - y
        if N == 0:
            a = 1
        if N == 2:
            b = 1
        if T == -1:
            c = 1
        if T == 1:
            d = 1
        n00 = a + n00
        n11 = b + n11
        n01 = c + n01
        n10 = d + n10
        a = 0;b = 0;c = 0;d = 0;N = 0;T = 0;
    phi0 = n01/(n00 + n01)
    phi1 = n11/(n10 + n11)
    phi = (n01 +  n11)/(n00 + n11 + n01 + n10)
    A = ((1 - phi)**(n00 + n10)) * ((phi)**(n01 + n11))
    B = ((1 - phi0)**n00) * (phi0**n01) * ((1 - phi1)**(n10)) * (phi1**n11)
    LRindb = - 2*np.log(A/B)
    if LRindb < val_crit:
        # print("Christoffersen Bootstrap superato, LR = "+str(LRindb)+" < CV = " + str(val_crit))
        cbk = True
    else:
        # print("Christoffersen Bootstrap fallito, LR = "+str(LRindb)+"  > CV = " + str(val_crit))
        cbk = False
    return LRindb,LRindg,cbk,cnk
def Con_Coverage(LRindb,LRlogB,LRlogN,LRindg,a):
    val_crit = ss.chi2.ppf(0.95, df=2)
    ## Bootstrap
    LRccb = LRindb + LRlogB
    if LRccb < val_crit:
        # print("Conditional Coverage Bootstrap VaR "+str(a)+"% superato")
        ccbk = True
    else:
        # print("Conditional Coverage Bootstrap VaR "+str(a)+"% fallito")
        ccbk = False
    ## Normal
    LRccn = LRlogN + LRindg
    if LRccn < val_crit:
        # print("Conditional Coverage Gaussiano VaR "+str(a)+"% superato")
        ccnk = True
    else:
        # print("Conditional Coverage Gaussiano VaR "+str(a)+"% fallito")
        ccnk = False
    return ccbk,ccnk
def Lista_Tickers():
    ############################################################################
    ### Caricamento Tickers USA  da FinnHub.io #################################
    ############################################################################
    US = requests.get('https://finnhub.io/api/v1/stock/symbol?exchange=US&token=btcvafv48v6veiek5r60')
    listdf=US.json()
    df = pd.DataFrame.from_dict(US.json())
    # df.to_csv(r'D:\Python\ProgettoFinanzaQuantitativa\tickers.csv', index = False)
    tickersUS = df.iloc[:,1:3]
    tickersUS.sort_values(by=["description"],axis=0)
    tickersUS_comb = tickersUS.iloc[:,0] + "     " + "[" + tickersUS.iloc[:,1]+ "]"
    tickersUS_comb_sort = tickersUS_comb.sort_values()
    scrollbar = Scrollbar(window,elementborderwidth=100,orient="vertical")
    insert_labelLT = tk.Label(window,text="Lista Tickers US (PagUp/PagDown)",\
                                font=("Helvetica",10))
    insert_labelLT.grid(row=16,column=0, sticky="NSWE", padx=10, pady=10)
    l=Listbox(window, width=50, height=18, selectmode=EXTENDED, yscrollcommand = scrollbar.set)
    l.grid(row=17,column=0,padx=10, rowspan=6)
    for tick in tickersUS_comb_sort:
        l.insert(END,str(tick))
###############################################################################
### Pulsante Lista Tickers ####################################################
###############################################################################
LT_button = tk.Button(text="Mostra Lista Tickers", command=Lista_Tickers)
LT_button.grid(row=15, column=0, sticky="WE", pady=10, padx=10)
###############################################################################
### Pulsante Analisi Preliminare ##############################################
###############################################################################
A_prel_button = tk.Button(text="Analisi Preliminare", command=Analisi_Preliminare)
A_prel_button.grid(row=15, column=1, sticky="WE", pady=10, padx=10, columnspan = 3)
###############################################################################
### Pulsante Analisi di Portafoglio ###########################################
###############################################################################
A_port_button = tk.Button(text="Analisi Portafoglio", command=Analisi_Portafoglio)
A_port_button.grid(row=16, column=1, sticky="WE", pady=10, padx=10,columnspan = 3)
###############################################################################
###############################################################################
### Pulsante VaR90 ###########################################
###############################################################################
VaR90_button = tk.Button(text="VaR Conf.Lvl 90%", command=VaR90)
VaR90_button.grid(row=17, column=1, sticky="NWE", pady=10, padx=10,columnspan = 1)
###############################################################################
### Pulsante VaR95 ###########################################
###############################################################################
VaR95_button = tk.Button(text="VaR Conf.Lvl 95%", command=VaR95)
VaR95_button.grid(row=17, column=2, sticky="NWE", pady=10, padx=10,columnspan = 1)
###############################################################################
### Pulsante VaR95 ###########################################
###############################################################################
VaR99_button = tk.Button(text="VaR Conf.Lvl 99%", command=VaR99)
VaR99_button.grid(row=17, column=3, sticky="NWE", pady=10, padx=10,columnspan = 1)
###############################################################################
###############################################################################
### Pulsante VaR90 ###########################################
###############################################################################
RW_VaR90_button = tk.Button(text="R.Win.6m VaR  90%", command=RW_VaR90)
RW_VaR90_button.grid(row=18, column=1, sticky="NWE", pady=10, padx=10,columnspan = 1)
###############################################################################
### Pulsante VaR95 ###########################################
###############################################################################
RW_VaR95_button = tk.Button(text="R.Win.6m VaR  95%", command=RW_VaR95)
RW_VaR95_button.grid(row=18, column=2, sticky="NWE", pady=10, padx=10,columnspan = 1)
###############################################################################
### Pulsante VaR95 ###########################################
###############################################################################
RW_VaR99_button = tk.Button(text="R.Win.6m VaR 99%", command=RW_VaR99)
RW_VaR99_button.grid(row=18, column=3, sticky="NWE", pady=10, padx=10,columnspan = 1)
###############################################################################
###############################################################################
### Pulsante VaR90 Violation ###########################################
###############################################################################
RW_VaR90_button = tk.Button(text="Violation VaR  90%", command=V_VaR90)
RW_VaR90_button.grid(row=19, column=1, sticky="NWE", pady=10, padx=10,columnspan = 1)
###############################################################################
### Pulsante VaR95 ###########################################
###############################################################################
RW_VaR95_button = tk.Button(text="Violation VaR  95%", command=V_VaR95)
RW_VaR95_button.grid(row=19, column=2, sticky="NWE", pady=10, padx=10,columnspan = 1)
###############################################################################
### Pulsante VaR95 ###########################################
###############################################################################
RW_VaR99_button = tk.Button(text="Violation VaR 99%", command=V_VaR99)
RW_VaR99_button.grid(row=19, column=3, sticky="NWE", pady=10, padx=10,columnspan = 1)
###############################################################################






### Credits ###################################################################
###############################################################################
# credits_label = tk.Label(window, text="By Stefano Putorti")
# credits_label.grid(row=2,column=2,sticky="WE",pady=10)
###############################################################################
### Loop Finestra #############################################################
# ###############################################################################
if __name__ == "__main__":
    window.mainloop()
