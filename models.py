import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV

label_encoder = LabelEncoder()
trainingdata = pd.read_json('output.json')

trainingdata['cardNames'] = trainingdata['cardNames'].apply(lambda x: ' '.join(x))

y = trainingdata['username']
X = trainingdata['cardNames']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

vectorizer = TfidfVectorizer(lowercase=True)

naivebayesmodel = make_pipeline(vectorizer, MultinomialNB())
RFmodel = make_pipeline(CountVectorizer(), RandomForestClassifier())

naivebayesmodel.fit(X_train, y_train)
RFmodel.fit(X_train, y_train)

nbpred = naivebayesmodel.predict(X_test)
rfpred = RFmodel.predict(X_test)

nbaccuracy = accuracy_score(y_test, nbpred)

cm = confusion_matrix(y_test, nbpred)

cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
plt.figure(figsize=(12, 8))  # Increase the figure size if needed
sns.heatmap(cm_normalized, annot=True, fmt='.2f', cmap='Blues', xticklabels=naivebayesmodel.classes_, yticklabels=naivebayesmodel.classes_)

plt.title('Normalized Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')

# Adjust layout to ensure everything fits without cutting off
plt.tight_layout()

# Save the plot as a JPEG file
plt.savefig('normalized_nb_cm.jpg', format='jpg')

# Optionally close the plot if you don't want it to display
plt.close()

RFaccuracy = accuracy_score(y_test, rfpred)
print(f'Accuracy: {nbaccuracy}')

report = classification_report(y_test, nbpred, output_dict=True, zero_division=0)

# Convert the classification report into a DataFrame for easy visualization
report_df = pd.DataFrame(report).transpose()

# Drop the last row 'accuracy' if it's present in the dataframe
if 'accuracy' in report_df.index:
    report_df = report_df.drop('accuracy')

# Set up the matplotlib figure
plt.figure(figsize=(10, 7))

# Create a heatmap from the DataFrame
sns.heatmap(report_df.iloc[:, :-1], annot=True, cmap='Blues', fmt='.2f', cbar=True, 
            xticklabels=['Precision', 'Recall', 'F1-Score'], yticklabels=report_df.index, 
            annot_kws={"size": 10}, linewidths=0.5)

# Set plot title
plt.title('Naive Bayes Classification Report')

plt.tight_layout()
plt.savefig('nb_clasification_report.jpg', format='jpg')

# Optionally close the plot if you don't want it to display
plt.close()
# THIS IS JHUST A PLACEHOLDER SO I DONT LOSE MY PLACE
print(f'Accuracy: {RFaccuracy}')
report = classification_report(y_test, rfpred, output_dict=True, zero_division=0)

# Convert the classification report into a DataFrame for easy visualization
report_df = pd.DataFrame(report).transpose()

# Drop the last row 'accuracy' if it's present in the dataframe
if 'accuracy' in report_df.index:
    report_df = report_df.drop('accuracy')

# Set up the matplotlib figure
plt.figure(figsize=(10, 7))

# Create a heatmap from the DataFrame
sns.heatmap(report_df.iloc[:, :-1], annot=True, cmap='Blues', fmt='.2f', cbar=True, 
            xticklabels=['Precision', 'Recall', 'F1-Score'], yticklabels=report_df.index, 
            annot_kws={"size": 10}, linewidths=0.5)

# Set plot title
plt.title('Random Forest Classification Report')

plt.tight_layout()
plt.savefig('rf_clasification_report.jpg', format='jpg')

# Optionally close the plot if you don't want it to display
plt.close()
cm = confusion_matrix(y_test, rfpred)

cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
plt.figure(figsize=(12, 8))  # Increase the figure size if needed
sns.heatmap(cm_normalized, annot=True, fmt='.2f', cmap='Blues', xticklabels=RFmodel.classes_, yticklabels=RFmodel.classes_)

plt.title('Normalized Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')

# Adjust layout to ensure everything fits without cutting off
plt.tight_layout()

# Save the plot as a JPEG file
plt.savefig('normalized_RF_cm.jpg', format='jpg')

# Optionally close the plot if you don't want it to display
plt.close()

svm_model = make_pipeline(vectorizer, LinearSVC())
svm_model.fit(X_train, y_train)

# Predict
SVMpred = svm_model.predict(X_test)

# Evaluate
SVCaccuracy = accuracy_score(y_test, SVMpred)
print(f'Accuracy: {SVCaccuracy}')
report = classification_report(y_test, SVMpred, output_dict=True, zero_division=0)

# Convert the classification report into a DataFrame for easy visualization
report_df = pd.DataFrame(report).transpose()

# Drop the last row 'accuracy' if it's present in the dataframe
if 'accuracy' in report_df.index:
    report_df = report_df.drop('accuracy')

# Set up the matplotlib figure
plt.figure(figsize=(10, 7))

# Create a heatmap from the DataFrame
sns.heatmap(report_df.iloc[:, :-1], annot=True, cmap='Blues', fmt='.2f', cbar=True, 
            xticklabels=['Precision', 'Recall', 'F1-Score'], yticklabels=report_df.index, 
            annot_kws={"size": 10}, linewidths=0.5)

# Set plot title
plt.title('LinearSVC Classification Report')

plt.tight_layout()
plt.savefig('svm_clasification_report.jpg', format='jpg')

# Optionally close the plot if you don't want it to display
plt.close()

cm = confusion_matrix(y_test, SVMpred)

cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
plt.figure(figsize=(12, 8))  # Increase the figure size if needed
sns.heatmap(cm_normalized, annot=True, fmt='.2f', cmap='Blues', xticklabels=svm_model.classes_, yticklabels=svm_model.classes_)

plt.title('Normalized Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')

# Adjust layout to ensure everything fits without cutting off
plt.tight_layout()

# Save the plot as a JPEG file
plt.savefig('normalized_svm_cm.jpg', format='jpg')

# Optionally close the plot if you don't want it to display
plt.close()