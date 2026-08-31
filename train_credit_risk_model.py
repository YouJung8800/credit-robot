import pickle
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from model import FEATURE_COLS, CreditRiskNet

np.random.seed(42)
torch.manual_seed(42)


def make_synthetic_data(n=5000):
    income = np.random.normal(350, 120, n).clip(100, 1000)
    total_debt = np.random.normal(3000, 2000, n).clip(0, 15000)
    card_util = np.random.beta(2, 3, n)
    delinquencies = np.random.poisson(0.4, n)
    loan_balance = np.random.normal(5000, 4000, n).clip(0, 30000)
    years_employed = np.random.exponential(4, n).clip(0, 30)
    credit_history_m = np.random.normal(80, 40, n).clip(1, 300)
    inquiries_6m = np.random.poisson(1.2, n)
    dsr = ((total_debt * 0.03 + loan_balance * 0.02) / (income + 1)).clip(0, 2)
    logit = (-3.0 + 2.5*dsr + 1.8*card_util + 0.9*delinquencies + 0.5*inquiries_6m
             - 0.015*years_employed - 0.004*credit_history_m
             - 0.002*(income-350)/100 + np.random.normal(0, 0.6, n))
    prob_default = 1 / (1 + np.exp(-logit))
    target = np.random.binomial(1, prob_default)
    return pd.DataFrame({"income": income, "total_debt": total_debt, "card_util": card_util,
        "delinquencies": delinquencies, "loan_balance": loan_balance,
        "years_employed": years_employed, "credit_history_m": credit_history_m,
        "inquiries_6m": inquiries_6m, "dsr": dsr, "target": target})


def train(df, epochs=60):
    X = df[FEATURE_COLS].values
    y = df["target"].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)
    model = CreditRiskNet(len(FEATURE_COLS))
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.BCEWithLogitsLoss()
    X_train_t = torch.tensor(X_train_s, dtype=torch.float32)
    y_train_t = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)
    X_test_t = torch.tensor(X_test_s, dtype=torch.float32)
    for epoch in range(epochs):
        model.train()
        opt.zero_grad()
        loss = loss_fn(model(X_train_t), y_train_t)
        loss.backward()
        opt.step()
    model.eval()
    with torch.no_grad():
        test_probs = torch.sigmoid(model(X_test_t)).squeeze().numpy()
    auc = roc_auc_score(y_test, test_probs)
    acc = accuracy_score(y_test, (test_probs > 0.5).astype(int))
    print(f"검증 성능: AUC={auc:.3f}  Accuracy={acc:.3f}  <- 이 줄이 보여야 진짜 학습된 것")
    return model, scaler


if __name__ == "__main__":
    df = make_synthetic_data()
    model, scaler = train(df)
    torch.save(model.state_dict(), "credit_risk_model.pt")
    with open("scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)
    print("저장 완료: credit_risk_model.pt, scaler.pkl")
