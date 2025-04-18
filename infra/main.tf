provider "aws"{
    region = "us-east-1"
}

module "s3_raw"{
    source = "./modules/s3"
    layer = "raw"
    bucket_name = "${var.project_name}-raw"
}

module "s3_processed"{
    source = "./modules/s3"
    layer = "processed"
    bucket_name = "${var.project_name}-processed"
}