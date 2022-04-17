import os

import ffmpeg

from data import there_and_back

for index, tupl in enumerate(there_and_back):
    tf, bf, tr, br = tupl
    tf = ffmpeg.input(os.path.expanduser(f"~/.tmp/{tf}"))
    bf = ffmpeg.input(os.path.expanduser(f"~/.tmp/{bf}"))
    tr = ffmpeg.input(os.path.expanduser(f"~/.tmp/{tr}"))
    br = ffmpeg.input(os.path.expanduser(f"~/.tmp/{br}"))

    vout = ffmpeg.filter(
        [
            tf.video,
            bf.video,
            tr.video,
            br.video,
        ],
        "xstack",
        inputs=4,
        layout="0_0|w0_0|0_h0|w0_h0",
    )

    (
        ffmpeg.output(
            vout,
            tf.audio,
            bf.audio,
            f"{index}.mkv",
            vcodec="hevc",
            vaapi_device="/dev/dri/renderD128",
        ).run()
    )
