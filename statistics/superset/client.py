from superset import db
from superset.models.core import Database
from superset.models.dashboard import Dashboard
from superset.models.slice import Slice

database = Database(
    database_name='my database',
    sqlalchemy_uri='postgresql://myuser:mypassword@127.0.0.1:5432/mydb'
)

dashboard = Dashboard(
    dashboard_title='Test dashboard',
    published=True
)

db.session.add(database)
db.session.add(dashboard)
db.session.commit()

# Get the IDs of the database and dashboard
database_id = db.session.query(Database.id).filter_by(database_name='my database').scalar()
dashboard_id = db.session.query(Dashboard.id).filter_by(dashboard_title='Test dashboard').scalar()

# Create the Slice object
my_slice = Slice(
    slice_name='My Slice',
    viz_type='table',
    datasource_type='table',
    datasource_id=database.tables.get('my_table').id,
    description='A slice of my_table showing total sales grouped by customer name',
    params={
        'adhoc_filters': [
            {
                'col': 'price',
                'op': '>=',
                'val': '100',
            },
        ],
        'groupby': ['customer_name'],
        'metrics': [
            {
                'expressionType': 'SQL',
                'sqlExpression': 'SUM(price)',
                'label': 'Total Sales',
                'type': 'FLOAT',
                'description': '',
            },
        ],
    },
)
my_slice.dashboard_id = dashboard_id

# Add the Slice to the database
db.session.add(my_slice)
db.session.commit()
