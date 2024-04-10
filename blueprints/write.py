from flask import Blueprint, request
from data import db, cursor, write_to_table, create_table

bp = Blueprint(
    name="write",
    import_name=__name__
)

__all__ = ['bp']

# content

@bp.route('/write/<record>/<id>', methods=['PUT', 'POST'])
@bp.route('/write/<record>/<id>/',methods=['PUT', 'POST'])
def write(record, id):
    response = {'message': 'Written record successfully.', 'data': ''}
    data = request.headers.get('data').split(', ')
    
    create_table(record) # just try and create a table just in case to prevent errors
    write_to_table(record, [
        (id, *data) # read all values from request data
    ])
    
    #try:
        #db.execute(query)
        #rows = cursor.fetchall()
        #response['data'] = rows
    #except: response = {'message': 'Error writing record.'}
    
    return response