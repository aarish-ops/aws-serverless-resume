# AWS Serverless Resume Website with Live Visitor Counter

A cloud-based personal resume website built using AWS serverless
architecture. The project uses Amazon S3, CloudFront, API Gateway,
AWS Lambda, DynamoDB, and IAM to deliver a scalable website with
a live visitor counter.

## Project Overview

This project demonstrates the deployment of a static web application
on AWS and its integration with a serverless backend.

The visitor counter follows this architecture:

User
  ↓
CloudFront
  ↓
S3
  ↓
JavaScript
  ↓
API Gateway
  ↓
AWS Lambda
  ↓
DynamoDB
