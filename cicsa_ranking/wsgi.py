import os
import dotenv
import warnings
from django.core.wsgi import get_wsgi_application

warnings.filterwarnings("ignore", category=UserWarning)

dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cicsa_ranking.settings")

application = get_wsgi_application()
