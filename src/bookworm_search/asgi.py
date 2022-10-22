from bookworm_search.api import Api
from bookworm_search.core.config import Config
from bookworm_search.core.service_container import ServiceContainer

config = Config()
service_container = ServiceContainer(config=config)
api = Api(config=config, service_container=service_container).api
