"""
    返回json,
    :param:状态码
    :param:信息
    :param:返回的数据
"""
import json

class Response:

    def json(self, code, message, data):

        try:
            code = int(code)
        except ValueError as reason:
            print('code必须为整形!', reason)
        else:
            alldata = {
                'code': code,
                'message': message,
                'data': data
            }
            result = json.dumps(alldata)
            return result

