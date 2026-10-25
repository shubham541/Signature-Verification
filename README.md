# Signature-Verification

An offline handwritten signature verification system. Before the algorithm runs, a scanned image is pre-processed to isolate the signature and remove noise. The project proposes a feature vector for an offline handwritten signature using Histogram of Oriented Gradients (HOG) as the feature extractor, which is then passed to an Artificial Neural Network for recognition.

## Results

An experiment on a local database of more than 48 genuine and 48 forged signature samples from 4 individuals gave an accuracy of 96.8%, with a False Accept Rate (FAR) of 3% and a False Reject Rate (FRR) of 3.35%.

## Repository contents

```
Pre-Processing/preprocessing.py            Image pre-processing script (Pillow, OpenCV, NumPy, Matplotlib)
Colab Notebooks-Signature Verf/fyp.ipynb   Google Colab notebook
SignatureVerf_Report_Pdf.pdf               Project report
SignatureVerf_Poster_pdf.pdf               Project poster
```

## Running

- The pre-processing script is Python and needs Pillow, OpenCV (`opencv-python`), NumPy and Matplotlib. It loads a signature image named `sign.jpg` from the working directory (not included in the repo). It uses IPython's `display`, so it is meant to run in a notebook-like environment.
- The notebook (`fyp.ipynb`) was written for Google Colab and mounts Google Drive; see the report for the full methodology.
