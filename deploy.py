import os

def run_pipeline():
    aws_region = os.environ.get('AWS_REGION')
    # Example usage of aws_region
    print(f"AWS Region: {aws_region}")

if __name__ == '__main__':
    run_pipeline()
