# Multi-Source Crypto Tracker & Processor

An end-to-end Data Engineering pipeline designed to ingest, process, and serve cryptocurrency market data. This project demonstrates professional software engineering practices applied to data workflows, including **OOP**, **Dockerization**, and **REST API** development.

## Overview

The pipeline automates the extraction of real-time cryptocurrency data from external APIs, performs data cleaning and transformation using **Pandas**, stores the results in optimized formats (**CSV** & **Partitioned Parquet**), and serves the processed data through a high-performance **FastAPI** backend.

## Tech Stack

- **Language:** Python 3.10+
- **Data Processing:** Pandas, PyArrow (for Parquet)
- **API Framework:** FastAPI
- **Containerization:** Docker, Docker-Compose
- **Environment Management:** Python-dotenv
- **Monitoring:** Custom Logging & Decorators

## Architecture & Features

### 1. Data Ingestion (OOP Approach)
- Built with an **Abstract Base Class (ABC)** to ensure scalability and maintainability.
- Supports multiple sources (currently implemented for CoinGecko API).
- Includes robust error handling and request timeouts to ensure pipeline stability.

### 2. Transformation & Storage
- **Data Cleaning:** Ensures correct data types.
- **Optimized Storage:** Saves data in both CSV for easy preview and **Parquet with Partitioning** (`partition_cols=['symbol']`) for high-performance analytical queries.
- **Type Hinting:** Fully implemented type hints for better code readability and static analysis.

### 3. Monitoring & Metadata
- **Custom Decorators:** Implemented `@monitor_execution` to track function duration and execution status.
- **Logging:** Comprehensive logging system to monitor the pipeline health and troubleshoot issues in production-like environments.

### 4. Containerization (Docker)
- Fully containerized using a multi-stage-like Dockerfile.
- **Docker Volumes:** Integrated for real-time development and data persistence.
- **Environment Configuration:** Managed via `.env` files for security and portability.

---

## Project Structure

```text
├── data/               # Processed CSV and Partitioned Parquet files
├── src/
│   ├── ingestors.py    # Data ingestion logic (OOP)
│   ├── processors.py   # Transformation logic (Pandas)
│   ├── decorators.py   # Performance monitoring decorators
│   ├── main.py         # Pipeline orchestrator
│   └── api.py          # FastAPI server
├── Dockerfile          # Container definition
├── docker-compose.yml  # Multi-container orchestration
├── requirements.txt    # Dependency list
└── .env                # Environment variables (API URLs, Ports)
```

## Getting Started

### Prerequisites
- Docker & Docker Compose installed.

### Installation & Execution
1. Clone the repository:
   ```bash
   git clone https://github.com/BetulBNY/multi-source-crypto-tracker-and-processor.git
   cd multi-source-crypto-tracker-and-processor
   ```

2. Run the entire stack (Pipeline + API):
   ```bash
   docker-compose up --build
   ```

3. Access the API:
   - **Data Endpoint:** `http://localhost:8000/cryptos`
   - **Data Endpoint:** `http://localhost:8000/cryptos/expensive`
   - **Swagger UI (Docs):** `http://localhost:8000/docs`

---

### Learning Outcomes
This project was built to master:
- Designing scalable data ingestion models.
- Handling large datasets with efficient file formats (Parquet).
- Deploying microservices using Docker.
- Adhering to professional Python standards (PEP8, Typing, Logging).

---