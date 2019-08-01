import dask_jobqueue

from .util import identify_host


def _get_base_class():
    """Function to determine which base class to use.
    """

    base_classes = {
        'hobart': dask_jobqueue.PBSCluster,
        'cheyenne': dask_jobqueue.PBSCluster,
        'casper': dask_jobqueue.SLURMCluster,
    }

    host = identify_host()
    return base_classes[host]


_base_class = _get_base_class()


class NCARCluster(_base_class):
    """Class to launch Dask Clusters with NCAR's queueing systems (Slurm, PBS)

    Returns
    -------
    cluster : object

         - PBSCluster, if the host on Cheyenne cluster or Hobart cluster.
         - SLURMCluster, if the host is on Casper cluster.
         - Throws exception otherwise.
    """

    def __init__(self, **kwargs):
        super(NCARCluster, self).__init__(**kwargs)
