#!/bin/bash
aws ec2 describe-images --owners 309956199498 --query 'Images[*].[CreationDate,Name,ImageId]' --filters "Name=name,Values=RHEL-7.?*GA*Access*" --region us-east-1 --output table | sort -r > RHEL7latest.log
