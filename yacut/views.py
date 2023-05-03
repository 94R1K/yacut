import random
import string

from flask import flash, redirect, render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap


def get_unique_short_id():
    characters = string.ascii_letters + string.digits
    short_id = ''.join(random.choice(characters) for _ in range(6))
    return short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('yacut.html', form=form, urlmap=None)
    if form.custom_id.data:
        short = form.custom_id.data
    else:
        short = get_unique_short_id()
    if URLMap.query.filter_by(short=short).first():
        flash(f'Имя {short} уже занято!')
        return render_template('yacut.html', form=form, urlmap=None)
    urlmap = URLMap(
        original=form.original_link.data,
        short=short
    )
    db.session.add(urlmap)
    db.session.commit()
    return render_template('yacut.html', form=form, urlmap=urlmap)


@app.route('/<short>')
def redirect_view(short):
    urlmap = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(f'{urlmap.original}', code=302)
