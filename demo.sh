#!/bin/bash
Set -e
echo "You have passed $# Arguments"
#This Scrip Will Get All The VPC ID Information From The Requested Region.
if [ $# -gt 0 ]
aws ec2 describe-vpcs --region $1|jq ".Vpcs[].VpcId"-r
echo "======================================================="
aws ec2 describe-vpcs --region $2|jq ".Vpcs[].VpcId"-r
echo "======================================================="
else
echo "You have not given any arguments. You need to pass atleast two positional Arguments"
fi
