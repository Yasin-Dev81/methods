"""
- استفاده از فضای ابری ابرآروان با استفاده از پکیج بوتو3

- requirements: 1.7.3.django-storages
"""
# ex:
# 0
# create "./bucket.py" and write bellow code
import boto3
from django.conf import settings


class Bucket:
	"""CDN Bucket manager

	init method creates connection.

	NOTE:
		none of these methods are async. use public interface in tasks.py modules instead.
	"""

	def __init__(self):
		session = boto3.session.Session()
		self.conn = session.client(
			service_name=settings.AWS_SERVICE_NAME,
			aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
			aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
			endpoint_url=settings.AWS_S3_ENDPOINT_URL,
		)

    # باقی کلاس بستگی به پروژه داره
	def get_objects(self):
		result = self.conn.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
		if result['KeyCount']:
			return result['Contents']
		else:
			return None

	def delete_object(self, key):
		self.conn.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=key)
		return True

	def download_object(self, key):
		with open(settings.AWS_LOCAL_STORAGE + key, 'wb') as f:
			self.conn.download_fileobj(settings.AWS_STORAGE_BUCKET_NAME, key, f)


bucket = Bucket()

# 1
# create "./home/tasks.py" and write bellow code
from bucket import bucket
from celery import shared_task


# TODO: can be async?
def all_bucket_objects_task():
	result = bucket.get_objects()
	return result


@shared_task
def delete_object_task(key):
	bucket.delete_object(key)


@shared_task
def download_object_task(key):
	bucket.download_object(key)
