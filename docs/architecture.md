# Architecture Overview

This document explains the internal structure of the Triaxial Test Analyzer.

---

## 1. High-Level Architecture

GUI (PySide6)

↓

Backend (Python modules)

↓

Plotting (Matplotlib)

↓

Reports (TXT, PDF, DOCX)

---

## 2. Backend Modules

### loader.py

Loads CSV/XLSX files and returns `Specimen` objects.

### models.py

Defines:

- `Specimen`
- `AnalysisResult`

### analysis.py

Computes:

- Peak stress
- Peak strain
- σ₁ and σ₃
- Mohr circle centers and radii

### mohr_coulomb.py

Fits Mohr–Coulomb envelope using linear regression.

### plotting.py

Generates:

- Mohr circles
- Tangent points
- Envelope line
- Round aspect ratio

### reports/

Generates:

- TXT
- PDF (ReportLab)
- DOCX (python-docx)

---

## 3. GUI Modules

### app.py

Entry point.

### main_window.py

Main window layout + menu actions.

### widgets/

- FileListWidget
- SpecimenView
- PlotView (Matplotlib canvas)

---

## 4. Data Flow

Load files → Specimen objects

Run analysis → AnalysisResult objects

Prepare Mohr data → centers & radii

Fit envelope → slope & cohesion

Plot → GUI + reports

Export → TXT/PDF/DOCX

---

## 5. Design Principles

- Modular
- Clean separation of GUI and backend
- Engineering-grade plotting
- Professional report generation

---
