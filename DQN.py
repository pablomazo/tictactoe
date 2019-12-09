import torch
import torch.nn as nn
import torch.nn.functional as F

class DQN(nn.Module):
    def __init__(self, D_in, H1, H2, D_out):
        super(DQN, self).__init__()
        self.lin1 = nn.Linear(D_in, H1)
        self.lin2 = nn.Linear(H1, H2)
        self.lin3 = nn.Linear(H2, D_out)
        self.transfer = nn.ReLU()

    def forward(self, x):
        x = F.relu(self.lin1(x))
        x = F.relu(self.lin2(x))
        x = self.lin3(x)
        return x