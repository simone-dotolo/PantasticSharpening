import torch
from torch import nn
from typing import List

# TODO: investigate scope

# Input -> MS bands + PAN band
# Output -> MS bands

class PNN(nn.Module):
    def __init__(self, input_channels : int, kernels : List[int]):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=input_channels,
                               out_channels=48,
                               kernel_size=kernels[0],
                               stride=1,
                               padding=0)
        self.conv2 = nn.Conv2d(in_channels=48,
                               out_channels=32,
                               kernel_size=kernels[1],
                               stride=1,
                               padding=0)
        self.conv3 = nn.Conv2d(in_channels=32,
                               out_channels=input_channels-1,
                               kernel_size=kernels[2],
                               stride=1,
                               padding=0)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.relu(self.conv1(x))
        out = self.relu(self.conv2(out))
        out = self.conv3(out)
        return out + x[:, :-1, :, :]