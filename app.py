import sc
import yt
import resourcedownloader
import ffmpegconverter
import settingsprovider
import argparse

def execute():
    parser = argparse.ArgumentParser()

    parser.add_argument("--sc-url", required=True, help="Soundcloud track URL is required")
    args = parser.parse_args()

    settings = settingsprovider.get_settings()
    soundcloud_client_id = settings['soundcloud']['client_id']
    soundcloud_track_url = args.sc_url
    soundcloud_track = sc.get_soundcloud_track(soundcloud_client_id, soundcloud_track_url)
    audio_file = resourcedownloader.download_file(soundcloud_track.download_url + "?client_id=" +
                                                  soundcloud_client_id, "audio.mp3")
    image_file = resourcedownloader.download_file(sc.get_highres_image(soundcloud_track.artwork_url), "image.jpg")
    ffmpegconverter.convert_to_video(image_file, audio_file, "video.mp4")
    yt.execute_youtube_upload("video.mp4", soundcloud_track.title, soundcloud_track.description, 17)


if __name__ == '__main__':
    execute()
