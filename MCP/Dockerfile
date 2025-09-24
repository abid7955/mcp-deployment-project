# FROM python:3.13-slim

# # Set working directory inside the container
# WORKDIR /app

# # Install Python dependencies
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# EXPOSE 3000

# # Copy the rest of your code
# COPY . .



# # Run your main MCP server
# CMD ["python", "Ems.py"]



# FROM python:3.12-slim-bullseye

# WORKDIR /app

# COPY Ems1.py .
# COPY rr.txt .

# RUN pip install -r rr.txt

# CMD ["python", "Ems1.py"]



# FROM python:3.12-slim-bullseye   
# WORKDIR /app                    
# COPY my_file.txt .             
# CMD ["cat", "my_file.txt"]     


FROM python:3.12-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY binance_mcp.py .

EXPOSE 8000

CMD ["python", "binance_mcp.py"]
