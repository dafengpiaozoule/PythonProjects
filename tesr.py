my_dict = {
    "王力宏":{
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰伦":{
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "林俊杰":{
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学友":{
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德华":{
        "部门": "科技部",
        "工资": 6000,
        "级别": 2
    },
}
print(my_dict)
key = my_dict.keys()
# for x in key:
#     print(my_dict[x][])

for x in key:
    if my_dict[x]["级别"] == 1:
        my_dict[x]["工资"] += 1000

print(my_dict)