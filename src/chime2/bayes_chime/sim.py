"""

==========
Simulation
==========

TODO : Document

"""


class BayesianCHIME(object):
    """Many factors surrounding the transmission, severity of
    infections, and remaining susceptibility of local populations
    to COVID-19 remain highly uncertain. However, as new data on
    hospitalized cases becomes available, we wish to incorporate this
    data in order to update and refine our projections of future demand
    to better inform capacity planners. To that end we have extended
    CHIME to increase the epidemiological process realism and to
    coherently incorporate new data as it becomes available. This
    extension allows us to transition from a few scenarios
    to assess best and worst case projections based on parameter
    assumptions, to a probabilistic forecast representing a continuous
    distribution of likely scenarios.
    """

    def __init__(
        self,
        model: str = "SIR",
        # Setting to true enforces the normal extension
        distributions: str = "normal",
        #
    ) -> None:
        self.model = model
        self._dist = distributions











class SIR:

    def __init__(self
                 infectious_disease,
                 region,
                 ):















