def convert_to_video(image, audio, output):
    from subprocess import call
    call(["ffmpeg", "-loop", "1", "-i", image, "-i", audio, "-c:a", "copy", "-c:v", "libx264", "-shortest", "-y", output])
