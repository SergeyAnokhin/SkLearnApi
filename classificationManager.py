import numpy as np
import timeit
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

class ClassificationManager:
    classifiers = {
        "Neural Net(Adam, a.1)":     
            MLPClassifier(alpha=.1, max_iter=1000, solver='adam'), # , verbose=10
        "Neural Net(Adam, a.01)":     
            MLPClassifier(alpha=.01, max_iter=500, solver='adam'), # , verbose=10
        "Neural Net(Adam)":     
            MLPClassifier(alpha=1, max_iter=500, solver='adam'), # , verbose=10
        "Naive Bayes":          
            GaussianNB(),
        "RBF SVM":              
            SVC(gamma=2, C=1),
        # "Neural Net(Sgd)":      
        #     MLPClassifier(alpha=1e-2, max_iter=1000, solver='sgd'), # , verbose=10
        "Neural Net(Sgd, tol)":      
            MLPClassifier(alpha=1e-2, tol=1e-4, max_iter=500, solver='sgd', random_state=1,
                    learning_rate_init=.1), # , verbose=10
        #"Linear SVM":           SVC(kernel="linear", C=0.025),
        #"Nearest Neighbors":    
        #    KNeighborsClassifier(3),
        "Gaussian Process":     
            GaussianProcessClassifier(1.0 * RBF(1.0)),
        # "Random Forest":        
        #     RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
        "Decision Tree":        
            DecisionTreeClassifier(max_depth=5),
        # "AdaBoost":             
        #     AdaBoostClassifier(),
        #"QDA":                  QuadraticDiscriminantAnalysis(),
    }

    def Init(self):
        pass

    def status(self):
        return self.classifiers

    def fitBinary(self, learnData):
        results = []
        for key in self.classifiers:
            result = ClassificationPrediction()
            print('Fit : {}'.format(key))
            clf = self.classifiers[key]
            d_X = []
            d_Y = []
            for d in learnData:
                d_X.append(d['Image'])
                d_Y.append(d['ClassName'])
            X = np.asarray(d_X)
            Y = np.asarray(d_Y)
            start_time = timeit.default_timer()
            clf.fit(X, Y)
            result.Seconds = timeit.default_timer() - start_time
            if hasattr(clf, 'loss_'):
                result.Probability = clf.loss_
            results.append(result.__dict__)
        return results

    def predictBinary(self, learnData):
        results = []
        for key in self.classifiers:
            result = ClassificationPrediction()
            print('Predict : {}'.format(key))
            clf = self.classifiers[key]
            d_X = []
            #d_Y = []
            for d in learnData:
                d_X.append(d['Image'])
                #d_Y.append(d['ClassName'])
            X = np.asarray(d_X)
            #Y = np.asarray(d_Y)
            start_time = timeit.default_timer()
            Y = clf.predict(X)
            print(Y)
            result.Seconds = timeit.default_timer() - start_time
            result.Class = Y[0]
            results.append(result.__dict__)
        return results

class ClassificationPrediction:
    Brain = {}
    Class = None
    Probability = 0
    Probabilities = {}
    Seconds = 0