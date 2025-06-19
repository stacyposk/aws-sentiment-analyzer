# Sentiment Analyzer on AWS
Analyze customer feedback at scale with real-time sentiment and entity detection using AWS services.

![AWS](https://img.shields.io/badge/Powered%20by-AWS-yellow?style=flat&logo=amazonaws)
![Comprehend](https://img.shields.io/badge/Service-Amazon%20Comprehend-orange)
![Quicksight](https://img.shields.io/badge/Visualization-QuickSight-blue)

---

## Project Overview
This project demonstrates an event-driven AI pipeline on AWS that:
- Accepts a batch of customer reviews in CSV format
- Automatically triggers analysis when the file is uploaded to Amazon S3
- Uses Amazon Comprehend to perform:
  - **Sentiment analysis**
  - **Entity detection**
- Stores processed results back into S3
- Visualizes insights using Amazon QuickSight

---

## Architecture

- **Amazon S3**: Uploads batch of 100 customer review CSV files
- **AWS Lambda**: Triggered by S3 `ObjectCreated` event
- **Amazon Comprehend**: Performs sentiment and entity detection on each review
- **S3**: Stores the results in a designated output folder
- **Amazon QuickSight**: Visualizes sentiment distribution and entity frequency
- Built fully on AWS Free Tier (Comprehend, Lambda, S3, QuickSight)

---

## How It Works

1. User uploads a CSV file containing 100 customer reviews to an S3 bucket.
2. S3 event triggers a Lambda function (Python), which:
   - Reads the CSV
   - Sends each review to Amazon Comprehend via Boto3
   - Extracts sentiment and entities
3. Lambda saves the analysis results (CSV) to another S3 bucket/folder.
4. Amazon QuickSight is configured to ingest the new result files from S3 for visualization
5. QuickSight dashboard with filters and comparison charts

---

## Key AWS Features Used

- **S3 Event Notification** to trigger computation
- **Lambda (Python)** with `boto3` to control Comprehend
- **Comprehend APIs:**
  - `DetectSentiment`
  - `DetectEntities`
- **QuickSight** dataset connecting from S3 output bucket using Manifest file

---

## Demo Screenshots

### 1. S3 File Upload
![S3 File Upload](screenshots/1_S3_File_Upload.png)
A CSV file containing customer reviews is uploaded to the `input/` folder in the S3 bucket, which triggers the analysis workflow.

### 2A. Lambda Function Diagram
![Lambda Function Diagram](screenshots/2A_Lambda_Function_Diagram.png)
The AWS Lambda function `trigger-comprehend-analysis` is automatically invoked by the S3 `ObjectCreated` event.

### 2B. CloudWatch Metrics
![CloudWatch Metrics](screenshots/2B_CloudWatch_Metrics.png)
CloudWatch metrics confirm successful Lambda execution, showing 100% success rate and low average duration.

### 3A. S3 Output Folder View
![S3 Output Folders](screenshots/3A_S3_Output_Folders.png)
After analysis, results are saved to the `output/` bucket, organized into separate folders by task (e.g., sentiment, entity, pii).

### 3B. Output File in Sentiment Folder
![S3 Output File](screenshots/3B_S3_Output_File.png)
Each processed file is saved with a unique folder name under `output/sentiment/`, containing the CSV result of sentiment scores.

### 4A. QuickSight Sentiment Dashboard
![QuickSight Sentiment Dashboard](screenshots/4A_QuickSight_Sentiment_Dashboard.png)
A QuickSight dashboard visualizes the sentiment breakdown (positive, negative, mixed) and confidence scores for each prediction.

### 4B. QuickSight Entity Dashboard
![QuickSight Entity Dashboard](screenshots/4B_QuickSight_Entity_Dashboard.png)
Entity analysis shows the top-mentioned brands and products from customer reviews, along with their sentiment distributions.

---

## Tech Stack

| Component | Service |
|----------|---------|
| Text Analysis | Amazon Comprehend |
| Event Trigger | Amazon S3 |
| Compute | AWS Lambda |
| Storage | Amazon S3 |
| Visualization | Amazon QuickSight |

---

## Possible Improvements

- Separate the PII detection process from sentiment and entity analysis to prevent false positives (e.g., dates or IDs misclassified as PII)
- Replace CSV parsing with streaming (e.g., using AWS Lambda + AWS Glue) to handle larger files more efficiently
- Add SNS or email notifications to alert users when analysis completes successfully

---

## 📄 License

MIT © Stacy Po
