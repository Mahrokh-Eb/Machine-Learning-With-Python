#!/usr/bin/env python
# coding: utf-8

# # SVM Loss Function

# ### unvectorized implementation - näive

# def l_i(x, y, w):
#     scores = w.dot(x)
#     correct_class_score = scores[y]
#     c =w.shape[0]
#     
#     loss_i = 0.0
#     for j in range(c):
#         if j==c:
#             continue
#         loss_i += max(0, scores[j] - correct_class_score +1.0)
#     return loss_i

# ### Half_vectorized implementation

# In[6]:


import numpy as np
def l_i_half_vectorized(x, y, w):
    scores = w.dot(x)
    margins = np.maximum(0, scores - scores[y] + 1.0)
    margins[y] = 0
    loss_i = np.sum(margins)
    return loss_i


# ### Fully_vectorized implementation

# In[11]:


def l_i_fully_vectorised(x, y, w):
    N = scores.shape[0]
    scores = w.dot(x)
    correct_class_score = scores[range(N), y]
    margins = np.maximum(0.0, scores - correct_class_score[:,None] + 1.0)
    margins[range(N), y] = 0.0
    loss = np.sum(margins) / N
    return loss


# # Softmax Loss Function 

# ### unvectorized implementation - näive

# In[14]:


def softmax_loss_naive(scores, y, W, reg=1e-3):
    
    N, C = scores.shape

    # compute data loss
    loss = 0.0
    for i in range(N):
        correct_class = y[i]
        score = scores[i]
        score -= np.max(scores)
        exp_score = np.exp(score)
        probs = exp_score / np.sum(exp_score)
        loss += -np.log(probs[correct_class])

    loss /= N

    # compute regularization loss
    loss += 0.5 * reg * np.sum(W * W)

    # Compute gradient off loss function w.r.t. scores
    # We will write this part later
    grads = {}  

    return loss, grads


# ### Half_vectorized implementation

# In[13]:


def softmax_loss(scores, y, W, reg=1e-3):
    N = scores.shape[0]  # number of input data

    # compute data loss
    scores -= np.max(scores, axis=1, keepdims=True)
    exp_scores = np.exp(scores)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    loss = -np.sum(np.log(probs[range(N), y])) / N

    # compute regularization loss
    loss += 0.5 * reg * np.sum(W * W)

    # Compute gradient off loss function w.r.t. scores
    # We will write this part later
    grads = {}  

    return loss, grads   


# ### Softmax loss, forward and backward

# In[15]:


def softmax_loss(s, y):
    
    #forward step
    shifted_log = s - np.max(s, axis=1, keepdims=True)
    z = np.sum(np.exp(shifted_log), axis=1, keepdims=True)
    log_probs = shifted_log - np.log(z)
    probs = np.exp(log_probs)
    N = s.shape[0]
    loss = -np.sum(log_probs[np.arange(N), y]) / N
    
    #backward step
    ds = probs.copy() 
    ds[np.arange(N), y] -= 1
    ds /= N
    return loss, ds


# In[ ]:




