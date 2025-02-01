#!/bin/bash
module load "jaspy/3.11"
source /home/users/mendrika/SSA/bin/activate

# Define the root folder
TARGET_DIR="/gws/nopw/j04/swift/rt_cores/2025/"

# Find the most recently modified file in the directory and subdirectories
LATEST_FILE=$(find "$TARGET_DIR" -type f -exec stat --format="%Y %n" {} \; | sort -nr | head -n 1 | cut -d ' ' -f2-)

# Run the Python script on the latest file
if [[ -n "$LATEST_FILE" ]]; then
    git pull
    python3 /home/users/mendrika/SSA/Zambia/codes/web/code/plot_observation.py "$LATEST_FILE"
    git add .
    git commit -m "Observations updated"
    git push
else
    echo "No files found in $TARGET_DIR"
fi
