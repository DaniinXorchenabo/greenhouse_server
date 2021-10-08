def get_migration_url():
    import os
    from src.utils.files import check_environment_params_loaded

    check_environment_params_loaded()

    return f"postgresql://{os.environ.get('PG_SUPERUSER_NAME')}:{os.environ.get('PG_SUPERUSER_PASSWORD')}" \
           f"@{os.environ.get('PGHOST')}:{os.environ.get('PGPORT')}/{os.environ.get('PGDATABASE')}"