import weaviate
import atexit
from weaviate.config import AdditionalConfig, Timeout

# Module-level variable to hold the singleton client
_client = None

def get_weaviate_client(cluster_endpoint=None, cluster_api_key=None, use_local=False):
	print("Connecting to Weaviate...")
	global _client
	if _client is None:
		if use_local:
			_client = weaviate.connect_to_local(
				auth_credentials=weaviate.auth.AuthApiKey(cluster_api_key),
				skip_init_checks=True,
				additional_config=AdditionalConfig(
					timeout=Timeout(init=90, query=900, insert=900)
				)
			)
		else:
			_client = weaviate.connect_to_wcs(
				cluster_url=cluster_endpoint,
				auth_credentials=weaviate.auth.AuthApiKey(cluster_api_key),
				skip_init_checks=True,
				additional_config=AdditionalConfig(
					timeout=Timeout(init=90, query=900, insert=900)
				)
			)
		# Register a cleanup function to close the client when the process exits
		atexit.register(close_weaviate_client)
	return _client

def close_weaviate_client():
	print("Disconnecting from Weaviate...")
	global _client
	if _client:
		_client.close()
		_client = None

# Weaviate Server & Client status and version
def status(client):
	print("Getting Weaviate status...")
	try:
		ready = client.is_ready()
		server_version = client.get_meta()["version"]
		client_version = weaviate.__version__
		return ready, server_version, client_version
	except Exception as e:
		print(f"Error: {e}")
		return False, "N/A", "N/A"
