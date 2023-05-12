# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title('Suriya varshini S - Water Quality Data Processing')
Name = tk.Label(text="Select The DataSet")
Name1 = tk.Label(text="Water Quality Prediction Project")
Name2 = tk.Label(text="By Suriya varshini S")
Name1.pack()
Name2.pack()
Name.pack()

def select_file():
    global filename
    filename =  0
    filetypes = (
        ('csv files', '*.csv'),
    )

    filename = fd.askopenfilename(
        title='Select a CSV File',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )
    showinfo(
        title='Processing...',
        message='Close the "Select The DataSet" Dialog Box to Get Analytics'

    )

    

open_button = ttk.Button(
    window,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)


window.mainloop()

while (filename!=0):

    df=pd.read_csv(filename)
    df.fillna(df.mean(), inplace=True)

    df.describe()

    df.Potability.value_counts().plot(kind="bar", color=["brown", "salmon"], title='Potability - Water Quality Prediction By Suriya varshini S')
    plt.show()

    sns.displot(df['ph']).set(title='pH Distribution - Water Quality Prediction By Suriya varshini S')

    df.hist(figsize=(14,14))
    plt.title('pH Distribution - Water Quality Prediction By Suriya varshini S')
    plt.show()
    sns.pairplot(df,hue='Potability').fig.suptitle('Water Quality Prediction By Suriya varshini S')


    # create a correlation heatmap
    sns.heatmap(df.corr(),annot=True, cmap='terrain', linewidths=0.1).set(title='Heat Map Distribution - Water Quality Prediction By Suriya varshini S')
    fig=plt.gcf()
    fig.set_size_inches(8,6)
    plt.show()
    df.boxplot(figsize=(14,7)).set(title='Box Plot - Water Quality Prediction By Suriya varshini S')
    X = df.drop('Potability',axis=1)
    Y= df['Potability']
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size= 0.2, random_state=101,shuffle=True)
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score,confusion_matrix,precision_score
    dt=DecisionTreeClassifier(criterion= 'gini', min_samples_split= 10, splitter= 'best')
    dt.fit(X_train,Y_train)
    prediction=dt.predict(X_test)
    accuracy_dt=accuracy_score(Y_test,prediction)*100
    print("Accuracy on training set: {:.3f}".format(dt.score(X_train, Y_train)))
    print("Accuracy on test set: {:.3f}".format(dt.score(X_test, Y_test)))
    X_DT=dt.predict([[5.735724, 158.318741,25363.016594,7.728601,377.543291,568.304671,13.626624,75.952337,4.732954]])
    from sklearn.neighbors import KNeighborsClassifier
    knn=KNeighborsClassifier(metric='manhattan', n_neighbors=22)
    knn.fit(X_train,Y_train)
    prediction_knn=knn.predict(X_test)
    accuracy_knn=accuracy_score(Y_test,prediction_knn)*100
    print('accuracy_score score     : ',accuracy_score(Y_test,prediction_knn)*100,'%')
    dt.get_params().keys()
    from sklearn.model_selection import RepeatedStratifiedKFold
    from sklearn.model_selection import GridSearchCV
    model = DecisionTreeClassifier()
    criterion = ["gini", "entropy"]
    splitter = ["best", "random"]
    min_samples_split = [2,4,6,8,10]
    grid = dict(splitter=splitter, criterion=criterion, min_samples_split=min_samples_split)
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    grid_search_dt = GridSearchCV(estimator=model, param_grid=grid, n_jobs=-1, cv=cv, 
                            scoring='accuracy',error_score=0)
    grid_search_dt.fit(X_train, Y_train)
    means = grid_search_dt.cv_results_['mean_test_score']
    stds = grid_search_dt.cv_results_['std_test_score']
    params = grid_search_dt.cv_results_['params']
        
    print("Training Score:",grid_search_dt.score(X_train, Y_train)*100)
    print("Testing Score:", grid_search_dt.score(X_test, Y_test)*100)
    dt_y_predicted = grid_search_dt.predict(X_test)
    dt_grid_score=accuracy_score(Y_test, dt_y_predicted)
    dt_grid_score
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import RepeatedStratifiedKFold
    from sklearn.model_selection import GridSearchCV
    model = KNeighborsClassifier()
    n_neighbors = range(1, 31)
    weights = ['uniform', 'distance']
    metric = ['euclidean', 'manhattan', 'minkowski']
    grid = dict(n_neighbors=n_neighbors,weights=weights,metric=metric)
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=1, random_state=1)
    grid_search_knn = GridSearchCV(estimator=model, param_grid=grid, n_jobs=-1, cv=cv, 
                            scoring='accuracy',error_score=0)
    grid_search_knn.fit(X_train, Y_train)
    means = grid_search_knn.cv_results_['mean_test_score']
    stds = grid_search_knn.cv_results_['std_test_score']
    params = grid_search_knn.cv_results_['params']



