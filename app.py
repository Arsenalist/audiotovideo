import sc
import yt
import resourcedownloader
import ffmpegconverter
import settingsprovider

def execute():
    settings = settingsprovider.get_settings()
    soundcloud_client_id = settings['soundcloud']['client_id']
    soundcloud_track_id = 522474537
    soundcloud_track = sc.get_soundcloud_track(soundcloud_client_id, soundcloud_track_id)
    audio_file = resourcedownloader.download_file(soundcloud_track.download_url + "?client_id=" +
                                                  soundcloud_client_id, "audio.mp3")
    image_file = resourcedownloader.download_file(soundcloud_track.artwork_url.replace('large', 't500x500'),
                                                  "image.jpg")
    ffmpegconverter.convert_to_video(image_file, audio_file, "video.mp4")
    yt.execute_youtube_upload("video.mp4", soundcloud_track.title, soundcloud_track.description, 17)


if __name__ == '__main__':
    execute()
