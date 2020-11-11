import boto3
import logging
import argparse

global log

def setup_log():
    global log
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    log = logging.getLogger('inf331-tarea3')
    log.setLevel(logging.INFO)

def setup_args():
    description_str = """
    Compares the text of two images using AWS Rekognition\n\n
    The program needs AWS credentials of an IAM user with
    AmazonRekognitionFullAccess and AmazonS3FullAccess roles
    """
    parser = argparse.ArgumentParser(description=description_str, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-c', '--control', type=str, help='path of the control image', required=True)
    parser.add_argument('-t', '--test', type=str, help='path of the test image', required=True)
    parser.add_argument('-b', '--bucket', type=str, help='bucket to store the images for Rekognition', required=True)
    parser.add_argument('-i', '--awsid', type=str, help='AWS secret key id', required=True)
    parser.add_argument('-k', '--awskey', type=str, help='AWS secret access key', required=True)
    return parser.parse_args()

def upload_images(args):
    global log
    log.info('Creating S3 client, using bucket {}'.format(args.bucket))
    client = boto3.client(
        's3',
        aws_access_key_id=args.awsid,
        aws_secret_access_key=args.awskey
    )
    log.info('Uploading control image: {}'.format(args.control))
    with open(args.control, 'rb') as fp:
        client.upload_fileobj(fp, args.bucket, 'control_image')
    log.info('Uploading test image: {}'.format(args.control))
    with open(args.test, 'rb') as fp:
        client.upload_fileobj(fp, args.bucket, 'test_image')
    log.info('Done uploading images')


if __name__ == "__main__":
    global log
    args = setup_args()
    setup_log()
    log.info('Started with args: {}'.format(args))
    try:
        upload_images(args)
    except Exception as excep:
        log.error('EXCEPTION: {}'.format(excep))
    log.info('Program done')
