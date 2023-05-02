import re

from flask import jsonify, request, url_for

from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.views import get_unique_short_id

from . import app, db

pattern = re.compile('^[a-zA-Z0-9]+$')


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    if 'custom_id' not in data or not data['custom_id']:
        data['custom_id'] = get_unique_short_id()
    if len(data['custom_id']) > 17 or not pattern.match(data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage(f"Имя \"{data['custom_id']}\" уже занято.")
    urlmap = URLMap(
        original=data['url'],
        short=data['custom_id']
    )
    db.session.add(urlmap)
    db.session.commit()
    return jsonify(
        url=urlmap.original,
        short_link=url_for('redirect_view', short=urlmap.short, _external=True)
    ), 201


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify(url=urlmap.original), 200
