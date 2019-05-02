#!/bin/bash
aws ec2 describe-images --owners 309956199498 --query 'Images[*].[CreationDate,Name,ImageId]' --filters "Name=name,Values=RHEL-6.8_HVM_GA*Access*" --region us-east-1 --output table | sort -r | awk 'NR==2{print $6;exit}' > RHELlatest.log
aws ec2 describe-images --owners 309956199498 --query 'Images[*].[CreationDate,Name,ImageId]' --filters "Name=name,Values=RHEL-6.9*HVM_GA*Access*" --region us-east-1 --output table | sort -r | awk 'NR==3{print $6;exit}' >> RHELlatest.log
aws ec2 describe-images --owners 309956199498 --query 'Images[*].[CreationDate,Name,ImageId]' --filters "Name=name,Values=RHEL-6.10_HVM_GA*Access*" --region us-east-1 --output table | sort -r | awk 'NR==2{print $6;exit}' >> RHELlatest.log 
aws ec2 describe-images --owners 309956199498 --query 'Images[*].[CreationDate,Name,ImageId]' --filters "Name=name,Values=RHEL-7.4_HVM_GA*Access*" --region us-east-1 --output table | sort -r | awk 'NR==2{print $6;exit}' >> RHELlatest.log
aws ec2 describe-images --owners 309956199498 --query 'Images[*].[CreationDate,Name,ImageId]' --filters "Name=name,Values=RHEL-7.5_HVM_GA*Access*" --region us-east-1 --output table | sort -r | awk 'NR==2{print $6;exit}' >> RHELlatest.log
aws ec2 describe-images --owners 309956199498 --query 'Images[*].[CreationDate,Name,ImageId]' --filters "Name=name,Values=RHEL-7.6_HVM_GA*Access*" --region us-east-1 --output table | sort -r | awk 'NR==2{print $6;exit}' >> RHELlatest.log

if [[ -f previousamilist/default/RHELlatest.log ]]; then
	diff RHELlatest.log previousamilist/default/RHELlatest.log
    if [[ $?==0 ]]; then
    echo "No updates in ami ids"
    else echo "TBD"
    fi
fi
