# REST in CRUD API

This API contains of four endpoints/methods for writing, reading, creating tables and deleting.

This API encrypts the email address and password of the user, and then stores it in session data and the database.

- `/`: Shows this Markdown file in a formatted HTML document.
- `/delete/<record>/<id>` - [ `DELETE` ]: Deletes an item from a record.
- `/write/<record>/<id>` - [ `POST`, `PUT` ]: Writes an (existing) item to a record.
- `/create/<record>` - [ `PUT` ]: Creates a new record, which items will be inserted into.
- `/read/<record>/<id>` - [ `GET`, `POST` ]: Read an item under a record by its ID.

The code for the pure login implementation and methods are in the file: `blueprints/root.py`
The code for just the API implementation or database methods are in the other blueprint files: `create.py`, `delete.py`, `read.py`, `write.py`.

[Log in](/login) or [Register](/register) for the demo.
Once logged in, your information will appear below here.

<style>
    a {
        color: #000;
    }
    p,h1,li {
        font-family: system-ui, arial, helvetica;
    }
    code {
        font-family: monospace;
    }
</style>
