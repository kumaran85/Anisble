#!/bin/python
from boto.ec2 import EC2Connection
conne = EC2Connection(profile_name='dev_prod')
conne.start_instances(instance_ids=['i-08cf866ac2e6cf748'])
