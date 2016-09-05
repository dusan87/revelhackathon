import json

from app import app
from app.models import RevelResource
from flask import render_template, request, jsonify

@app.route('/')
@app.route('/index')
def list_content():
    """
    This view lists all stored data ordered by resource name.
    Context data looks like {'orders': [obj, obj], 'customers': [obj, obj]...}
    """

    resources = RevelResource.get_all()

    ctx = {}

    for resource in resources:
        resource_data = {'id': resource.id, 
                         'revel_id': resource.revel_id,
                         'created_date': resource.created_date,
                         'updated_date': resource.updated_date
                         }

        key = resource.name_plural if not resource.updated else 'updated_%s' % resource.name_plural       

        if key in ctx:
            ctx[key].append(resource_data)
        else:
            ctx.update({
                key: [resource_data]
            })

    return render_template('index.html', **{'tables': ctx})


@app.route('/resource/<int:resource_id>')
def show_resource_content(resource_id):
    """
    This view shows json like content data. 
    JSON data present Revel resource data retrived by webhook.
    """
    resource = RevelResource.query.get(resource_id)

    data = json.loads(resource.data)

    return jsonify(**data)
