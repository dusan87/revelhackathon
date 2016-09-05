#!flask/bin/python
import click

from app import app
from app.database import create_all


@click.group()
def execute():
    pass


@execute.command(help='Setup database schema')
def initdb():
    create_all()


@execute.command(help='Run application')
def application():
    app.run(debug=True)

if __name__ == '__main__':
    execute()
