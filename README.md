Personal note: You should know that I had very little knowledge of machine learning and deep learning before starting this project. I had to go through a lot of content and courses 
(Thank you [Andrew Ng](https://www.youtube.com/watch?v=vStJoetOxJg&list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI) and [folks at Google BI specialization](https://www.coursera.org/professional-certificates/google-business-intelligence)!) 
while implementing this project, and I hope it can help, and inspire others. As I mentioned, I am relatively new to the tech industry and data science, so constructive criticism would be greatly appreciated. 

# Spending Tracker

**Dashboard Preview:**



https://github.com/user-attachments/assets/76295cfc-1dce-4766-be97-80276ff94d63




## Overview

The **Spending Tracker** project leverages AI to categorize financial transactions, aiming to inspire the tech community to integrate AI into daily tasks. By fine-tuning the DistilBERT model, I achieved a multiclass classification system that sorts transactions into 20 distinct categories. The open-source model ensures data privacy as it operates locally, not requiring internet connectivity for processing personal bank data. The beauty of fine-tuning is that you can get personized result. I tested the trained model with my data and then compared its performance against an online service provider ([Wallet]([url](https://web.budgetbakers.com)) by budget bakers). My model performed 15% better than the OSP. 



## Goal

The goal of this project is to:
- Demonstrate the effectiveness of fine-tuning open-source models on personal data.
- Create a system to track financial spending 
- Encourage non-data scientists to experiment with AI models.

## Features

- **Fine-tuned DistilBERT Model**: Classifies transactions into 20 categories based on transaction notes.
- **Privacy-Focused**: Processes data locally, ensuring no personal data is shared online.
- **Performance**: Outperforms a paid service provider by 15% in categorizing transactions.

**Performance test:** 
![Chi-square test](https://github.com/user-attachments/assets/9ef09552-5dc2-4b51-9eb1-03fc9db937ad)


## Project Structure

- **Model Training**: Notebooks,scripts, for training the DistilBERT model along with the saved model. Perhaps the most important. 
- **Dashboarding**: Processing data for further visualization. 
- **Data Extraction**: Scripts for extracting data from PDF bank statements. This might not for everyone. This was coded specifically for myself, but I included it in the git hub respository. 


## Data and Features

- Dataset: Approximately 300-400 rows of text data with corresponding labels for transaction categories.
- Combined Text: Merges transaction notes with amount information (e.g., "Customer Transfer Cr. INVESTMENT PROCEEDS: $678.64").
- Class Imbalance Handling: Techniques like oversampling used to address class imbalances.
- Training: Utilizes the Trainer API from Hugging Face Transformers for efficiency.
- Setup: Small model with 110M parameters trained on a GPU with 6GB VRAM (Can work with CPU if you have enough RAM).

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/prayag-purohit/Financial_tracker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Financial_tracker
   ```
3. Follow the instructions in the Jupyter notebooks within subdirectories to set up and use the model.

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Required Python libraries: Transformers, sklearn, torch, camelot, imblearn, subprocesses, os, pandas, numpy, Matplotlib

### Installation

1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Launch Jupyter Notebook and edit the notebooks to begin categorizing your transactions.

## Future Directions

- Experiment with text-generation models for comparison.
- Remove classification heads from pre-trained models for better personalization.
- Implement relational database structures instead of using CSVs.
- Data augmentation is very hard for transaction data with conventional methods. Suggestions are highly appreciated.

## Limitations

- **Small Dataset**: Limited to 300 rows due to the sensitive nature of bank transaction data.
- **Overfitting Risk**: High risk due to the small dataset size, mitigated by careful monitoring and regularization techniques.
- **Hardcoded paths**

## Contributions and Feedback

This project welcomes contributions and constructive criticism. If you are from a different background or have suggestions for improvement, feel free to contribute or provide feedback.

## Further Documentation

Detailed documentation and usage instructions can be found within the subdirectories in the Jupyter notebooks.
