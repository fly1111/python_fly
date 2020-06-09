import json
with open('movie.json') as f:
    list_json = json.load(f)
    for i in list_json:
        print("数字{}: 名字:{}, 介绍:{},星级{},评论{},电影描述{}".format(
        i['serial_number'][0],
        i['movie_name'][0],
        i['introduce'][0],
        i['star'][0],
        i['evaluate'][0],
        i['describe'][0]))



