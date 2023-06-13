from concurrent import futures

import tensorflow as tf
import tensorflow_io as tfio
from tqdm import tqdm


def extract_frame(frame: tf.Tensor, n: int, extracting_path: str) -> None:
    png_frame = tf.io.encode_png(frame)
    frame_path = f"{extracting_path}/frame_{n}.png"
    tf.io.write_file(frame_path, png_frame)

def extract_frames(gif_path: str, extracting_path: str = ".") -> None:
    frames = []

    try:
        gif_data = tf.io.read_file(gif_path)
        frames = tf.io.decode_gif(gif_data)
    except Exception as err:
        print(err.with_traceback())
        return

    # Using a thread for each frame
    with futures.ThreadPoolExecutor() as executor:
        for n, frame in enumerate(tqdm(frames), start=1):
            executor.submit(extract_frame, frame, n, extracting_path)

    print("Extraction success!")


if __name__ == "__main__":
    gif_path = input("Path to gif file: ")
    destination = input("Path for extracted frames: ")

    extract_frames(gif_path, destination)