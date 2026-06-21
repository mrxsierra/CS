---
title: Deep Learning Foundations
tags: ['stack/data']
created: 2026-06-10
---

# Deep Learning Foundations

## Overview
Deep Learning interviews test your understanding of neural network fundamentals — backpropagation, activation functions, architectures, and the PyTorch/TensorFlow ecosystems.

## Neural Network Fundamentals

### The Perceptron → Multi-Layer Network
```
Input  →  Hidden Layer 1  →  Hidden Layer 2  →  Output
x1 ────── h1 ────────────── h3 ──────────────── y1
x2 ────── h2 ────────────── h4 ──────────────── y2
            ║ activation      ║ activation
          weight matrix W₁  weight matrix W₂
```

### Forward Pass
```
z = W·x + b
a = activation(z)  # e.g., ReLU, sigmoid, tanh
output = a (for hidden layers) or directly z (for output)
```

### Backpropagation (The Chain Rule)
1. Compute loss: L = MSE(y_pred, y_true)
2. Gradient w.r.t. output: dL/dz_L = y_pred - y_true
3. Propagate backward: dL/dW_i = (dL/da_i) · (da_i/dz_i) · (dz_i/dW_i)
4. Update weights: W_i = W_i - learning_rate · dL/dW_i

### Activation Functions
| Function | Range | Pros | Cons |
|----------|-------|------|------|
| **ReLU** | [0, ∞) | Fast, sparse (dead neurons can be a feature) | Dying ReLU |
| **Leaky ReLU** | (-∞, ∞) | Solves dying ReLU | Slightly more compute |
| **Sigmoid** | (0, 1) | Output is probability | Vanishing gradient |
| **Tanh** | (-1, 1) | Zero-centered | Still saturates |
| **GELU** | ≈(-0.17, ∞) | Used in Transformers (GPT, BERT) | More complex |
| **Swish/SiLU** | ≈(-0.28, ∞) | Self-gated, smooth | Newer, less studied |

## Architectures

### CNNs (Convolutional Neural Networks)
```python
# Key idea: Convolution kernels learn spatial features
# Conv2D: filter_size, stride, padding
# Pooling: MaxPool (downsample, keep strongest features)
# Modern: ResNet (skip connections), EfficientNet (compound scaling)

input_shape = (224, 224, 3)
x = Conv2D(64, (3,3), activation='relu', padding='same')(input)
x = MaxPooling2D((2,2))(x)
x = Conv2D(128, (3,3), activation='relu', padding='same')(x)
x = GlobalAveragePooling2D()(x)
output = Dense(num_classes, activation='softmax')(x)
```

### RNNs / LSTMs (Sequential Data)
- **RNN**: Hidden state passed through time steps. Suffers from vanishing gradients.
- **LSTM**: Three gates (forget, input, output) + cell state → controls gradient flow.
- **GRU**: Simplified LSTM — reset + update gates, fewer parameters.

### Transformers — The Modern Standard
```python
# Key innovation: Self-Attention
# Attention(Q, K, V) = softmax(Q · K^T / sqrt(d_k)) · V
# Q = what am I looking for?
# K = what do I contain?
# V = what do I output?

# Multi-Head Attention: Run Attention in parallel, concatenate results
# Positional Encoding: Sinusoidal functions to encode position
# LayerNorm + Residual connections → stable training of very deep networks
```

## PyTorch vs. TensorFlow (2026)

| Aspect | PyTorch | TensorFlow / Keras |
|--------|---------|-------------------|
| **Style** | Imperative (Pythonic) | Declarative (graph-based, though TF2 is eager) |
| **Debugging** | Standard Python debugger | tfdbg |
| **Production** | TorchServe, onnx | TF Serving, TFLite |
| **Research** | Dominant (most papers use it) | Legacy |
| **Mobile** | PyTorch Mobile | TFLite (better) |

## Common Interview Questions

1. **"Explain the vanishing gradient problem."** — In deep networks, gradients get exponentially smaller as they backpropagate, preventing early layers from learning. Solutions: ReLU activations, residual connections (ResNet), layer normalization, proper weight initialization (He/Xavier).

2. **"What is the difference between Batch Normalization and Layer Normalization?"** — Batch Norm normalizes across the batch dimension (bad for small batch sizes / RNNs). Layer Norm normalizes across the feature dimension (used in Transformers, works well for sequential data).

3. **"How does dropout prevent overfitting?"** — Randomly drops neurons during training (keeps a fraction p). Forces network to learn redundant representations. At inference, all neurons are used (weight scaling).

4. **"Explain attention score computation."** — Dot product of Q and K gives attention scores, scaled by 1/sqrt(d_k) to prevent softmax saturation, then softmax gives attention weights, multiplied by V.

## Related Topics
- [[08_Stack_Deep_Dives/03_Data_AI_Stack/05_LLMs_LangChain|LLMs & AI Orchestration]]
- [[08_Stack_Deep_Dives/03_Data_AI_Stack/03_Machine_Learning|Machine Learning Mastery]]
- [[08_Stack_Deep_Dives/03_Data_AI_Stack/Index|Data & AI Stack Index]]
- [[02_Role_Tracks/04_ML_Engineer|ML Engineer Track]]

## Resources
- [Deep Learning (Goodfellow et al.)](https://www.deeplearningbook.org/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [d2l.ai — Dive into Deep Learning](https://d2l.ai/)
- [3Blue1Brown Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)