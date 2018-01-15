from __future__ import print_function
import pandas as pd
import numpy as np
from datetime import datetime
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot



def result(target, prediction):
    error = []
    for i in range(len(target)):
        error.append(target[i] - prediction[i])

    print("Errors: ", error)
    squaredError = []
    absError = []
    absErrorRe = []
    for i,val in enumerate(error):
        squaredError.append(val * val)  # target-prediction之差平方
        absError.append(abs(val))  # 误差绝对值
        absErrorRe.append(abs(val)*100/prediction[i])

    print("Square Error: ", squaredError)
    print("Absolute Value of Error: ", absError)

    print("MSE = ", sum(squaredError) / len(squaredError))  # 均方误差MSE

    from math import sqrt
    print("RMSE = ", sqrt(sum(squaredError) / len(squaredError)))  # 均方根误差RMSE
    print("MAE = ", sum(absError) / len(absError))  # 平均绝对误差MAE
    print("MAPE = ",sum(absErrorRe)/len(absErrorRe))

    targetDeviation = []
    targetMean = sum(target) / len(target)  # target平均值
    for val in target:
        targetDeviation.append((val - targetMean) * (val - targetMean))
    print("Target Variance = ", sum(targetDeviation) / len(targetDeviation))  # 方差

    print("Target Standard Deviation = ", sqrt(sum(targetDeviation) / len(targetDeviation)))  # 标准差




# key = '371300403107~371311991027' #(2,0,2)RMSE 13   (2,0,1) RMSE 12.97
key = '371302989805~371302989806' #(2,0,2)RMSE 11  (2,0,1) RMSE 10.93
# key = '371302971143~371302971096' #不行 误差太大，因为数据有空缺
filePath1 = "/Users/migowei/Documents/实验数据/30_padding/TraveltimeList/"+ key + ".txt"
frV = open(filePath1,'r')
# dtaV = ['%.2f' % float(n) for n in frV.read().split(' ')[5953:-1]] #两个月测试集
dtaV = ['%.2f' % float(n) for n in frV.read().split(' ')[2977:-1]] #一个月测试集
# print(dtaV)


# filePath2 = "/Users/migowei/Documents/实验数据/TestSet/2months/"+ key + ".txt"
filePath2 = "/Users/migowei/Documents/实验数据/30_padding/TestSet/1months/"+ key + ".txt"
frT = open(filePath2,'r')
dta = ['%.2f' % float(n) for n in frT.read().split(' ')[0:-1]]
dta = np.array(dta,dtype=np.float)
dta = pd.Series(dta)
# print(dta)
dta.index = pd.date_range(datetime.strptime('2015-12-01 00:00:00',"%Y-%m-%d %H:%M:%S"),periods=2976,freq='15min')
dta.plot(figsize = (12,8))
# plt.show()


# 一阶差分
# flg = plt.figure(figsize=(12,8))
# ax1 = flg.add_subplot(111)
# diff1 = dta.diff(2)
# diff1.plot(ax=ax1)
# plt.show()


# diff1 = dta.diff(1)
# fig = plt.figure(figsize=(12,8))
# ax1 = fig.add_subplot(211)
# fig = sm.graphics.tsa.plot_acf(dta, lags=40, ax=ax1)
# ax2 = fig.add_subplot(212)
# fig = sm.graphics.tsa.plot_pacf(dta, lags=40, ax=ax2)
# plt.show()


# #choose right p,d,q
# arima_mod302 = sm.tsa.ARIMA(dta,(3,0,2)).fit()
# print(arima_mod302.aic, arima_mod302.bic, arima_mod302.hqic)
#
# arima_mod101 = sm.tsa.ARIMA(dta,(1,0,1)).fit()
# print(arima_mod101.aic, arima_mod101.bic, arima_mod101.hqic)
#
# arima_mod310 = sm.tsa.ARIMA(dta,(3,1,0)).fit()
# print(arima_mod310.aic, arima_mod310.bic, arima_mod310.hqic)

# arima_mod200 = sm.tsa.ARIMA(dta,(2,0,0)).fit()
# print(arima_mod200.aic, arima_mod200.bic, arima_mod200.hqic)
#
# arima_mod210 = sm.tsa.ARIMA(dta,(2,1,0)).fit()
# print(arima_mod210.aic, arima_mod210.bic, arima_mod210.hqic)
#
# arima_mod220 = sm.tsa.ARIMA(dta,(2,2,0)).fit()
# print(arima_mod220.aic, arima_mod220.bic, arima_mod220.hqic)

arima_mod201 = sm.tsa.ARIMA(dta,(2,0,1)).fit()
# print(arima_mod201.aic, arima_mod201.bic, arima_mod201.hqic)

# arima_mod202 = sm.tsa.ARIMA(dta,(2,0,2)).fit()
# print(arima_mod202.aic, arima_mod202.bic, arima_mod202.hqic)

# 检验残差序列

resid = arima_mod201.resid

fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)
# plt.show()


# # D-W检验， 检验自相关性最常用的方法，仅适用于检验一阶自相关性。
# # 因为自相关系数p的值介于－1和1之间，所以0<=DW<=4。 并且DW=O=>p=1,即存在正自相关性。
# # DW＝４＜＝＞ρ＝－１　即存在负自相关性，
# # DW＝２＜＝＞ρ＝０　　即不存在（一阶）自相关性。
# # 因此，当DW值显著的接近于O或４时，则存在自相关性，而接近于２时，则不存在（一阶）自相关性
# print(sm.stats.durbin_watson(arma_mod20.resid.values))

# 观察是否符合正态分布
# print(stats.normaltest(resid))
# fig = plt.figure(figsize=(12,8))
# ax = fig.add_subplot(111)
# fig = qqplot(resid, line='q',ax=ax, fit=True)
# plt.show()

# # 残差序列Ljung-Box检验，也叫Q检验
# r,q,p = sm.tsa.acf(resid.values.squeeze(), qstat=True)
# data = np.c_[range(1,8736),r[1:],q,p]
# table = pd.DataFrame(data, columns=['lag','AC',"Q","Prob(>Q)"])
# print(table.set_index('lag'))

# 预测！！

predict_dta = arima_mod201.predict('2016-01-01','2016-01-01 01:00:00',dynamic=True)
# print(predict_dta)

flg,ax = plt.subplots(figsize=(12,8))

ax = dta.plot(ax=ax)
flg = arima_mod201.plot_predict('2016-01-01','2016-01-01 01:00:00',dynamic=True,ax=ax, plot_insample=False)
# plt.show()



target = [float(i) for i in dtaV[0:5]]
prediction = ['%.2f' % float(i) for i in predict_dta]
prediction = [float(i) for i in prediction]
print(target)
print(prediction)

result(target,prediction)




