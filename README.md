
# Automatic Evaluation of Handwritten Answersheets

Welcome to the **Automatic Evaluation of Handwritten Answer Sheets** project! This project aims to streamline and enhance the grading process by using artificial intelligence to evaluate handwritten responses automatically.

Manual grading is time-consuming and prone to errors. Our system employs machine learning to digitize, understand, and grade handwritten answers accurately and consistently.

This project aims to make grading faster, fairer, and more reliable, benefiting educators and students alike. We look forward to your contributions and feedback!
## Basic Overview

For the given problem statement, following were the steps taken by us:

1. Verified that the answer sheets are correctly oriented to ensure accurate processing.
2. Preprocessed the images to enhance quality and readability for analysis.
3. Extracted the right-most column from each sheet, where students marked their true/false answers.
4. Divided the extracted column into 10 separate cells, each corresponding to one of the 10 questions on the sheet.
**Example:**
![App Screenshot](https://raw.githubusercontent.com/deepak5512/Evaluation-of-Handwritten-Answer-Sheets/main/Archive/False/1%20(2).png?token=GHSAT0AAAAAACORO6MD33VGGFZSOMV3UNIMZT2ZNEQ)

![App Screenshot](https://raw.githubusercontent.com/deepak5512/Evaluation-of-Handwritten-Answer-Sheets/main/Archive/True/1%20(1).png?token=GHSAT0AAAAAACORO6MDSKSOHHYUOOLV2PL2ZT2ZNYA)

5. Trained and applied two different models: CNN (Convolutional Neural Network) and ViT (Vision Transformer), to recognize the written answers as True/False/Empty and evaluate the answers in each cell.
6. Compared the accuracy of the two models and selected ViT as the most accurate model for final evaluation.
## How to use our model?

For using CNN model,

1. Download the main_cnn.ipynb file and best_model_cnn.keras from best_model folder.
2. Write the path of images you want to evaluate in the variable named *directory* in the file.
3. Write the path of the model downloaded in the variable *model_path* in the file.
4. Write the correct answers in the variable *correct_answers* in the file.
5. Run the code file.
\
For using ViT model,

1. Download the main_vit.ipynb file and best_model_vit.pth from best model folder.
2. Write the path of images you want to evaluate in the variable named *directory* in the file.
3. Write the path of the model downloaded in the variable *model_save_path* in the file.
4. Write the correct answers in the variable *correct_answers* in the file.
5. Run the code file.
## Problems which might occur

1. Switch to Jupyter notebook if program gives error on vs code or other ide.
2. Check Model size, should be around 330MB for ViT and 26MB for CNN, in case of any errors while loading the model.
3. Ensure python 3.10 or above.
4. Don't download the complete GitHub repo as a zip file as it doesn't download the ViT model completely. Download the ViT model from the best model folder seperately.
## 🚀 Contributors

- Deepak Bhatter [@DeepakBhatter](https://www.linkedin.com/in/deepak-bhatter5512?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BoCYT3PQmTJKYeWeOME6%2BdA%3D%3D)
- Tushar Bhatt [@TusharBhatt](https://www.linkedin.com/in/tushar-bhatt-6031a5253?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BzitutbMqTRShyjk8F6UWAA%3D%3D)
- Prajjwal Dixit [@PrajjwalDixit](https://www.linkedin.com/in/prajjwal-dixit-713592289?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BeFX0MtOKRI63FgKQtPUx2Q%3D%3D)