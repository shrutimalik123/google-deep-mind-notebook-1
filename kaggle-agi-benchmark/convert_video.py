import imageio

def convert_webp_to_mp4(input_file, output_file):
    print(f"Reading {input_file}...")
    reader = imageio.get_reader(input_file)
    # Default to 10 fps if not found
    fps = reader.get_meta_data().get('fps', 10)
    
    print(f"Writing {output_file} at {fps} FPS...")
    writer = imageio.get_writer(output_file, fps=fps)
    
    for im in reader:
        writer.append_data(im)
        
    writer.close()
    print("Conversion complete!")

if __name__ == "__main__":
    convert_webp_to_mp4('eval_video.webp', 'eval_video.mp4')
