#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Update system packages
sudo apt-get update
sudo apt-get upgrade -y

# Install Python and pip if not already installed
sudo apt-get install -y python3 python3-pip

# Navigate to the project directory
cd /path/to/CryptoSocialSage

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Set environment variables (if needed)
# export API_KEY=your_api_key_here

# Run the Streamlit app
nohup streamlit run streamlit_app.py --server.port 8501 &

echo "CryptoSocialSage Streamlit app is now running on port 8501"