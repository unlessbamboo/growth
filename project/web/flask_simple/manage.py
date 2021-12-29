from flask_migrate import Migrate


from apps import create_app, db
from apps.models import models


app = create_app()
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    context = dict(app=app, db=db)
    context.update(vars(models))
    return context
