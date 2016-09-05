import random

from individual import Individual

class MarriagesSimulation():
    """A simulation of men and women being matched with the Gale-Shapley
       algorithm."""

    def __init__(self, size):
        """Initialize the fundamental components of the simulation.

        Args:
            size: The size of the simulation, in numbers of men, which will be
                  the same as the number of women.
        """
        self.size = size
        self.men = []
        self.women = []

    def populate(self):
        """Populate the simulation with valid men and women."""
        for i in range(0, self.size):
            self.men.append(Individual(i))
        for i in range(self.size, self.size * 2):
            self.women.append(Individual(i))

    def set_preferences(self):
        """Set the preference list for all the men and women in this
           simulation."""
        for man in self.men:
            man.preference_list = self.random_woman_list()
            man.available_proposals = list(man.preference_list)
        for woman in self.women:
            woman.preference_list = self.random_man_list()

    def random_id_list(self):
        """Get a randomized list of indexes that may be used to refer to
           internal lists of men and women.

        Returns:
            A randomized list of indexes.
        """
        id_list = range(0, self.size)
        random.shuffle(id_list)
        return id_list

    def random_man_list(self):
        """Get a randomized list of men from this simulation.

        Returns:
            A random list of Man objects.
        """
        random_id_list = self.random_id_list()
        man_list = []
        for i in random_id_list:
            man_list.append(self.men[i])
        return man_list

    def random_woman_list(self):
        """Get a randomized list of women from this simulation.

        Returns:
            A random list of Woman objects.
        """
        random_id_list = self.random_id_list()
        woman_list = []
        for i in random_id_list:
            woman_list.append(self.women[i])
        return woman_list

    def is_stable(self):
        """Check if this simulation has reached a stable state.

        The simulation is considered stable if both members of couple would
        not be happier with an alternative match.

        Returns:
            A boolean indicating the stability of this simulation.
        """
        for man in self.men:
            if not man.partner:
                return False
        return True

    def pair_couple(self, man, woman):
        """Pair two individuals.

        The man in this couple will no longer be able to propose
        to the specified woman.

        Args:
            man: The first individual.
            woman: The second individual.
        """
        man.partner = woman
        woman.partner = man
        print 'New pair man={0} woman={1}'.format(man.id_number, woman.id_number)

    def free_couple(self, man, woman):
        """Free two individuals.

        Args:
            man: The first individual.
            woman: The second individual.
        """
        man.partner = None
        woman.partner = None

    def match(self):
        """Perform the Gale-Shapley matching algorithm.

        Print new matches that are made and the state of the simulation
        between iterations.
        """
        iterations = 0
        while not self.is_stable():
            iterations += 1
            print '{0}\n'.format(self)
            for man in self.men:
                if not man.partner:
                    for woman in man.available_proposals:
                        if not woman.partner:
                            self.pair_couple(man, woman)
                            man.available_proposals.remove(woman)
                            break
                        elif woman.partner and woman.get_priority(man) < woman.get_priority(woman.partner):
                            self.free_couple(woman.partner, woman)
                            self.pair_couple(man, woman)
                            break
        print 'Matching complete'
        print 'iterations={0}'.format(iterations)
        print self

    def __str__(self):
        men_outputs = []
        for man in self.men:
            men_outputs.append('\t' + str(man))
        men_string = '\n'.join(men_outputs)
        women_outputs = []
        for woman in self.women:
            women_outputs.append('\t' + str(woman))
        women_string = '\n'.join(women_outputs)
        return ('Men:\n'
                '{0}\n'
                'Women:\n'
                '{1}'.format(men_string, women_string))
