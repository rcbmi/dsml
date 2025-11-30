#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 22. Compute Accuracy, Error rate, Precision, Recall for the following
# confusion matrix.
# Actual Class\Predicted

# class

# cancer =
# yes

# cancer = no Total

# cancer = yes 90 210 300
# cancer = no 140 9560 9700
# Total 230 9770 10000


# In[1]:


TP=90
FN=210
FP=140
TN=9560

Accuracy=(TP+TN)/(TP+TN+FN+FP)
ErrorRate=1-Accuracy
Precision=TP/(TP+FP)
Recall=TP/(TP+FN)

print(f"Accuracy is {Accuracy}")
print(f"ErrorRate is {ErrorRate}")
print(f"Precision is {Precision}")
print(f"Recall is {Recall}")


# In[ ]:




