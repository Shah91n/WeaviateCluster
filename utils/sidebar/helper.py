import streamlit as st

# Update the side bar labels on the fly
def update_side_bar_labels():
	print("Updating side bar labels...")
	if not st.session_state.get("client_ready"):
		st.warning("Please Establish a connection to Weaviate on the side bar")
	else:
		st.sidebar.info("Connection Status: Ready")
		st.sidebar.info(f"Current Connected Endpoint: {st.session_state.cluster_endpoint}")
		st.sidebar.info(f"Client Version: {st.session_state.client_version}")
		st.sidebar.info(f"Server Version: {st.session_state.server_version}")
		print("cluster_endpoint in session state:", st.session_state.get('cluster_endpoint'))
		print("Server Version in session state:", st.session_state.get('server_version'))

# Clear the session state
def clear_session_state():
	print("Session state cleared!")
	for key in st.session_state.keys():
		del st.session_state[key]
