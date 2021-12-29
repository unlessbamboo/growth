from flask import (
    Flask, request, make_response,
    redirect, session, flash, url_for, current_app,
    render_template)
from flask_mail import (Mail, Message)

from apps.models.models import User, Role, NameForm
from apps import db, mail

from . import bp


def send_mail(to, subject, template, **kwargs):
    msg = Message(
        bp.config['MAIL_SUBJECT'] + subject,
        sender=bp.config['MAIL_SENDER'],
        recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)


@bp.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@bp.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@bp.route('/', methods=['GET', 'POST'])
def index():
    user_agent = request.headers.get('User-Agent')
    name = None
    form = NameForm()
    if form.validate_on_submit():
        # 获取前一个输入的名称
        oldName = session.get('name')

        # 数据库操作
        name = form.name.data
        user = User.query.filter_by(username=name).first()
        if user is None:
            user = User(username=name)
            db.session.add(user)
            session['known'] = False
            if bp.config['MAIL_ADMIN']:
                send_mail(bp.config['MAIL_ADMIN'],
                          "New user",
                          "mail/new_user",
                          user=user)
        else:
            session['known'] = True

        # 存储前一个输入的名称
        session['name'] = name
        if oldName and oldName != name:
            flash("Looks like you have changed your name.")

        return redirect(url_for('index'))
    return render_template(
        'index.html', user_agent=user_agent,
        form=form, name=session.get('name'),
        known=session.get('known', False)
    )


@bp.route('/cookie/<name>/')
def cookie(name):
    response = make_response(
        f"<h1>Hello {name}, we carry a cookie!</h1>")
    response.set_cookie('answer-bamboo', '100000')
    return response


@bp.route('/index.html')
def index_ref():
    return render_template('index.html')


@bp.route('/user/<name>/')
def user(name):
    return render_template('user.html', name=name)


@bp.route('/redirect/')
def redirect_google():
    return redirect('http://www.google.com')
