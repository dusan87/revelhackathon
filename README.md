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

Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv
* PostgreSQL


First make sure to create and activate a _virtualenv_, then open a terminal at the project root and install the requirements for local development:

    $ pip install -r requirements.txt

.. _virtualenv_: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Run the database initialization(please make sure postgreSQL is running and a **_revelhackathon_** database is created):

    $ python run.py initdb

You can now run the ``application`` command::

    $ python run.py application

You should be able to open _revelhackathon_ app accessing:

    http://127.0.0.1:5000

Developing and debugging
------------------------
In order to fully experience and be able to link and debug Revel webhooks with _revelhackathon_ app running on your local machine, you would need to install [ngrok](https://ngrok.com/) (this is optional, feel free to use any similar) tool. For more information on this tool you can read [ngrok documentation](https://ngrok.com/docs).

Assuming that [ngrok](https://ngrok.com/) is installed successfully, you just need to run the `ngrok`:

    $ ./ngrok http 5000

You should be provided with ngrok running infomation like this:

<img width="400" alt="screen shot 2016-09-06 at 1 30 42 pm" src="https://cloud.githubusercontent.com/assets/3380583/18262221/f2766c90-7442-11e6-920f-1f3e51526601.png">



Revel webhook functionality requires a secure https URL. To link webhooks with local running app you must take https url that `ngrok` created for you:

    https://****.ngrok.io


As last step you would need to link Revel webhooks with revelhathon available endpoints:

* Order finalized: https://****.ngrok.io/order/finalized/
* Customer created: https://****.ngrok.io/customer/created/
* Customer updated: https://****.ngrok.io/customer/updated/
* Reward card created: https://****.ngrok.io/rewardcard/created/

Enjoy! #RevelUP


