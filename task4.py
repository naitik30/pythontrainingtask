data_list =[12,24,35,24,88,120,155,88,120,155]

dist_data_list=[data for num,data in enumerate(data_list) if data not in data_list[:num]]

print dist_data_list[::-1]