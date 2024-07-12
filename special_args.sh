Regions=$@
if [ $# -gt 0 ];then
    for regions in $Regions
    do
    aws ec2 describe-vpcs --region $regions | jq ".Vpcs[].VpcId" -r 
    echo "==================================================="
    done
else
    echo "invalid code"
fi