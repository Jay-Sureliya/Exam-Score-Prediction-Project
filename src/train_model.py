import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler , OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score
import joblib 

df = pd.read_csv('data\Exam_Score_Prediction.csv')

df = df[['study_hours','class_attendance','sleep_hours','study_method','sleep_quality','exam_score']]

encoder_col = ['study_method', 'sleep_quality']
scaler_col = ['study_hours', 'class_attendance', 'sleep_hours']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), scaler_col),
        ('cat', OneHotEncoder(handle_unknown='ignore'), encoder_col)
    ]
)
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

X = df.drop('exam_score', axis=1)
y = df['exam_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)


r2_score_value = r2_score(y_test, y_pred)
print(f'R^2 Score: {r2_score_value}')

joblib.dump(pipeline, "model/exam_score_model.pkl")