from argparse import ArgumentParser
from boto.ec2 import connect_to_region
import logging

logging.basicConfig(filename='log/snapshot.log',level=logging.DEBUG)

parser = ArgumentParser(description='Take and manage EBS snapshots.')
parser.add_argument('--region', '-r', required=True, dest='region',
                    help='aws region to act upon')
parser.add_argument('--volume', '-v', required=True, dest='volume_id',
                   help='ebs volume id')
parser.add_argument('--hourly', '-H', required=False, dest='hourly', type=int,
                    default=8,
                   help='hours between hourly snapshots')
parser.add_argument('--daily', '-d', required=False, dest='daily', type=int,
                    default=1,
                   help='days between daily snapshots')
parser.add_argument('--weekly', '-w', required=False, dest='weekly', type=int,
                    default=4,
                   help='weeks between weekly snapshots')

args = parser.parse_args()
conn = connect_to_region(args.region)

conn.create_snapshot(args.volume_id)

conn.trim_snapshots(hourly_backups=args.hourly, daily_backups=args.daily,
                   weekly_backups=args.weekly)
