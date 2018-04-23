# import matplotlib.pyplot as plt
# from scipy import stats
#
# x_data = []
# y_data = []
#
# for y in range(1, 100):
#     y_data.append(y)
#     x_data.append((y-1)/2)
#
# plt.plot(x_data, y_data)
#
# plt.show()
#
# slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)
#
# model = {
#     'slope': slope,
#     'intercept': intercept,
#     'r_value': r_value,
#     'p_value': p_value,
#     'std_err': std_err,
# }
#
# pickle.dump(model, open('model.p', 'wb'))

def predict(x):
    import pickle
    predictor = pickle.load(open('predictDjango\model.p', 'rb'))
    slope = predictor['slope']
    intercept = predictor['intercept']
    return slope*x + intercept

if __name__ == '__main__':
    print(predict(5))
