
from src.main.main import app

from mangum import Mangum

app.root_path = "/dev/example"

handler = Mangum(app,
                 api_gateway_base_path='example')
