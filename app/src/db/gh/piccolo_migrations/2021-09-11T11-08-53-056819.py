from piccolo.apps.migrations.auto import MigrationManager


ID = "2021-09-11T11:08:53:056819"
VERSION = "0.45.1"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="", description=DESCRIPTION
    )

    def run():
        print(f"running {ID}")

    manager.add_raw(run)

    return manager
