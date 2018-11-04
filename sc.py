import soundcloud

def get_soundcloud_track(client_id, track_url):
    client = soundcloud.Client(client_id=client_id)
    return client.get('/resolve', url=track_url)

def get_highres_image(artwork_url):
    return artwork_url.replace('large', 't500x500')