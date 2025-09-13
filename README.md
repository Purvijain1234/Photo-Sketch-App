# 🖼️ Sketchify-App ✏️

Sketchify-App converts any photo into a **pencil sketch** using Python and OpenCV.  
It applies grayscale conversion, inversion, Gaussian blur, and blending to produce a realistic sketch effect.

---

## 🚀 Features

- Convert any photo into a pencil sketch
- Simple and lightweight (uses only OpenCV)
- Works with all image formats supported by OpenCV
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

- By default, the script processes `Image1.png` and outputs `sketch_output.jpg`.
- To use your own image, replace `Image1.png` with your file or edit the script to change the input path.

---

## 🛠️ How it Works

1. **Grayscale Conversion:** Converts the input image to grayscale.
2. **Inversion:** Inverts the grayscale image.
3. **Blurring:** Applies a Gaussian blur to the inverted image.
4. **Blending:** Blends the grayscale image with the blurred version to create a pencil-sketch effect.

All of this is handled in `photo_sketch.py`.

---

## 🖼️ Example

**Input:**

![Input](Image1.png)

**Output (Sketch):**

![Output](sketch_output.jpg)

---

## 📜 License

This project is open-source and available under the MIT License.
