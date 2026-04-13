import os
from PIL import Image

def resize_frames():
    target_dir = r"c:\Users\Youssef356\Documents\Mobile development\AR_ExplorerWebsite\frames\Videoframes"
    total_frames = 367
    
    if not os.path.exists(target_dir):
        print(f"Error: Directory {target_dir} not found.")
        return

    print(f"Starting resize of {total_frames} frames in {target_dir}...")
    
    for i in range(total_frames):
        num = str(i).zfill(5)
        filename = f"AR_EXPLORER_{num}.jpg"
        filepath = os.path.join(target_dir, filename)
        
        if os.path.exists(filepath):
            try:
                with Image.open(filepath) as img:
                    width, height = img.size
                    new_size = (width // 2, height // 2)
                    resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
                    resized_img.save(filepath, "JPEG", quality=85)
                
                if i % 50 == 0:
                    print(f"Processed {i}/{total_frames} frames...")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
        else:
            print(f"Warning: {filename} not found.")

    print("Resize complete!")

if __name__ == "__main__":
    resize_frames()
