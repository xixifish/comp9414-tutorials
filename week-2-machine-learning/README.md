# Decision Tree for Week 2 - COMP9414

All the programming tasks are in the Jupyter notebook file. 

## Recall & Accuracy & Precision
### Recall
- Recall = Detected Positive Predictions / All of Positive Cases
- Recall is critical when **missing a positive is the most costly mistake**. (Cancer/disease detection, Fraud detection, Criminal identification)
### Precision
- Precision = Correct Positive Predictions / All of predicted positives
- If the cost of a false alarm is high -> prioritize Precision
### Accuracy
- Accuracy = Correct Predictions / All the predictions
- When the dataset is balanced, accuracy is most useful

# Confusion Matrix
```
[[18 1 0]
 [0 12 1]
 [0 2 11]]
```
This means there are 3 classes(0, 1, 2 row), and for predicting class 0, there are 18 correct predictions (predicted them as class 0) and 1 wrong prediction (predicted this one as class 1).

