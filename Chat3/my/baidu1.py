from aip import AipOcr
import json
import base64

# 定义常量
APP_ID = '15382948'
API_KEY = 'g9cuLk9o30YWG5rFwtcigcvn'
SECRET_KEY = 'yYhiszR49AUIBvxZ0KhZDF8c5GpojbMI'

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "D:/pythonworkspace/DeepLearning/Chat3/my/1.jpg"


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return base64.encode(fp.read())



# 定义参数变量

options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}


# 调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content(filePath), options)
print(json.dumps(result).encode("unicode-escape"))
