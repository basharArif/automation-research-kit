# Dockerfile - Reproducible Automation Research Environment
# Build: docker build -t automation-research .
# Run: docker run -it -v $(pwd):/workspace automation-research

FROM python:3.10-slim-bullseye

LABEL maintainer="Automation Research" \
      description="Comprehensive automation research package with control theory, robotics, and ML"

# Set working directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    wget \
    curl \
    graphviz \
    libopencv-dev \
    python3-opencv \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Create non-root user
RUN useradd -m -s /bin/bash researcher && \
    mkdir -p /workspace && \
    chown -R researcher:researcher /workspace

USER researcher

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/workspace:$PYTHONPATH

# Expose Jupyter port (optional)
EXPOSE 8888

# Default command: bash shell
CMD ["/bin/bash"]

# Optional: Start Jupyter Lab
# CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]