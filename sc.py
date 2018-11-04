import soundcloud

def get_soundcloud_track(client_id, track_id):
    client = soundcloud.Client(client_id=client_id)
    return client.get('/tracks/' + str(track_id))
