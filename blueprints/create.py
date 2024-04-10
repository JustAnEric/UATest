from flask import Blueprint
from data import create_table

bp = Blueprint(
    name="create",
    import_name=__name__
)

__all__ = ['bp']

# content

@bp.route('/create/<record>', methods=['PUT'])
@bp.route('/create/<record>/', methods=['PUT'])
def create(record):
    create_table(str(record))
    return "[]"
