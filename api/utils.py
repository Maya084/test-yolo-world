import os
import json


def load_env(key):
    """
    Load env variable, such as int, float, dict, list, etc.
    If var not declared or it's empty returns None.
    If var not a valid JSON document return as it is.
    """
    result = os.getenv(key)
    try:
        # try to JSON parse the value
        parse_nums = {"parse_float": float, "parse_int": int}
        return None if result in (None, "") else json.loads(result, **parse_nums)
    except (TypeError, json.decoder.JSONDecodeError):
        # if unable to parse return the value as it is
        return result
