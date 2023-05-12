**WATER QUALITY PREDICTION USING MACHINE LEARNING**

This project discusses the importance of water quality prediction using machine learning models and data science techniques. In recent years, water quality has been put at risk due to industrial and agricultural activities, oil spills, and other environmental concerns. As a result, it is critical for us to develop accurate predictive models for water quality. Using machine learning and data science, we can analyse vast amounts of data that can help us build models to predict water quality. In this paper, we will discuss the data sources, machine learning models, and data science techniques that can be used to understand and predict water quality. We will also provide a brief overview of existing models and discuss the areas that need improvement. Via the project study the performance of artificial intelligence techniques including artificial neural network (ANN), group method of data handling (GMDH) and support vector machine (SVM)To develop the ANN and SVM, different types of transfer and kernel functions were tested, respectively. Reviewing the results of ANN and SVM indicated that both models have suitable performance for predicting water quality components. During the process of development of ANN and SVM, it was found that tansig and RBF as transfer and kernel functions have the best performance among the tested functions. Comparison of outcomes of GMDH model with other applied models shows that although this model has acceptable performance for predicting the components of water quality, its accuracy is slightly less than ANN and SVM. The evaluation of the accuracy of the applied models according to the error indexes declared that SVM was the most accurate model. Examining the results of the models showed that all of them had some over-estimation properties. By evaluating the results of the models based on the DDR index, it was found that the lowest DDR value was related to the performance of the SVM model.

**EXISTING SYSTEM**

In Existing system, the dataset has to be manually analysed with individual scripts which is a very slow process to analyse the complete data set, where the dataset can't be changed (static dataset) and the User experience (UX) is very complicated as it doesn't contain any User Interference (UI), also it is not cross-platform such that it can be executed only after satisfying the package requirements (Dependent Script).

**Disadvantages** : **Complicated UX**.

User experience (UX) is the process of designing and improving the interaction between users and digital products or services. When UX is complicated, it means that the design and structure of the product or service are complex, confusing, or overwhelming for the user. Complicated UX due to poor information architecture, unclear navigation and confusing terminology can frustrate users, decrease engagement.

**Not Cross Platform.**

Cross-platform refers to the ability of a product or service to work seamlessly on different operating systems and devices. When a product or service is missing cross-platform capabilities, it means that it is limited to specific platforms, which can be a significant disadvantage for users.

**Time Consuming.**

Time complexity refers to the amount of time it takes for an algorithm to run or for a function to execute, as a function of the size of its input. It is a measure of the efficiency of an algorithm, and it helps to determine how well it will perform as the size of the input grows.

**PROPOSED SYSTEM**

In proposed system, the User Experience (UX) is very human-centric and understandable as it contains a Graphical User Interference (GUI) so it is easy to analyse any dataset in a single execution with multiple graphs and charts, even multiple datasets can be analysed together which is not possible in existing model also it is cross-platform such that all the package requirements are predefined and installed along with the script which makes it a platform independent script.

**Advantages** : **GUI Based – Better UX.**

GUI (Graphical User Interface) plays a significant role in creating a better user experience (UX) for digital products. A well-designed GUI can make it easier for users to interact with a product, understand how it works, and accomplish their goals more efficiently.

**Platform Independent Script.**

A platform-independent script is a script that can run on multiple platforms or operating systems without requiring any modifications or adjustments. This means that the script can be written once and then deployed on any platform that supports the required scripting environment.

**Large dataset can be processed in very less time.**

Processing large datasets can be a time-consuming task, especially if the data needs to be processed in real-time through various methods and techniques like RNN, Faker, Random can help to process large datasets quickly.

**SOFTWARE SPECIFICATION**

| **COMPONENTS** | **REQUIREMENTS** |
| --- | --- |
| OPERATING SYSTEM | Windows 8 and Above |
| FRONT END | Python (TKinter) |
| ML DATA SET | Water Quality Dataset in CSV |
| BACK END | Python (Seaborn) |

**HARDWARE SPECIFICATION**

| **COMPONENTS** | **REQUIREMENTS** |
| --- | --- |
| CPU | x86 64-bit CPU (Intel / AMD architecture) |
| RAM | 2GB Minimum |
| STORAGE | 5GB Minimum disk space |
| PERIPHERALS | Common Peripherals (Mouse, Keyboard,..) |

**MODULE DESCRIPTION**

**Machine Learning – Data Set**

A dataset in machine learning is, quite simply, a collection of data pieces that can be treated by a computer as a single unit for analytic and prediction purposes. This means that the data collected should be made uniform and understandable for a machine that doesn't see data the same way as humans do. For this, after collecting the data, it's important to pre-process it by cleaning and completing it, as well as annotate the data by adding meaningful tags readable by a computer.

A tabular dataset can be understood as a database table or matrix, where each column corresponds to a particular variable, and each row corresponds to the fields of the dataset. The most supported file type for a tabular dataset is "Comma Separated File," or CSV. But to store a "tree-like data," we can use the JSON file more efficiently.


FIG 1 : DataSet – Reviews Set by Kaggle<img width="452" alt="Picture1" src="https://github.com/kheshore/Water-Quality-Prediction/assets/43311731/f5403c43-d4f9-466b-8fcb-a78d5b981422">


The above dataset (FIG 1) includes 23486 rows and 10 feature variables. Each row corresponds to a water test result, and includes the variables:

**NLP**

Natural language processing (NLP) refers to the branch of computer science and more specifically, the branch of artificial intelligence or AI—concerned with giving computers the ability to understand text and spoken words in much the same way human beings can.

NLP combines computational linguistics—rule-based modelling of human language—with statistical, machine learning, and deep learning models. Together, these technologies enable computers to process human language in the form of text or voice data and to 'understand' its full meaning, complete with the speaker or writer's intent and sentiment.

NLP drives computer programs that translate text from one language to another, respond to spoken commands, and summarize large volumes of text rapidly—even in real time. There's a good chance you've interacted with NLP in the form of voice-operated GPS systems, digital assistants, speech-to-text dictation software, customer service chatbots, and other consumer conveniences. But NLP also plays a growing role in enterprise solutions that help streamline business operations, increase employee productivity, and simplify mission-critical business processes.

**Seaborn**

Seaborn is a library for making statistical graphics in Python. It builds on top of matplotlib and integrates closely with pandas data structures.

Seaborn helps to explore and understand the data. Its plotting functions operate on data frames and arrays containing whole datasets and internally perform the necessary semantic mapping and statistical aggregation to produce informative plots. Its dataset-oriented, declarative API lets you focus on what the different elements of your plots mean, rather than on the details of how to draw them.

**Tkinter**

Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

The tkinter package ("Tk interface") is the standard Python interface to the Tcl/Tk GUI toolkit. Both Tk and tkinter are available on most Unix platforms, including macOS, as well as on Windows systems.
