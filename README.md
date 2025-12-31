# Multi-Language Voice Newsletter System (AWS)

A serverless application that allows users to subscribe to newsletters and receive
multi-language voice-based audio content via email.

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

> Sensitive configuration values are intentionally hidden.
