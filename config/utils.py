def string_to_list(value, separator=','):
    """Convert a separator-separated string to a list."""
    if not value:
        return []
    return [item.strip() for item in value.split(separator)]
