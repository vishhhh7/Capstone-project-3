# Multi-Tier Web App Deployment on AWS

## Overview

This project demonstrates a Multi-Tier Web Application Architecture on AWS by separating the application into three layers:

- Frontend Tier
- Backend Tier
- Database Tier

The architecture improves scalability, security, and maintainability by isolating each layer.

---

## Architecture

Users access the application through an Application Load Balancer.

Request Flow:

Users → Application Load Balancer → Frontend EC2 → Backend EC2 → Amazon RDS

---

## AWS Services Used

- Amazon EC2
- Amazon RDS (MySQL)
- Application Load Balancer
- Security Groups

---

## Project Components

### Frontend Tier

- Hosted on Amazon EC2
- Apache Web Server
- HTML/CSS User Interface

### Backend Tier

- Hosted on Amazon EC2
- Python Flask API
- Processes application requests

### Database Tier

- Amazon RDS MySQL
- Stores application data

---

## Features

- Multi-Tier Architecture
- Load Balancing
- Secure Communication Between Tiers
- Database Integration
- Scalable Design

---
