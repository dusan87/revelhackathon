"""
It's an API that provides endpoints for Revel webhooks.

Once webhook is fired it sends resources data to linked API endpoint. 
Data are processed in local database and displayed to web content like.

Hooking enpoints example:
    * Order finalized - https://****.com/order/finalized/
    * Customer created - https://****.com/customer/created/
    * Customer updated - https://****.com//customer/updated/
    * Rewardcard created - https://****.com//rewardcard/created/

"""

from app import app
from app.database import db
from app.models import RevelResource
from flask import render_template, request, jsonify, render_template


def format_date(date_str):
    """This is a helper that cut off milliseconds of date string object."""
    return date_str.split('.')[0]


@app.route('/order/finalized/', methods=['POST'])
def order_finalized():
    """Endpoint that is triggered once order is finalized."""
    payload = request.json

    revel_id = payload['orderInfo']['id']
    created_date = format_date(payload['orderInfo']['created_date'])

    obj = RevelResource(revel_id=revel_id,
                        created_date=created_date,
                        name='order',
                        data=request.data)

    db.session.add(obj)
    db.session.commit()

    return jsonify(**request.json), 201


@app.route('/customer/created/', methods=['POST'])
def customer_created():
    """Endpoint that is triggered once a customer is created."""
    payload = request.json

    revel_id = payload['id']
    created_date = format_date(payload['created_date'])

    obj = RevelResource(revel_id=revel_id,
                        created_date=created_date,
                        name='customer',
                        data=request.data)

    db.session.add(obj)
    db.session.commit()

    print("Customer : '{}' is created! \nData: {}".format(request.json['first_name'], request.json))

    return jsonify(**request.json), 201


@app.route('/customer/updated/', methods=['POST'])
def customer_updated():
    """Endpoint that is triggered once a customer is updated."""
    payload = request.json

    revel_id = payload['id']
    created_date = format_date(payload['created_date'])
    updated_date = format_date(payload['updated_date'])

    obj = RevelResource(revel_id=revel_id,
                        created_date=created_date,
                        updated_date=updated_date,
                        name='customer',
                        updated=True,
                        data=request.data)

    db.session.add(obj)
    db.session.commit()

    print("Customer : '{}' is updated! \nData: {}".format(request.json['first_name'], request.json))

    return jsonify(**request.json), 201


@app.route('/rewardcard/created/', methods=['POST'])
def rewardcard_created():
    """Endpoint that is triggered once reward card is created."""

    payload = request.json

    revel_id = payload['id']
    created_date = format_date(payload['created_date'])

    obj = RevelResource(revel_id=revel_id,
                        created_date=created_date,
                        name='rewardcard',
                        data=request.data)

    db.session.add(obj)
    db.session.commit()

    print ("Reward Card Created! \nData:{}".format(request.json))

    return jsonify(**request.json), 201
