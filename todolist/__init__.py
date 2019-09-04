import os

# env vars for testing
ENVIRON = {
    'SOCIAL_AUTH_EVENTBRITE_KEY': 'basura',
    'SOCIAL_AUTH_EVENTBRITE_SECRET': 'basura',
    'SECRET_KEY': 'basura',
    }


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        return ENVIRON[var_name]
