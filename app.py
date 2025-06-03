
from torch import cuda

import torch

print(cuda.is_available())

print("CUDA 支持版本:", torch.version.cuda)