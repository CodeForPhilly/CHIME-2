# -*- coding: utf-8 -*-
"""
"""
from typing import List
from ._base import CompartmentalModel


_compartments: List[str] = ['susceptible', 'infected', 'removed']


class SIR(CompartmentalModel):

    def __init__(self,
                 susceptible: int,
                 infected: int,
                 removed: int
                 ) -> None:
        """
        :param susceptible:
        :type susceptible: int

        :param infected:
        :type infected: int

        :param removed:
        :type removed: int
        """

        self.total = sum[susceptible, infected, removed]
