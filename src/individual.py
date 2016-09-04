class Individual():
    def __init__(self, id_number):
        self.id_number = id_number
        self.preference_list = []
        self.available_proposals = []
        self.partner = None

    def get_priority(self, other):
        """Get the priority of a match from the perspective of the current
        person.

        Args:
            other: The other person in the prospective match.
        """
        return self.preference_list.index(other)

    def __str__(self):
        preference_list_numbers = []
        for other in self.preference_list:
            preference_list_numbers.append(other.id_number)
        output = 'id_number={0} preference_list={1} partner={2}'.format(
                    self.id_number, preference_list_numbers,
                    self.partner.id_number if self.partner else None)
        return output
