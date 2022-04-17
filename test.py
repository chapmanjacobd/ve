import os

import ffmpeg

in0 = ffmpeg.input(os.path.expanduser("~/.tmp/2022_0412_090814_F.mp4"))
in1 = ffmpeg.input(os.path.expanduser("~/.tmp/2022_0412_090814_R.mp4"))
aout = ffmpeg.filter(
    [
        in0.audio,
        in1.audio,
    ],
    "amultiply",
)
vout = ffmpeg.filter(
    [
        in0.video,
        in1.video,
        in0.video,
        in1.video,
    ],
    "xstack",
    inputs=4,
    layout="0_0|w0_0|0_h0|w0_h0",
)

(
    ffmpeg.output(
        aout,
        vout,
        "out.mkv",
    ).run()
)

# ffmpeg -i input0 -i input1 -i input2 -i input3
# -filter_complex "[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]"
# -map "[v]" output
