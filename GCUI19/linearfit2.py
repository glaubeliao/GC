import pandas as pd

#create DataFrame
df = pd.DataFrame({'x': [1, 2, 2, 4, 2, 1, 5, 4, 2, 4, 4, 3, 6],
                   'y': [1, 3, 3, 5, 2, 2, 1, 1, 0, 3, 4, 3, 2],
                   'score': [76, 78, 85, 88, 72, 69, 94, 94, 88, 92, 90, 75, 96]})

#view DataFrame
print(df)


from sklearn.linear_model import LinearRegression

#initiate linear regression model
model = LinearRegression()

#define predictor and response variables
X, y = df[["x", "y"]], df.score

#fit regression model
model.fit(X, y)

#calculate R-squared of regression model
r_squared = model.score(X, y)

#view R-squared value
print(r_squared)

0.7175541714105901
