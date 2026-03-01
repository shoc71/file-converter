def get_storage():
    if settings.storage_type == "s3":
        return S3Storage()
    return LocalStorage()