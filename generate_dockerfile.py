import argparse
import os

# --- TEMPLATES ---

# This is the final, approved Dockerfile text from Role C
node_template = """
# Use lightweight Node.js image
FROM node:18-alpine

# Set working directory inside container
WORKDIR /app

# Copy dependency files first
COPY package*.json ./

# Install only production dependencies
RUN npm install --production

# Copy the rest of the app files
COPY . .

# Expose app port
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
"""

# This is a placeholder for when the team adds a Java app
java_template = """
# Dockerfile for Java (Spring Boot)
FROM openjdk:17-jdk-slim
WORKDIR /app
ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
"""
# --- END TEMPLATES ---


def generate_dockerfile(app_type):
    """
    Generates a Dockerfile based on the selected application type.
    """
    content = ""
    if app_type == 'node':
        content = node_template
    elif app_type == 'java':
        content = java_template
    else:
        # This case should be handled by argparse 'choices'
        print(f"Error: Unsupported app type '{app_type}'.")
        return

    try:
        # Write the content to a file named 'Dockerfile'
        # It will create/overwrite this file in the directory where you run the script.
        with open("Dockerfile", "w") as f:
            f.write(content.strip()) # .strip() removes leading/trailing whitespace
        
        print(f"Success! 'Dockerfile' for '{app_type}' generated in {os.getcwd()}")

    except IOError as e:
        print(f"Error writing to file: {e}")


def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="AI-Powered DevOps: Dockerfile Generator"
    )
    
    # Add the '--type' argument
    # 'required=True' means the script won't run without it.
    parser.add_argument(
        "-t", "--type",
        type=str,
        required=True,
        choices=['node', 'java'], # Restricts input to only these values
        help="The application type (e.g., 'node' or 'java')"
    )

    args = parser.parse_args()
    
    # Call the generate function with the user's chosen type
    generate_dockerfile(args.type)


if __name__ == "__main__":
    main()
