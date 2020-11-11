import argparse

def setup_args():
    parser = argparse.ArgumentParser(description='Compares the text of two images using AWS Rekognition')
    parser.add_argument('-c', '--control', type=str, help='path of the control image', required=True)
    parser.add_argument('-t', '--test', type=str, help='path of the test image', required=True)
    parser.add_argument('-b', '--bucket', type=str, help='bucket to store the images for Rekognition', required=True)
    parser.add_argument('-i', '--awsid', type=str, help='AWS secret key id', required=True)
    parser.add_argument('-k', '--awskey', type=str, help='AWS secret access key', required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = setup_args()
