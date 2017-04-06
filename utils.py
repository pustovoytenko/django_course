import os
import uuid


def get_file_path(instance, filename):
    """
    Upload images
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(instance.__class__.__name__.lower(), filename)