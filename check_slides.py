import fitz  # PyMuPDF
import os

def render_slides(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Higher resolution
        output_path = os.path.join(output_dir, f"slide_{i+1}.png")
        pix.save(output_path)
        print(f"Slide {i+1} saved to {output_path}")
    doc.close()

if __name__ == "__main__":
    render_slides("prezentace.pdf", "slides_check")
