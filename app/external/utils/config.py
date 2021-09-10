from os import environ


class ConfigUtils:

    @staticmethod
    def env(key: str, env_type):
        if key not in environ:
            raise TypeError(f'Environment variable is absent {key}')

        value = environ[key]

        if env_type == str:
            return value
        elif env_type == bool:
            if value.lower() in ["1", "true", "yes", "y", "ok", "on"]:
                return True
            if value.lower() in ["0", "false", "no", "n", "nok", "off"]:
                return False
            raise ValueError(
                "Invalid environment variable '%s' (expected a boolean): '%s'" % (key, value)
            )
        elif env_type == int:
            try:
                return int(value)
            except ValueError:
                raise ValueError("Invalid environment variable '%s' (expected an integer): '%s'" % (key, value))
        else:
            raise TypeError('Unknown type')
