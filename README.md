# 🧠 Early Diagnosis Tool for Alzheimer's Detection
Detect Alzheimer's Disease in its critical stages (Stage 3 & 4)

## 🚀 What It Does
This tool leverages advanced machine learning algorithms to detect whether a person may have Alzheimer's in the third or fourth stage, using MMSE,Functional Assessment, ADL tests and other simple questions. By identifying Alzheimer's in these critical stages, we aim to aid in early intervention and support for affected individuals.

## 🎯 Why This Project?
Alzheimer's Disease affects millions worldwide, often going undiagnosed until it has significantly progressed. Early diagnosis is key to improving the quality of life and enabling better treatment options. This project focuses on bridging that gap by offering a reliable detection tool that can assist healthcare professionals in identifying cases in the early stages of advanced Alzheimer's.

## ⚙️ How It Works
### Data Collection
We used a public dataset found on [kaggle.com](https://www.kaggle.com/datasets/sulimanabusamak123/alzheimers-public-dataset), of course this data was reviewed by doctors who agreed on its quality.

### Model Training
Using machine learning algorithms, such as LGBMClassifier, the model is trained to detect Alzheimer's disease patterns.

### Evaluation
The model's performance is evaluated using metrics like accuracy, cross_val_score, ensuring a balance between correctly detecting the disease and minimizing false positives.

## 🧬Features
* High Accuracy: Our model achieves 95.19% accuracy in detecting Alzheimer's at critical stages.
* Easy Integration: Plug this tool into any healthcare system for smooth integration with existing patient records.
* User-Friendly Interface: Designed for healthcare professionals with a clear, intuitive interface.
## 🛠️ Tech Stack
* Programming Language: Python

* Libraries:
Scikit-learn
, lightgbm
, xgboost
, Pandas, NumPy
, Matplotlib, Seaborn, joblib, Streamlit
* Tools:
Google Colab,
Git 

## 🤝 Contributing
Contributions are welcome! If you want to contribute to improving the tool or expanding its capabilities, feel free to create a pull request.


## 🙌 Acknowledgements
Special thanks to the doctors who created and approved of this data, and all the open-source contributors whose work made this project possible!

