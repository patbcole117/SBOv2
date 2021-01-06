import json
import os

def get_config():
    config = {'SBO_HOST': os.getenv('SBO_HOST'), 'SBO_PORT': os.getenv('SBO_PORT'), 'SBO_SDC_URL': os.getenv('SBO_SDC_URL'), 'SBO_SALTY_URL': os.getenv('SBO_SALTY_URL')}
    return config