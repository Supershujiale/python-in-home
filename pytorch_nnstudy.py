import torch
import torch.nn as nn

N, D_in, H, D_out = 64, 1000, 100, 10
# 随机初始化一些训练数据
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)


class TwolayerNet(torch.nn.Module):
    def __init__(self, D_in, H, D_out):
        super(TwolayerNet,self).__init__()
        self.Linear1 = torch.nn.Linear(D_in, H)
        self.Linear2 = torch.nn.Linear(H, D_out)

    def forward(self, x):
        y_pred = self.Linear2(self.Linear1(x).clamp(min=0))
        return y_pred


model = TwolayerNet(D_in,H,D_out)
# torch.nn.init.normal_(model[0].weight)
# torch.nn.init.normal_(model[2].weight)
loss_fn = nn.MSELoss(reduction='sum')
learning_rate = 1e-04
optimizer = torch.optim.Adam(model.parameters(),lr=learning_rate)

for it in range(500):
    # Forward pass
    y_pred = model(x)#model.forward pass

    # computer loss
    loss = loss_fn(y_pred, y)
    print(it, loss.item())

    model.zero_grad()

    # computer loss
    # computer the gradient
    loss.backward()

    # update weights of w1 and w2
    with torch.no_grad():
        for param in model.parameters():
            param -= learning_rate*param.grad