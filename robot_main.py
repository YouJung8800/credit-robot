import random, time
from robot_face_eyes import draw_blink, draw_eyes, score_to_mood, show_on_device


def read_score_file(path="score.txt", default=50):
    try:
        with open(path) as f:
            return max(0, min(100, int(f.read().strip())))
    except Exception:
        return default


def main_loop():
    print("로봇 켜짐 (Ctrl+C로 종료)")
    score = read_score_file()
    mood = score_to_mood(score)
    show_on_device(draw_eyes(mood))
    while True:
        time.sleep(random.uniform(3, 8))
        show_on_device(draw_blink())
        time.sleep(0.15)
        show_on_device(draw_eyes(mood))


if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("종료")
