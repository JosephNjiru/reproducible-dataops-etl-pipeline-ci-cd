# Basic Infrastructure-as-Code Example for AWS EC2
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "etl_server" {
  ami           = "ami-0c02fb55956c7d316" # Amazon Linux 2
  instance_type = "t2.micro"
  tags = {
    Name = "ZenithActiveETL"
  }
}
