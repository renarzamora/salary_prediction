## We evaluate a salary dataset with Linear Regression, Random Forest and Support Vector Regression (SVR), ending with a simple deployment in Streamlit

![alt text](image_nL6IwJo.jpg)

## We evaluated a small salary dataset, when the amount of data is not important a concrete way to get accuracy is to evaluate with several models, here we did it with linear regression, random forest and support vector regression (SVR), in the end we chose one to implement it with Streamlit, we used Joblib to save and it brings the scaling and modeling, thus we avoid doing it during deployment.

### EDA Process

![alt text](picture1.png)

![alt text](picture2.png)

![alt text](picture3.png)

![alt text](picture4.png)

## Finding out insights

![alt text](picture5.png)

![alt text](picture6.png)

## Modeling and evaluating: Linear Regression, Support Vector Regression and Random Forest

![alt text](picture8.png)

![alt text](picture9.png)

![alt text](picture10.png)

**We choose Linear Regression Model, since this got the minimus values for Mean Absolute Erro and Mean Squared Error**
![alt text](picture8.png)

## Finally we deploy it with Streamlit: you can run it: streamlit run app.py

![alt text](picture7.png)

**Author**
------------

* Renar Zamora - renarzamora@gmail.com

**Tools**
----------------

* Python 3.11, Visual Studio Code, Streamlit, Scikit Learn, Matplotlib, Joblib, Pandas and Numpy