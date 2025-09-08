weight_input = input("请输入重量：")
if weight_input [-2:] in ['kg', 'KG']:
    pound = (eval(weight_input[0:-2])) * 2.2046
    print(f"对应的英制重量为{pound:.3f}磅")
elif weight_input [-2:] in ['pd', 'PD']:
    kilogram = (eval(weight_input[0:-2])) * 0.4535
    print(f"对应的公制重量为{kilogram:.3f}公斤")
else:
    print("输入格式错误")
