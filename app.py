import sc
import yt
import resourcedownloader
import ffmpegconverter
import settingsprovider
import argparse

def execute():
    parser = argparse.ArgumentParser()

    parser.add_argument("soundcloud_url", help="Soundcloud track URL is required")
    parser.add_argument("-c", "--yt-cat", help="YouTube category ID", type=int, default=17)
    parser.add_argument("-b", "--background", help="Background for video - defaults to Soundcloud")
    args = parser.parse_args()

    settings = settingsprovider.get_settings()
    soundcloud_client_id = settings['soundcloud']['client_id']
    soundcloud_track_url = args.soundcloud_url
    yt_cat_id = args.yt_cat
    soundcloud_track = sc.get_soundcloud_track(soundcloud_client_id, soundcloud_track_url)

    if soundcloud_track.downloadable is False:
        raise Exception("File is not enabled for downloads from Soundcloud")

    audio_file = resourcedownloader.download_file(soundcloud_track.download_url + "?client_id=" +
                                                  soundcloud_client_id, "audio.mp3")
    if args.background is None:
        image_file = resourcedownloader.download_file(sc.get_highres_image(soundcloud_track.artwork_url), "image.jpg")
    else:
        image_file = resourcedownloader.download_file(args.background)
    ffmpegconverter.convert_to_video(image_file, audio_file, "video.mp4")
    yt.execute_youtube_upload("video.mp4", soundcloud_track.title, soundcloud_track.description, yt_cat_id)


if __name__ == '__main__':
    execute()
