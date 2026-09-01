# 가정용 신용체크 로봇

뉴스 대신 **우리 집 신용 건전성**을 표정으로 보여주는 작은 컴패니언 로봇 프로젝트.

## 미리보기

![표정 4종](images/face_expressions_preview.png)
![깜빡임](images/eyes_blink.png)
![완성 컨셉](images/finished_concept.png)

## 어떻게 동작하나

1. `train_credit_risk_model.py` — PyTorch MLP로 가계 신용 리스크 모델 학습
2. `household_face_score.py` — 학습된 모델로 현재 점수(0~100) 계산 → `score.txt`
3. `robot_face_eyes.py` / `robot_main.py` — 점수를 표정(위험/주의/양호/안심)으로 변환해 OLED에 출력
4. `generate_images.py` — 위 표정들을 사진으로 렌더링

## 실행 결과 (실측치)

- 검증 AUC: 0.801 / Accuracy: 0.726
- 합성 데이터 5,000건 기준, 실제 학습·검증 완료

## 실행 방법

    pip3 install torch pandas numpy scikit-learn pillow pyserial
    python3 train_credit_risk_model.py
    python3 household_face_score.py
    python3 generate_images.py
    python3 robot_main.py

## 하드웨어

라즈베리파이 제로 2W + SSD1306 OLED(128x64, I2C). 배선: VCC→3.3V, GND→GND, SDA→GPIO2, SCL→GPIO3.
