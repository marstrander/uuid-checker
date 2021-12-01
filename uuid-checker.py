from uuid import UUID
import sys

if len(sys.argv) < 2:
    print('\n(*) USAGE:\t python3 '+sys.argv[0]+' UUID')
    sys.exit()

def version_uuid(uuid):
    try:
        print(UUID(uuid).version)
    except ValueError:
        print('Not a valid UUID')

uuid = str(sys.argv[1])

version_uuid(uuid)
