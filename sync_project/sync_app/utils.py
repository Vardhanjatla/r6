import paramiko 

def synchronize_files(source_server, source_folder, destination_server, destination_folder):
    # Establish SSH/SFTP connections
    source_client = paramiko.SSHClient()
    source_client.load_system_host_keys()
    source_client.connect(source_server.address)

    destination_client = paramiko.SSHClient()
    destination_client.load_system_host_keys()
    destination_client.connect(destination_server.address)

    sftp_source = source_client.open_sftp()
    sftp_destination = destination_client.open_sftp()

    # Synchronize files
    for filename in sftp_source.listdir(source_folder.path):
        source_path = f"{source_folder.path}/{filename}"
        destination_path = f"{destination_folder.path}/{filename}"
        sftp_source.get(source_path, destination_path)
        sftp_destination.put(destination_path, destination_path)

    sftp_source.close()
    sftp_destination.close()
    source_client.close()
    destination_client.close()