source_file = "user_demo.txt"
final_file = "mylist.txt"
favorite_list = [
    "CCTV1",
    "CCTV2",
    "CCTV3",
    "CCTV4",
    "CCTV5",
    "CCTV5+",
    "CCTV6",
    "CCTV7",
    "CCTV8",
    "CCTV9",
    "CCTV10",
    "CCTV11",
    "CCTV12",
    "CCTV13",
    "CCTV14",
    "CCTV15",
    "CCTV16",
    "CCTV17",
    "CCTV4K",
    "CCTV8k",
    "CCTV世界地理",
    "CCTV兵器科技",
    "CCTV卫生健康",
    "CCTV央视台球",
    "CCTV央视文化",
    "CCTV女性时尚",
    "CCTV怀旧剧场",
    "CCTV电视指南",
    "CCTV第一剧场",
    "CCTV音乐",
    "CCTV风云剧场",
    "CCTV风云足球",
    "CCTV风云音乐",
    "CCTV高尔夫网球",
    "CGTN",
    "CGTN俄语",
    "CGTN法语",
    "CGTN纪录",
    "CGTN西语",
    "CGTN阿语",
    "安多卫视",
    "安徽卫视",
    "北京卫视",
    "兵团卫视",
    "东方卫视",
    "东南卫视",
    "甘肃卫视",
    "广东卫视",
    "广东珠江",
    "广西卫视",
    "贵州卫视",
    "海南卫视",
    "海峡卫视",
    "河北卫视",
    "河南卫视",
    "湖北卫视",
    "湖南卫视",
    "吉林卫视",
    "江苏卫视",
    "江西卫视",
    "康巴卫视",
    "辽宁卫视",
    "旅游卫视",
    "内蒙卫视",
    "宁夏卫视",
    "农林卫视",
    "青海卫视",
    "三沙卫视",
    "厦门卫视",
    "山东卫视",
    "山西卫视",
    "陕西卫视",
    "上海卫视",
    "深圳卫视",
    "四川卫视",
    "天津卫视",
    "西藏卫视",
    "新疆卫视",
    "延边卫视",
    "云南卫视",
    "浙江卫视",
    "重庆卫视",
    "黑龙江卫视",
    "内蒙古卫视",
    "广东南方卫视",
    "山东教育卫视",
    "优漫卡通",
    "卡酷少儿",
    "嘉佳卡通",
    "炫动卡通",
    "金鹰卡通",
    "黑莓动画",
    "广东少儿",
    "云南少儿",
    "浙江少儿",
    "海南少儿",
    "甘肃少儿",
    "CETV1",
    "CETV2",
    "CETV3",
    "CETV4",
    "凤凰中文",
    "凤凰资讯",
    "香港卫视",
    "无线新闻",
    "无线资讯",
    "有线新闻",
    "有线资讯",
    "TVBS新闻",
    "TVBS亚洲",
    "TVBS欢乐台",
    "TVB翡翠台",
    "明珠台",
    "J2",
    "RTHK32",
    "香港佛陀",
    "MOMO1台",
    "MOMO2台",
    "大爱1台",
    "大爱2台",
    "台视新闻",
    "中视新闻",
    "三立新闻",
    "三立台湾",
    "寰宇新闻",
    "年代新闻",
    "耀才新闻",
    "民视新闻",
    "非凡新闻",
    "中天新闻",
    "公视新闻",
    "亚洲新闻",
    "东森新闻",
    "东森洋片",
    "东森美洲",
    "中天娱乐",
    "靖天国际",
    "八大台",
    "澳视卫星",
    "澳视澳门",
    "澳門有线",
    "澳门信息",
    "澳门卫视",
    "澳门莲花",
    "澳门葡语",
    "澳门资讯",
]
favorite_page_num = 6
default_page_num = 4
urls_limit = 15
response_time_weight = 0.6
resolution_weight = 0.4
recent_days = 30
ipv_type = "ipv4"