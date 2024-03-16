import logging
# 1xx（信息性状态码）：表示服务器收到请求并且正在处理。
# 2xx（成功状态码）：表示服务器成功处理了请求。
# 3xx（重定向状态码）：表示需要客户端采取进一步的操作来完成请求。
# 4xx（客户端错误状态码）：表示客户端发送的请求有错误，服务器无法处理。
# 5xx（服务器错误状态码）：表示服务器在处理请求时发生错误。

logging.basicConfig(filename='loggingStudy.log',filemode='a',level=logging.DEBUG)
logging.debug('this is debug log')
logging.info('this is debug log')
logging.warning('this is debug log')
logging.error('this is debug log')
logging.critical('this is debug log')