# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a machine learning classifier trained to predict whether a person’s income is greater than $50K per year based on census data. The model uses a Random Forest classifier. The training pipeline includes data preprocessing, one-hot encoding of categorical features, label binarization, model training, inference, and evaluation.
## Intended Use
The intended use of this model is educational. It is designed to demonstrate how to build, evaluate, and deploy a machine learning model using FastAPI and a reproducible ML pipeline.
## Training Data
The training data comes from the UCI Census Income dataset. It includes demographic and employment-related features such as age, workclass, education, marital-status, occupation, race, sex, hours-per-week, and native-country. The target variable indicates whether a person earns more than $50K per year.
## Evaluation Data
The evaluation data was created by splitting the original dataset into training and test sets using an 80/20 split. The test set was held out from training and used to evaluate model performance.
## Metrics
The model was evaluated using precision, recall, and F1 score. The model achieved: Precision: 0.7419 | Recall: 0.6384 | F1: 0.6863.
## Ethical Considerations
This dataset contains demographic attributes such as race and sex, which can lead to biased model behavior across groups.
## Caveats and Recommendations
Performance may vary across demographic groups and may not generalize well to current real-world populations.