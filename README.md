# 가정용 신용체크 로봇

![완성품](images/hero_shot.png)

아침에 커피 내리면서 부엌 테이블에 잠깐 두면, 앱을 켜서 숫자를 확인할 필요가 없다. 지나가다 눈 마주치듯 표정만 보면 끝이다 — 웃고 있으면 이번 달 지출이 괜찮다는 뜻이고, 눈썹이 처져 있으면 카드값을 한 번 들여다볼 때라는 신호다. 화면 속 숫자를 읽는 게 아니라 **표정을 읽는 것**, 그게 이 로봇이 다른 가계부 앱들과 다른 지점이다.

![가정에서 사용하는 모습](images/home_context.png)

책상 위에 두면 업무용 리마인더처럼, 침대 협탁에 두면 자기 전 마지막으로 확인하는 루틴처럼 — 어디 놓아도 크기가 커피잔 하나 정도라 자리를 차지하지 않으면서, 매일 무심코 지나치다 한 번씩 눈이 가는 존재감은 남긴다.

## 표정 4종

![표정 4종](images/face_expressions_preview.png)
![깜빡임](images/eyes_blink.png)

## 어떻게 동작하나

1. `train_credit_risk_model.py` — PyTorch MLP로 가계 신용 리스크 모델 학습
2. `household_face_score.py` — 학습된 모델로 현재 점수(0~100) 계산 → `score.txt`
3. `robot_face_eyes.py` / `robot_main.py` — 점수를 표정(위험/주의/양호/안심)으로 변환해 OLED에 출력
4. `generate_images.py` — 위 이미지들을 렌더링

## 실행 결과 (실측치)

- 검증 AUC: 0.801 / Accuracy: 0.726

## 실행 방법

    pip3 install torch pandas numpy scikit-learn pillow pyserial
    python3 train_credit_risk_model.py
    python3 household_face_score.py
    python3 generate_images.py
    python3 robot_main.py

## 하드웨어

라즈베리파이 제로 2W + SSD1306 OLED(128x64, I2C). 배선: VCC→3.3V, GND→GND, SDA→GPIO2, SCL→GPIO3.
