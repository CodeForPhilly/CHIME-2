"""model/compartment.py

===================
Model Compartments
==================

TODO : Documentation
TODO : Unit Testing

"""


class ModelCompartment(int):
    """Base class for model compartments"""

    def __init__(self, population: int) -> None:
        """
        :param population:
            Total starting population of individuals within the
            compartment.
        """
        super().__init__()
        self._population = population


class Susceptible(ModelCompartment):
    """The portion of the population susceptible to infection"""

    def __init__(self, population: int) -> None:
        super().__init__(population)


class Exposed(ModelCompartment):
    """The portion of the population exposed to infection"""

    def __init__(self, population: int) -> None:
        super().__init__(population)


class Infected(ModelCompartment):
    """The portion of the population actively infected."""

    def __init__(self, population: int) -> None:
        super().__init__(population)


class Recovered(ModelCompartment):
    """The portion of the population which has recovered from infection
    """

    def __init__(self, population: int = 0) -> None:
        super().__init__(population)
