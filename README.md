# 🎨 Sketchify-App 

Sketchify is a simple Streamlit + OpenCV app that transforms your images into creative styles like pencil sketch, cartoon, grayscale, blur, and edge detection.

---

## 🚀 Features

- Upload any .jpg, .jpeg, or .png image
- Apply effects instantly:
  -- Original
  -- Pencil Sketch
  -- Cartoon
  -- Grayscale
  -- Edge Detection
  -- Blur
- Side-by-side comparison (Original vs. Processed)
- Download the processed image
- Simple and lightweight (uses only OpenCV)
- Fast processing

---

## 📂 Project Structure

```
Sketchify-App/
│── photo_sketch.py
│── Image1.png 
│── sketch_output.jpg 
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/Purvijain1234/Sketchify-App.git
cd Sketchify-App
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the script with:

```bash
python photo_sketch.py
```

- By default, the script processes `Image.png` and outputs image.
- To use your own image, replace `Image.png` with your file or edit the script to change the input path.

---

## 🖼️ Example

![Output](sketch_output.jpg)

---

## 📜 License

This project is open-source and available under the MIT License.
