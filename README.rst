awstools
========

Python tools for EC2 and AWS management

These are my own tools for EC2 and AWS management, and I expect them to
build up a little over time.

So far there are tools for:

* tools/snapshot.py
    A simple tool to take a snapshot then manage snapshots, keeping
    appropriate ones. This is little more than a wrapper on boto's
    snapshot functions, supporting snapshotting a volume, then
    managing the number of snapshots kept across the region.
