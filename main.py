import tensorflow as tf
import tensorflow_io as tfio
from PIL import Image
from PIL import GifImagePlugin

# Load the GIF file
FILENAME = "gman_1.gif"
gif_data = tf.io.read_file(FILENAME)

# Decode the GIF file using TensorFlow IO
gif = tf.io.decode_gif(gif_data)

flags = []


for n, frame in enumerate(gif, start=1):
    png_frame = tf.io.encode_png(frame)
    frame_path = f"frames/frame_{n}.png"
    tf.io.write_file(frame_path, png_frame)