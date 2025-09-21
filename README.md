# Master's Thesis Project on Geo-AI-ML

## Project Overview

This repository contains the code, models, and documentation for my master's thesis project on how Artificial Intelligence (AI) and Machine Learning (ML) can assist in analyzing geographical locations. The project utilizes YOLOv3 for object detection and classification, focusing on:
- Parking detection
- Housing detection
- Classification of residential vs. non-residential areas

## Objectives

- Apply YOLOv3 to satellite and aerial images to detect parking lots and housing structures.
- Classify areas as residential or non-residential based on detected objects.
- Analyze the spatial distribution of these features.

## Repository Structure

```
data/               # Datasets and data samples
notebooks/          # Jupyter notebooks for experiments and analysis
src/                # Source code for training, inference, and utilities
models/             # Saved YOLOv3 weights and models
results/            # Output results, visualizations, and evaluation metrics
docs/               # Additional documentation and thesis write-ups
```

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bhuvi0001/masters-thesis-project-on-geo-ai-ml.git
   cd masters-thesis-project-on-geo-ai-ml
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download YOLOv3 weights and datasets:**
   - Place your weights in `models/`
   - Place datasets in `data/`
   - Instructions for downloading pre-trained YOLOv3 weights: [YOLOv3 Website](https://pjreddie.com/darknet/yolo/)

4. **Run detection/classification:**
   - Use scripts in `src/` or notebooks in `notebooks/` for object detection and classification tasks.

## Results

Results and visualizations will be placed in the `results/` folder.

## Contributing

Pull requests and suggestions are welcome!

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## Contact

For questions, please reach out via [GitHub Issues](https://github.com/bhuvi0001/masters-thesis-project-on-geo-ai-ml/issues).
