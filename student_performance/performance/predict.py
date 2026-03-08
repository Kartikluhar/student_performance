from .filter import filter_dataframe
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

def predict(file_path, g1, g2, failures, studytime, absences):

    main_df = filter_dataframe(file_path)

    X = main_df.drop(columns=['g3'])
    y = main_df['g3']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        max_depth=10,
        n_estimators=50,
        random_state=42
    )

    model.fit(X_train, y_train)

    # ✅ Calculate R2
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)

    input_data = [[g1, g2, failures, studytime, absences]]

    prediction = model.predict(input_data)

    return prediction[0], r2