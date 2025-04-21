import os
import sys
import subprocess
import time
import webbrowser
from concurrent.futures import ThreadPoolExecutor

def run_streamlit_app(app_path, port):
    """Run a Streamlit app on the specified port"""
    command = [
        sys.executable, "-m", "streamlit", "run", 
        app_path, 
        "--server.port", str(port)
    ]
    
    # Print info about the app being started
    app_name = os.path.basename(app_path).replace('.py', '')
    print(f"Starting {app_name} on http://localhost:{port}")
    
    # Run the process and redirect output
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Return the process object
    return process

def main():
    # Define the apps and their ports
    apps = [
        {"name": "Field Analyzer", "path": "src/webapp/app.py", "port": 8501},
        {"name": "Basic Crop Recommender", "path": "src/webapp/crop_recommendation_app.py", "port": 8502},
        {"name": "Advanced Crop Recommender", "path": "src/webapp/combined_model_app.py", "port": 8503}
    ]
    
    print("==========================================")
    print("   Starting All Smart Farming Apps")
    print("==========================================")
    
    # Start all apps in parallel
    processes = []
    with ThreadPoolExecutor(max_workers=len(apps)) as executor:
        for app in apps:
            # Start the app
            process = run_streamlit_app(app["path"], app["port"])
            processes.append({"app": app, "process": process})
    
    # Wait a moment for the apps to start
    time.sleep(3)
    
    # Open the browsers
    for app in apps:
        url = f"http://localhost:{app['port']}"
        print(f"Opening {app['name']} at {url}")
        webbrowser.open(url)
    
    print("\nAll apps are running. Press Ctrl+C to stop all apps.")
    
    try:
        # Monitor the processes
        while True:
            time.sleep(1)
            
            # Check if any process has terminated
            for proc_info in processes:
                if proc_info["process"].poll() is not None:
                    app = proc_info["app"]
                    print(f"WARNING: {app['name']} on port {app['port']} has terminated.")
                    
                    # Check for errors
                    stderr = proc_info["process"].stderr.read()
                    if stderr:
                        print(f"Error from {app['name']}: {stderr}")
                    
                    # Remove from monitoring
                    processes.remove(proc_info)
            
            # If all processes have terminated, exit
            if not processes:
                print("All apps have terminated. Exiting.")
                break
                
    except KeyboardInterrupt:
        print("\nStopping all apps...")
        
        # Terminate all processes
        for proc_info in processes:
            proc_info["process"].terminate()
        
        print("All apps stopped.")

if __name__ == "__main__":
    main() 