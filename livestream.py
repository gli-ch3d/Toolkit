import argparse
from pathlib import Path
import time

import cv2
import mediapipe as mp


def parse_source(value: str) -> int | str:
    try:
        return int(value)
    except ValueError:
        return value


def on_result(
    result,
    _output_image: mp.Image,
    timestamp_ms: int,
) -> None:
    print(f"Detected {len(result.pose_landmarks)} pose(s) at {timestamp_ms} ms")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run pose detection on a live video source.")
    parser.add_argument(
        "--source",
        default="0",
        help="webcam index (default: 0) or a direct video stream URL",
    )
    parser.add_argument(
        "--model",
        type=Path,
        default=Path(__file__).with_name("pose_landmarker_lite.task"),
        help="path to the Pose Landmarker .task model",
    )
    parser.add_argument(
        "--no-preview",
        action="store_true",
        help="do not open a window showing the captured video",
    )
    args = parser.parse_args()

    if not args.model.is_file():
        raise FileNotFoundError(f"Pose Landmarker model not found: {args.model}")

    source = parse_source(args.source)
    options = mp.tasks.vision.PoseLandmarkerOptions(
        base_options=mp.tasks.BaseOptions(model_asset_path=str(args.model)),
        running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
        num_poses=1,
        output_segmentation_masks=False,
        result_callback=on_result,
    )

    print("Creating Pose Landmarker; this may use significant memory.", flush=True)
    with mp.tasks.vision.PoseLandmarker.create_from_options(options) as landmarker:
        capture = cv2.VideoCapture(source)
        if not capture.isOpened():
            capture.release()
            raise RuntimeError(f"Could not open video source: {args.source}")

        last_timestamp_ms = -1
        try:
            while True:
                ok, frame = capture.read()
                if not ok:
                    raise RuntimeError(f"Could not read a frame from: {args.source}")

                height, width = frame.shape[:2]
                if width > 640:
                    scale = 640 / width
                    frame = cv2.resize(
                        frame,
                        (640, round(height * scale)),
                        interpolation=cv2.INTER_AREA,
                    )

                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                timestamp_ms = max(
                    time.monotonic_ns() // 1_000_000,
                    last_timestamp_ms + 1,
                )
                last_timestamp_ms = timestamp_ms

                mp_image = mp.Image(
                    image_format=mp.ImageFormat.SRGB,
                    data=rgb_frame,
                )
                landmarker.detect_async(mp_image, timestamp_ms)

                if not args.no_preview:
                    cv2.imshow("Pose Landmarker", frame)
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        break
        finally:
            capture.release()
            if not args.no_preview:
                cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
