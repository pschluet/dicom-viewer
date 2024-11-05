import os
import pydicom
import matplotlib.pyplot as plt
import argparse

def find_dicom_files_with_pixel_data(directory):
    dicom_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Read the DICOM file
                ds = pydicom.dcmread(file_path, stop_before_pixels=False)
                
                # Only add files that contain pixel data
                if hasattr(ds, 'PixelData'):
                    dicom_files.append(file_path)
            except Exception:
                # Ignore non-DICOM or unreadable files
                continue
    return dicom_files

def display_and_save_dicom_images(dicom_files, output_dir):
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
    
    for dicom_path in dicom_files:
        try:
            dicom_data = pydicom.dcmread(dicom_path)
            
            # Set up full-screen display
            fig = plt.figure(figsize=(16, 9))
            manager = plt.get_current_fig_manager()
            manager.full_screen_toggle()
            
            plt.imshow(dicom_data.pixel_array, cmap='gray')
            plt.title(f"X-ray Image: {os.path.basename(dicom_path)}")
            plt.axis('off')
            
            # Save as JPEG
            jpeg_filename = os.path.join(output_dir, f"{os.path.basename(dicom_path)}.jpeg")
            plt.savefig(jpeg_filename, format='jpeg', bbox_inches='tight', pad_inches=0)
            print(f"Saved image as {jpeg_filename}")
            
            # Display the image
            plt.show()
        except Exception as e:
            print(f"Could not display or save image from {dicom_path}. Error: {e}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Parse, display, and save all DICOM images as JPEGs from the specified directory.")
    parser.add_argument("base_directory", help="Path to the base directory containing DICOM files")
    parser.add_argument("--output_dir", default="output_images", help="Directory to save the JPEG images")

    args = parser.parse_args()

    # Find all DICOM files with pixel data in the specified base directory
    dicom_files = find_dicom_files_with_pixel_data(args.base_directory)

    if dicom_files:
        print(f"Found {len(dicom_files)} DICOM files with pixel data.")
        # Display and save all DICOM images found
        display_and_save_dicom_images(dicom_files, args.output_dir)
    else:
        print("No DICOM files with pixel data found.")

if __name__ == "__main__":
    main()
