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

        Returns:
            An index indicating the priority of a match.
            Lower numbers indicate higher priorities.
        """
        return self.preference_list.index(other)

    def get_id_list(self, instance_list):
        """Get a list of ID numbers corresponding to the input
        list of instances.

        Args:
            intance_list: A list of other Individual objects.

        Returns:
            A list of ID numbers.
        """
        id_list = []
        for i in instance_list:
            id_list.append(i.id_number if i else None)
        return id_list

    def __str__(self):
        output = ('id_number={0} preference_list={1} available_proposals={2} '
                  'partner={3}'.format(
                     self.id_number,
                     self.get_id_list(self.preference_list),
                     self.get_id_list(self.available_proposals),
                     self.partner.id_number if self.partner else None))
        return output
