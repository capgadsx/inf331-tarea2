# INF331 - Tarea 2

Este aplicativo busca comparar el texto contenido en dos imagenes, utilizando los siguientes servicios de [AWS](https://aws.amazon.com/es/)

* [Rekognition](https://aws.amazon.com/es/rekognition/)
* [S3](https://aws.amazon.com/es/s3/)
* [IAM](https://aws.amazon.com/es/iam/)

## Dependencias

* [Python 3.0+](https://www.python.org/download/releases/3.0/)
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## Instalación de dependencias

```bash
pip3 install -r requirements.txt
```

## Utilizando el software

```bash
$ python app.py -h
usage: app.py [-h] -c CONTROL -t TEST -b BUCKET -i AWSID -k AWSKEY -co CONFIDENCE [-v]

    Compares the text of two images using AWS Rekognition

    The program needs AWS credentials of an IAM user with
    AmazonRekognitionFullAccess and AmazonS3FullAccess roles
    

optional arguments:
  -h, --help            show this help message and exit
  -c CONTROL, --control CONTROL
                        path of the control image
  -t TEST, --test TEST  path of the test image
  -b BUCKET, --bucket BUCKET
                        bucket to store the images for Rekognition
  -i AWSID, --awsid AWSID
                        AWS secret key id
  -k AWSKEY, --awskey AWSKEY
                        AWS secret access key
  -co CONFIDENCE, --confidence CONFIDENCE
                        confidence for detected words
  -v, --debug           enable debug logging

$ python app.py -c ~/Descargas/control_image.png -t ~/Descargas/test_image.png -b bucket-inf-331... -i AKIA... -k bTc... --confidence 97
12-Nov-20 02:53:13 - inf331-tarea3 - INFO - Started with args: Namespace(awsid='AKIA...', awskey='bTc...', bucket='bucket-inf-331...', confidence=97.0, control='/home/cponce/Descargas/control_image.png', debug=False, test='/home/cponce/Descargas/test_image.png')
12-Nov-20 02:53:13 - inf331-tarea3 - INFO - Creating S3 client, using bucket bucket-inf-331...
12-Nov-20 02:53:13 - inf331-tarea3 - INFO - Uploading control image: /home/cponce/Descargas/control_image.png
12-Nov-20 02:53:17 - inf331-tarea3 - INFO - Uploading test image: /home/cponce/Descargas/test_image.png
12-Nov-20 02:53:20 - inf331-tarea3 - INFO - Done uploading images
12-Nov-20 02:53:20 - inf331-tarea3 - INFO - Creating Rekognition client
12-Nov-20 02:53:20 - inf331-tarea3 - INFO - Detecting text from control image
12-Nov-20 02:53:22 - inf331-tarea3 - INFO - Detected words from control image: {'keep', 'Smiling', 'but', 'MONDAY', "IT'S", 'but keep'}
12-Nov-20 02:53:22 - inf331-tarea3 - INFO - Detecting text from test image
12-Nov-20 02:53:23 - inf331-tarea3 - INFO - Detected words from test image: {'keep', 'Smiling', 'but', 'MONDAY', "IT'S", 'but keep'}
12-Nov-20 02:53:23 - inf331-tarea3 - INFO - Final Result: TRUE
12-Nov-20 02:53:23 - inf331-tarea3 - INFO - Program done
```

## Contribuir al proyecto

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Licencia

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
