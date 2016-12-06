from flask import Flask, jsonify
from flask_restful import Resource, Api
from sampa2x import getPhoneticStrings
from arabizer import phonetize

app = Flask(__name__)
api = Api(app)

# to force the JSON library to handle unicode - we are in 2016 and it's still not the default... ;(
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = 'application/json; charset=utf-8'

class ResourceIndex(Resource):
  def get(self):
    return jsonify(
      {
        '_links': {
          'arabizer': {
            'href': '/arabizer/{german_word}',
            'templated': True
          }
        }
      })

class Arabizer(Resource):
  def get(self, german_word):
    print(german_word)
    phonetic = phonetize(german_word)
    sampa = getPhoneticStrings(False, ipa=phonetic)
    return jsonify(sampa)

api.add_resource(ResourceIndex, '/')
api.add_resource(Arabizer, '/arabizer/<string:german_word>')


if __name__ == '__main__':
    app.run(debug=True)