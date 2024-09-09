# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import CountVectorizer

# # Load the dataset from preddata.csv
# df = pd.read_csv('data.csv')

# # Prepare the data
# X = df['Reaction'].values
# y = df['Type'].values

# # Encode the labels
# label_encoder = LabelEncoder()
# y_encoded = label_encoder.fit_transform(y)

# # Vectorize the reaction strings
# vectorizer = CountVectorizer()
# X_vectorized = vectorizer.fit_transform(X)

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y_encoded,test_size=0.2, random_state=42)

# # Train the Random Forest model
# rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
# rf_model.fit(X_train, y_train)

# def predict_reaction_type(reaction):
#     reaction_vectorized = vectorizer.transform([reaction])
#     prediction = rf_model.predict(reaction_vectorized)
#     return label_encoder.inverse_transform(prediction)[0]

# # Test predictions
# if __name__ == "__main__":
#     test_reactions = ['A + B -> AB', 'AB -> A + B', 'C + D -> CD']
#     for reaction in test_reactions:
#         predicted_type = predict_reaction_type(reaction)
#         print(f"Input : {reaction}, Predicted Type: {predicted_type}")

#--------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

try:
    df = pd.read_csv('data_pred.csv', quotechar='"', delimiter=',', skipinitialspace=True)
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    df = pd.DataFrame()

if not df.empty:
    # Prepare the data
    X = df['Equation'].values
    y = df['Type'].values

    # Encode the labels
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    # Train the Random Forest model
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train.reshape(-1, 1), y_train)

    def predict_reaction_type(reaction):
        prediction = rf_model.predict([reaction])
        return label_encoder.inverse_transform(prediction)[0]

    def get_reaction_details(reaction):
        try:
            details = df[df['Reaction'].str.lower() == reaction.lower()]
            if not details.empty:
                return details.iloc[0].to_dict()
            else:
                return None
        except Exception as e:
            print(f"Error retrieving reaction details: {e}")
            return None
else:
    def predict_reaction_type(reaction):
        return "Model not trained. CSV data could not be loaded."

    def get_reaction_details(reaction):
        return None


