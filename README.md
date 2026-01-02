# Multi-Language Voice Newsletter System (AWS)

The Multi-language Voice Newsletter System is a web application designed to create, manage, and send newsletters in multiple languages. It allows users to subscribe to newsletters based on their language preference and receive personalized content via email.

## Features
- Multi-language text-to-speech using Amazon Polly
- Email delivery using Amazon SES
- Serverless backend with AWS Lambda & API Gateway
- Subscriber management using DynamoDB
- Admin panel for broadcasting newsletters

## Tech Stack
- AWS Lambda, API Gateway, Polly, SES, DynamoDB, S3
- Python, HTML, CSS, JavaScript

## Architecture
![Architecture](architecture/aws-architecture.png)

## Setup (High-Level)
1. Create DynamoDB table: Subscribers
2. Configure Amazon SES and verify sender email
3. Create S3 bucket for audio files
4. Deploy Lambda functions
5. Update API Gateway URL in frontend

