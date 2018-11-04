def get_settings():
    import json
    with open('settings.json') as json_data:
        settings = json.load(json_data)
    return settings
