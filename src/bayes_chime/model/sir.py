"""model/sir.py
===
SIR
===

SIR Compartmental Model

TODO : Documentation
TODO : Unit testing

"""
from typing import Any, List, Dict, NewType

from .base import CompartmentalModel

_valid_distributions: List[str] = ["normal"]
_sir_params: Dict[str, Any] = {
    "compartments": ["susceptible", "infected", "removed"],
    "epidemiological": ["beta" or "initial_doubling_time", "gamma" or "recovery_days"],
    "regional": [
        "market_share",
        "initial_hospitalized",
        "hospitalization_probability",
        "hospitalized_LOS",
        "initial_icu",
        "icu_probability",
        "icu_LOS",
        "initial_ventilatory",
        "ventilatory_probability",
        "ventilatory_LOS",
    ],
}


class SIR(CompartmentalModel):
    """SIR Compartmental Model
    """
    _model_parameters: List[str] = [[i for i in values] for values in _sir_params.values()]

    def __init__(self, distributions="normal"):
        super().__init__()
        self._dist = distributions
        self._valid_parameters = _sir_params
        self.gamma: float = 0.0
        self.susceptible: int = 0
        self.infected: int = 0
        self.removed: int = 0

    def fit(self, parameters: Dict[str, Any], census) -> None:
        """Fit the model to the time series data provided by hospital
        census records"""

        if "gamma" not in parameters:
            self.gamma = 1 / (
                parameters["recovery_days"] / parameters["days_per_step"]
            )

        if "beta" not in parameters:
            total_population = sum(
                parameters["initial_" + comp] for comp in self.compartments
            )
            beta = log(2) / (parameters["initial_doubling_time"]
                             / parameters["days_per_step"]
                             )
            beta += parameters["gamma"]
            beta *= total_population / parameters["initial_susceptible"]
            parameters["beta"] = beta

    def simulate(
        self, data: Dict[str, NormalDistVar], **parameters: Dict[str, FloatOrDistVar]
    ) -> Array:
        """Executes SIR step and patches results such that each component is larger zero.
        Arguments:
            data:
                susceptible: Susceptible population
                infected: Infected population
                recovered: Recovered population
            pars:
                beta: Growth rate for infected
                gamma: Recovery rate for infected
        Returns:
            Updated compartments and optionally additional information like change
            from last iteration.
        """
        super().simulate()
        infected = data["infected"]
        recovered = data["recovered"]

        total = susceptible + infected + recovered

        d_si = parameters["beta"] * susceptible / total * infected
        d_ir = parameters["gamma"] * infected

        susceptible -= d_si
        infected += d_si - d_ir
        recovered += d_ir

        susceptible = max(susceptible, 0)
        infected = max(infected, 0)
        recovered = max(recovered, 0)

        rescale = total / (susceptible + infected + recovered)

        return {
            "susceptible": susceptible * rescale,
            "infected": infected * rescale,
            "recovered": recovered * rescale,
            "infected_new": d_si * rescale,
            "recovered_new": d_ir * rescale,
        }
        # _validate_parameters(parameters, self._model_parameters)
        # self._idx = _build_dt_index(
        #     parameters["dates"]["start_date"], parameters["dates"]["stop_date"]
        # )
        # if "compartments" not in parameters:
        #     raise ModelError("Parameters missing compartments")
        # self.compartments_ = _get_compartments(
        #     self._model_parameters["compartments"],
        #     parameters["compartments"]
