import os
import sys
import subprocess
import argparse
import time

print("Starting pipeline script...")

# Add the project root to the path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

try:
    from src.utils.paths import ensure_all_dirs
    print("Successfully imported from src.utils.paths")
except ImportError as e:
    print(f"Error importing: {e}")
    # Try a different approach
    try:
        sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
        from utils.paths import ensure_all_dirs
        print("Successfully imported from utils.paths")
    except ImportError as e:
        print(f"Still cannot import: {e}")

def run_command(command):
    """Run a system command and print output in real-time"""
    print(f"\n\n{'='*80}")
    print(f"Running: {command}")
    print(f"{'='*80}\n")
    
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        shell=True
    )
    
    # Print output in real-time
    for line in process.stdout:
        print(line, end='')
    
    process.wait()
    
    print(f"\n{'='*80}")
    print(f"Command completed with return code: {process.returncode}")
    print(f"{'='*80}\n")
    
    return process.returncode

def run_pipeline(mode='basic', skip_preprocessing=False, skip_training=False, launch_app=True):
    """Run the complete pipeline"""
    # Ensure all directories exist
    try:
        print("Calling ensure_all_dirs...")
        ensure_all_dirs()
        print("Directories ensured!")
    except Exception as e:
        print(f"Error ensuring directories: {e}")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Base directory: {base_dir}")
    
    # Function to properly quote file paths
    def quote_path(path):
        return f'"{path}"'
    
    # Step 1: Preprocessing
    if not skip_preprocessing:
        if mode == 'basic':
            print("Running basic data preprocessing...")
            preprocess_script = os.path.join(base_dir, 'src', 'preprocessing', 'preprocess_crop_data.py')
            run_command(f'python {quote_path(preprocess_script)}')
        else:
            print("Running combined data preprocessing...")
            preprocess_script = os.path.join(base_dir, 'src', 'preprocessing', 'preprocess_combined_data.py')
            run_command(f'python {quote_path(preprocess_script)}')
    
    # Step 2: Model Training
    if not skip_training:
        if mode == 'basic':
            print("Training basic crop prediction model...")
            training_script = os.path.join(base_dir, 'src', 'training', 'crop_prediction_model.py')
            run_command(f'python {quote_path(training_script)}')
        else:
            print("Training combined and extended crop prediction models...")
            training_script = os.path.join(base_dir, 'src', 'training', 'train_combined_model.py')
            run_command(f'python {quote_path(training_script)}')
    
    # Step 3: Launch Web App
    if launch_app:
        if mode == 'basic':
            print("Launching basic web application...")
            app_script = os.path.join(base_dir, 'webapp', 'app.py')
            run_command(f'streamlit run {quote_path(app_script)}')
        else:
            print("Launching enhanced web application...")
            app_script = os.path.join(base_dir, 'webapp', 'app_combined.py')
            run_command(f'streamlit run {quote_path(app_script)}')

if __name__ == "__main__":
    print("Script running in __main__")
    parser = argparse.ArgumentParser(description="Run the Crop Recommendation System pipeline")
    parser.add_argument(
        "--mode", 
        choices=["basic", "enhanced"], 
        default="basic",
        help="Run mode: 'basic' for the original dataset only, 'enhanced' for combined datasets"
    )
    parser.add_argument(
        "--skip-preprocessing", 
        action="store_true",
        help="Skip data preprocessing step"
    )
    parser.add_argument(
        "--skip-training", 
        action="store_true",
        help="Skip model training step"
    )
    parser.add_argument(
        "--no-app", 
        action="store_true",
        help="Don't launch the web application"
    )
    
    args = parser.parse_args()
    
    print(f"Starting pipeline in {args.mode} mode")
    run_pipeline(
        mode=args.mode,
        skip_preprocessing=args.skip_preprocessing,
        skip_training=args.skip_training,
        launch_app=not args.no_app
    ) 