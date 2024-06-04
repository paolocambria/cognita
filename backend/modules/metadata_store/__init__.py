from backend.modules.metadata_store.base import register_metadata_store
from backend.modules.metadata_store.local import LocalMetadataStore
from backend.modules.metadata_store.prismastore import PrismaStore
from backend.modules.metadata_store.truefoundry import TrueFoundry
from backend.settings import settings

register_metadata_store("local", LocalMetadataStore)
register_metadata_store("truefoundry", TrueFoundry)
register_metadata_store("prisma", PrismaStore)
