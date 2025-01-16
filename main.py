import datetime

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

event1 = datetime.datetime(year=1920, month=12, day=24, hour=23)
event2 = datetime.datetime.now()

age_of_wineeeee = event1 - event2
age_of_wineeeeeeeeeeeeeeee = age_of_wineeeee.days()

rendered_page = template.render(
    age_of_wine=age_of_wineeeeeeeeeeeeeeee,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()