# Sentiment Analyzer on AWS

Analyze customer review CSV files with real-time sentiment and entity detection using Amazon Comprehend.

![AWS](https://img.shields.io/badge/Powered%20by-AWS-yellow?style=flat&logo=amazonaws)
![Comprehend](https://img.shields.io/badge/Service-Amazon%20Comprehend-orange)
![Quicksight](https://img.shields.io/badge/Visualization-QuickSight-blue)

---

## Architecture

- **Amazon S3**: Uploads batch of 100 customer review CSV files
- **AWS Lambda**: Triggered by S3 `ObjectCreated` event
- **Amazon Comprehend**: Performs sentiment and entity detection on each review
- **S3**: Stores the results in a designated output folder
- **Amazon QuickSight**: Visualizes sentiment distribution and entity frequency

---

## 🚀 How It Works

1. Upload a CSV file to `s3://input-bucket/reviews.csv`
2. An S3 event triggers a Lambda function written in Python
3. Lambda reads the CSV, calls Amazon Comprehend for analysis
4. Processed results are saved to `s3://output-bucket/results/`
5. QuickSight dashboard to connect to S3 folder and visualize the new data

---

## 📸 Demo Screenshots

> _Coming soon — Screenshots will be added to show:_
- S3 file upload
- Lambda execution log
- Output results in S3
- QuickSight dashboard

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

- Add SNS or SES notifications upon analysis completion
- Use Step Functions to manage error handling and retries
- Add support for multiple languages (via Comprehend's language detection)
- Export results to DynamoDB or Athena for advanced querying

---

## 📄 License

MIT © Stacy Po
