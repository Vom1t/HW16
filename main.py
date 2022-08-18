import json

from flask import request

from config import app
from models import Order, User, Offer
from service import init_db, get_all, get_all_by_id, update_universal, \
     delete_universal, insert_data_universal


@app.route('/users/', methods=['GET', 'POST'])  # Вьюшка получения и записи юзеров
def get_user():
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_all(User), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "POST":
        if isinstance(request.json, list):
            insert_data_universal(User, request.json)
        elif isinstance(request.json, dict):
            insert_data_universal(User, [request.json])
        else:
            print('Непонятный тип данных')

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route('/orders/', methods=['GET', 'POST'])  # Вьюшка получения и записи ордеров
def get_orders():
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_all(Order), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "POST":
        if isinstance(request.json, list):
            insert_data_universal(Order, request.json)
        elif isinstance(request.json, dict):
            insert_data_universal(Order, [request.json])
        else:
            print('Непонятный тип данных')

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route('/offers/', methods=['GET', 'POST'])  # Вьюшка получения и записи офферов
def get_offers():
    if request.method == "GET":
        return app.response_class(
            response=json.dumps(get_all(Offer), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == "POST":
        if isinstance(request.json, list):
            insert_data_universal(Offer, request.json)
        elif isinstance(request.json, dict):
            insert_data_universal(Offer, [request.json])
        else:
            print('Непонятный тип данных')

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route('/users/<int:users_id>', methods=['GET', 'PUT', 'DELETE'])  # Вьюшка получения, обновления и удаления
# одного юзера
def get_user_by_id(users_id):
    if request.method == 'GET':
        data = get_all_by_id(User, users_id)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_universal(User, users_id, request.json)
        return app.response_class(
            response=json.dumps(['OK'], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_universal(User, users_id)
        return app.response_class(
            response=json.dumps(['OK'], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route('/orders/<int:users_id>', methods=['GET', 'PUT', 'DELETE'])  # Вьюшка получения, обновления и удаления
# одного оредра
def get_order_by_id(users_id):
    if request.method == 'GET':
        data = get_all_by_id(Order, users_id)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_universal(Order, users_id, request.json)
        return app.response_class(
            response=json.dumps(['OK'], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_universal(Order, users_id)
        return app.response_class(
            response=json.dumps(['OK'], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route('/offers/<int:users_id>', methods=['GET', 'PUT', 'DELETE'])  # Вьюшка получения, обновления и удаления
# одного оффера
def get_offers_by_id(users_id):
    if request.method == 'GET':
        data = get_all_by_id(Offer, users_id)

        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_universal(Offer, users_id, request.json)
        return app.response_class(
            response=json.dumps(['OK'], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_universal(Offer, users_id)
        return app.response_class(
            response=json.dumps(['OK'], indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=8080, debug=True)