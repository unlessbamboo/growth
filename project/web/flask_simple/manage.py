from flask_migrate import Migrate


from apps import create_app, db, socketio
from apps.models import models


app = create_app()
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    context = dict(app=app, db=db)
    context.update(vars(models))
    return context


@app.cli.command('list_route')
def list_route():
    print('以下是所有路由设置:')
    route_num = 0
    for route in app.url_map.iter_rules():
        print(route)
        route_num += 1
    print(f'{"*" * 10}总路由数量:{route_num}')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)
