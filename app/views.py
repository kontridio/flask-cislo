from flask_appbuilder import ModelView ,DirectByChartView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import appbuilder, db
from .models import Pocet


class CisloView(ModelView):
    datamodel = SQLAInterface(Pocet)

    list_columns = ["cislo"]


class CountryDirectChartView(DirectByChartView):
    datamodel = SQLAInterface(Pocet)
    chart_title = 'graf'

    definitions = [
    {
        'label': 'Cislo',
        'group': 'id',
        'series': ['cislo']

    }
]
db.create_all()

appbuilder.add_view(
    CisloView, "Osoby", icon="fa-folder-open-o"
)
appbuilder.add_view(CountryDirectChartView, "Show Country Chart", icon="fa-dashboard", category="Statistics")