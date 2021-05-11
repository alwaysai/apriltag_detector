import time
import edgeiq


def main():
    fps = edgeiq.FPS()
    detector = edgeiq.AprilTagDetector(edgeiq.AprilTagFamily.TAG_16h5)
    try:
        with edgeiq.WebcamVideoStream(cam=0) as video_stream, \
                edgeiq.Streamer() as streamer:
            # Allow Webcam to warm up
            time.sleep(2.0)
            fps.start()
            # loop detection
            while True:
                text = []
                frame = video_stream.read()
                detections = detector.detect(frame)
                for detection in detections:
                    frame = detection.markup_image(frame, tag_id=True)
                    text.append(detection.tag_id)

                text.append(fps.compute_fps())
                streamer.send_data(frame, text)

                if streamer.check_exit():
                    break

                fps.update()

    finally:
        fps.stop()
        print("elapsed time: {:.2f}".format(fps.get_elapsed_seconds()))
        print("approx. FPS: {:.2f}".format(fps.compute_fps()))
        print("Program Ending")


if __name__ == "__main__":
    main()
