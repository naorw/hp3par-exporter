from prometheus_client import Gauge
from prometheus_client import REGISTRY

registry = REGISTRY

gauge_hp3par_total_capacity_mib = Gauge('hp3par_totalCapacityMiB', 'Total system capacity in MiB', ["id", "hp3par_name"])
gauge_hp3par_allocated_capacity_mib = Gauge('hp3par_allocatedCapacityMiB',
                                            'Total allowed capacity in MiB', ["id", "hp3par_name"])
gauge_hp3par_free_capacity_mib = Gauge('hp3par_freeCapacityMiB',
                                       'Total free capacity in MiB', ["id", "hp3par_name"])
gauge_hp3par_failed_capacity_mib = Gauge('hp3par_failedCapacityMiB',
                                         'Total failed capacity in MiB', ["id", "hp3par_name"])
gauge_hp3par_volumes = Gauge('hp3par_volumes',
                                         'Total failed capacity in MiB', ["id", "hp3par_name"])
gauge_hp3par_volume_used = Gauge('hp3par_volume_used',
                                         'Volume used size', ["id", "hp3par_name", "baseId"])
gauge_hp3par_volume_total = Gauge('hp3par_volume_total',
                                         'Volume total size', ["id", "hp3par_name", "baseId"])
gauge_hp3par_cpg_user = Gauge('hp3par_cpg_userl',
                                         'Volume total size', ["id", "hp3par_name"])
gauge_hp3par_cpg_admin = Gauge('hp3par_cpg_admin',
                                         'Volume total size', ["id", "hp3par_name"])
gauge_hp3par_cpg_snapshot = Gauge('hp3par_cpg_snapshot',
                                         'Volume total size', ["id", "hp3par_name"])
