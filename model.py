import torch.nn as nn

FEATURE_COLS = [
    "income", "total_debt", "card_util", "delinquencies", "loan_balance",
    "years_employed", "credit_history_m", "inquiries_6m", "dsr",
]


class CreditRiskNet(nn.Module):
    def __init__(self, in_dim: int = len(FEATURE_COLS)):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 32), nn.ReLU(), nn.Dropout(0.2),
            nn.Linear(32, 16), nn.ReLU(),
            nn.Linear(16, 1),
        )

    def forward(self, x):
        return self.net(x)
