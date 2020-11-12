import boto3
import logging
import argparse

global log

def setup_log(args):
    global log
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    log = logging.getLogger('inf331-tarea3')
    if args.debug:
        log.setLevel(logging.DEBUG)
    else:
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
    parser.add_argument('-v', '--debug', action='store_true', help='enable debug logging',)
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

def search_text(args):
    global log
    log.info('Creating Rekognition client')
    client = boto3.client(
        'rekognition',
        aws_access_key_id=args.awsid,
        aws_secret_access_key=args.awskey
    )
    log.info('Detecting text from control image')
    s3obj = {'S3Object': {'Bucket': args.bucket, 'Name': 'control_image'}}
    control_res = client.detect_text(Image=s3obj)
    log.debug('Rekognition response: {}'.format(control_res))
    control_set = set()
    for detection in control_res['TextDetections']:
        control_set.add(detection['DetectedText'])
    log.info('Detected words from control image: {}'.format(control_set))
    log.info('Detecting text from test image')
    s3obj = {'S3Object': {'Bucket': args.bucket, 'Name': 'test_image'}}
    test_res = client.detect_text(Image=s3obj)
    log.debug('Rekognition response: {}'.format(test_res))
    test_set = set()
    for detection in test_res['TextDetections']:
        test_set.add(detection['DetectedText'])
    log.info('Detected words from test image: {}'.format(test_set))
    return control_set, test_set

if __name__ == "__main__":
    global log
    args = setup_args()
    setup_log(args)
    log.info('Started with args: {}'.format(args))
    try:
        upload_images(args)
        control, test = search_text(args)
        if control == test:
            log.info('Final Result: TRUE')
        else:
            log.info('Final Result: FALSE')
    except Exception as excep:
        log.error('EXCEPTION: {}'.format(excep))
    log.info('Program done')
