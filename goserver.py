"""Flask server for personal go/ links."""

import flask
import tinydb

app = flask.Flask(__name__)
db = tinydb.TinyDB('links.json')


def find_url_by_shortcut(shortcut: str):
  matches = db.search(tinydb.Query().shortcut == shortcut)
  return None if not matches else matches[0]['url']


@app.route('/new', methods=['POST'])
def new():
  abort = lambda desc: (flask.jsonify({'description': desc}), 400)
  if not flask.request.is_json:
    return abort('Only JSON requests are ok.')

  payload = flask.request.get_json()
  if not set(payload.keys()) == {'shortcut', 'url'}:
    return abort('Only JSON objects with "shortcut" and "url" keys are ok.')

  shortcut = payload['shortcut'].strip()
  url = payload['url'].strip()

  if not shortcut:
    return abort('Shortcut cannot be empty.')

  if not url:
    return abort('URL cannot be empty.')

  matching_url = find_url_by_shortcut(payload['shortcut'])
  if matching_url:
    return abort(f'go/{shortcut} already points to {matching_url}')

  db.insert(payload)
  return flask.jsonify({'success': True})


@app.route('/go/<path:shortcut>')
def go(shortcut: str):
  url = find_url_by_shortcut(shortcut)
  if not url:
    flask.abort(404, description=shortcut)
  return flask.redirect(url)


@app.errorhandler(404)
def not_found(e: Exception):
  variables = {'shortcut': e.description}
  return flask.render_template('not_found.html', **variables), 404
