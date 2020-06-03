import torch

N, D_in, H, D_out = 64, 1000, 100, 10
# 随机初始化一些训练数据
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)

w1 = torch.randn(D_in, H)
w2 = torch.randn(H, D_out)

learning_rate = 1e-06
for it in range(500):
    # Forward pass
    h = x.mm(w1)  # N*H
    h_rule = h.clamp(min=0)  # N*H
    y_pred = h_rule.mm(w2)  # N*D_out

    # computer loss
    loss = (y_pred - y).pow(2).sum().item()
    print(it, loss)

    # computer loss
    # computer the gradient
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_rule.t().mm(grad_y_pred)
    grad_h_rule = grad_y_pred.mm(w2.t())
    grad_h = grad_h_rule.clone()
    grad_h[h < 0] = 0
    grad_w1 = x.t().mm(grad_h)

    # update weights of w1 and w2
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2