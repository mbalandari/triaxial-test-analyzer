# Usage Guide

This guide explains how to use the Triaxial Test Analyzer application.

---

## 1. Launch the Application

Run:

```bash
python -m gui.app
```

## 2. Load Triaxial Test Files

Go to:

```bash
File → Load Files
```

Supported formats:

- .csv
- .xlsx

You may load multiple files at once.

## 3. Run Analysis

Go to:

```
Analyze → Run Analysis
```

The application will:

- Compute peak stress & strain
- Compute σ₁ and σ₃
- Generate Mohr circles
- Fit Mohr–Coulomb envelope
- Display tangent points
- Update specimen information panel
- Show the Mohr plot in the GUI

## 4. Export Reports

Go to:

```bash
Export → Export Report
```

Supported formats:

- .txt
- .pdf
- .docx

PDF and DOCX include the Mohr plot.

## 5. Example Data

Example files are located in:

```bash
examples/
```

Use these to test the full pipeline.

## 6. GUI Overview

Left panel:

- Loaded file list

Right top:

- Specimen information

Right bottom:

- Mohr plot (round circles, envelope, tangent points)
