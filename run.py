#!flask/bin/python
from app import app
from app.database import create_all

create_all()
app.run(debug=True)