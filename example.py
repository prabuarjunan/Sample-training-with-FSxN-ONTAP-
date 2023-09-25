# SSH into your SageMaker instance
ssh -i "your-key.pem" ec2-user@your-sagemaker-instance-ip

# Create a mount point
sudo mkdir /fsx
sudo mount -t nfs svm-dns-name:/volume-junction-path /fsx

# Mount the FSx volume
sudo mount -t nfs IP_address:/vol1 /fsx

# Define the FSx path where your data is mounted
fsx_path = '/mnt/fsx'

# Load your data using pandas # data is the CSV
def load_data():
    fsx_data_path = os.path.join(fsx_path, 'your-data-directory')
    data = pd.read_csv(os.path.join(fsx_data_path, 'data.csv'))
    return data
