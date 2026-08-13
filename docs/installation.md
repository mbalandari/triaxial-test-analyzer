# Installation Guide

This document explains how to install and run the Triaxial Test Analyzer application.

---

## 1. Requirements

### Python

You need **Python 3.10+** installed.

Check your version:

```bash
python --version
```

## 2.Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

Then install dependencies inside it.

## 3. Install Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

If you do not have a requirements file yet, use:

```bash
PySide6
matplotlib
numpy
pandas
python-docx
reportlab
```

Install manually:

```bash
pip install PySide6 matplotlib numpy pandas python-docx reportlab
```

## 4. Running the Application

Run the app from the project root, not inside the gui/ folder.

Correct command:

```bash
python -m gui.app
```

This ensures Python recognizes gui and src as packages.
