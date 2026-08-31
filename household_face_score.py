import pickle
import torch
from model import FEATURE_COLS, CreditRiskNet


def load_model_and_scaler(model_path="credit_risk_model.pt", scaler_path="scaler.pkl"):
    model = CreditRiskNet(len(FEATURE_COLS))
    model.load_state_dict(torch.load(model_path))
    model.eval()
    with open(scaler_path, "rb") as f:
        scaler = pickle.load(f)
    return model, scaler


def get_household_input():
    return {"income": 380, "total_debt": 4200, "card_util": 0.55, "delinquencies": 0,
            "loan_balance": 8000, "years_employed": 3.5, "credit_history_m": 60,
            "inquiries_6m": 1, "dsr": 0.42}


def predict_risk(model, scaler, household):
    x = [[household[c] for c in FEATURE_COLS]]
    x_scaled = scaler.transform(x)
    x_t = torch.tensor(x_scaled, dtype=torch.float32)
    with torch.no_grad():
        return torch.sigmoid(model(x_t)).item()


def to_score(risk_prob):
    return max(0, min(100, int(round((1 - risk_prob) * 100))))


def mood_label(score):
    if score <= 25: return "위험"
    elif score <= 45: return "주의"
    elif score <= 70: return "양호"
    else: return "안심"


def write_score_file(score, path="score.txt"):
    with open(path, "w") as f:
        f.write(str(score))


if __name__ == "__main__":
    model, scaler = load_model_and_scaler()
    household = get_household_input()
    risk_prob = predict_risk(model, scaler, household)
    score = to_score(risk_prob)
    print(f"부실 위험 확률: {risk_prob:.1%} (실제 모델 계산값, 고정값 아님)")
    print(f"가계 신용 건전성 점수: {score} / 100")
    print(f"표정 상태: {mood_label(score)}")
    write_score_file(score)
