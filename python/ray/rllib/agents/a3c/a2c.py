from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ray.rllib.agents.a3c.a3c import A3CTrainer, DEFAULT_CONFIG as A3C_CONFIG
from ray.rllib.optimizers import SyncSamplesOptimizer
from ray.rllib.utils.annotations import override
from ray.rllib.utils import merge_dicts

A2C_DEFAULT_CONFIG = merge_dicts(
    A3C_CONFIG,
    {
        "sample_batch_size": 20,
        "min_iter_time_s": 10,
        "sample_async": False,
    },
)


class A2CTrainer(A3CTrainer):
    """Synchronous variant of the A3CTrainer."""

    _name = "A2C"
    _default_config = A2C_DEFAULT_CONFIG

    @override(A3CTrainer)
    def _make_optimizer(self):
        return SyncSamplesOptimizer(
            self.local_evaluator,
            self.remote_evaluators,
            train_batch_size=self.config["train_batch_size"])
