# callback
# Hàm gọi trong hàm, 
# map, filter, reduce ... using callback
def get_value(params, data):
    print(data)
def call_back(value):
    print("Value is: ",value)

get_value(call_back,123)