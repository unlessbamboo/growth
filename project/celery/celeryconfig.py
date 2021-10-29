""" 配置中心
判断配置是否正确: python -m celeryconfig
"""

broker_url = 'redis://127.0.0.1:6379/10'
result_backend = 'redis://127.0.0.1:6379/9'

# 序列化
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']

# 执行错误时专用队列
task_routes = {
    'tasks.add': 'low-priority',
}

# 任务限速
task_annotations = {
    'tasks.add': {'rate_limit': '10/m'},
}

# 忽略结果, 以减少时间和空间的资源浪费, 如果设置backend, 则不生效.
# 全局: task_ignore_result
# 任务配置: ignore_result: @app.task(ignore_result=True)
# 任务执行选项: ignore_result: mytask.apply_async(1, 2, ignore_result=True)
