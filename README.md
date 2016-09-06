**Revelhackathon Webhooks**
==================

This is a Flask web application that demonstrates usage of Revel webhooks.
It covers usage of 4 available Revel webhooks at the moment:

* Order is finalized;
* Customer is created;
* Customer is updated;
* Reward card is created;

The application is composed of API endpoints and views. API enpoints stand for receiving content of fired webhook, while views display received content.

Here are available API enpoints that can be linked to Revel webhooks:

* /order/finalized/
* /customer/created/
* /customer/updated/
* /rewardcard/created/

_Note: Each endpoint stands for one of available Revel webhook_

Getting up and running on Heroku
--------------------------------

The steps below will get you up and running app on Heroku environment. We assume you have the following installed:

* heroku account
* heroku CLI

Download app and checkout to `heroku` branch:

    $ git clone git@github.com:dusan87/revelhackathon.git
    $ cd path/to/app/dir/
    $ git checkout heroku

Make sure that you are logged in to Heroku.

    $ heroku login

.. _heroku_: https://devcenter.heroku.com/

Create a test app on Heroku:

    $ heroku create app_name -s cedar

Push ``revelhackathon`` app to Heroku::

    $ git push heroku heroku:master

Run web app on Heroku:

    $ heroku ps:scale web=1

Add PostgreSQL to Heroku:

    $ heroku addons:add heroku-postgresql
    $ heroku pg:promote YELLOW_COLOR_POSTGRESQL_NAME (it's usually somethig like this 'postgresql-tapered-29893')

_It is **important** to switch YELLOW_COLOR_POSTGRESQL_NAME with the colored DB name shown to you after adding the heroku-postgresql to heroku._

Initialize database running with `initdb` command:

    $ heroku run python run.py initdb

Restart running app on Heroku:

    $ heroku restart -a app_name

Open running app:

    $ heroku open


Link Heroku app with Revel webhooks
-----------------------------------

As last step you would need to link Revel webhooks with deployed Heroku app with available endpoints:

* Order finalized: https://****.herokuapp.com/order/finalized/
* Customer created: https://****.herokuapp.com/customer/created/
* Customer updated: https://****.herokuapp.com/customer/updated/
* Reward card created: https://****.herokuapp.com/rewardcard/created/

Enjoy! #RevelUP


