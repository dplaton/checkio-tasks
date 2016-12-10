"""
For the mission "How to find friends" , it's nice to have access to a specially
made data structure. In this mission we will realize a data structure which we
will use to store and work with a friend network.
The class "Friends" should contains names and the connections between them.
Names are represented as strings and are case sensitive. Connections are
undirected, so if "sophia" is connected with "nikola",
then it's also correct in reverse.
"""
class Friends:
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        """
            Add a connection in the instance. "connection" is a set of two
            names (strings). Returns True if this connection is new.
            Returns False if this connection exists already.
        """
        if connection in self.connections:
            return False
        else:
            self.connections.append(connection)
            return True

    def remove(self, connection):
        """
            Remove a connection from the instance. "connection" is a set of
            two names (strings). Returns True if this connection is exist.
            Returns False if this connection is not in the instance.
        """
        if connection not in self.connections:
            return False
        new_list = [c for c in self.connections if c != connection]
        self.connections = new_list
        return True

    def names(self):
        """
            Returns a set of names. The set contains only names which is
            connected with somebody.
        """
        return set([name for pair in self.connections for name in pair])

    def connected(self, name):
        """
            Returns a set of names which is connected with the given "name".
            If "name" does not exists in the instance it returns an empty set.
        """

        return {list(pair - {name})[0] for pair in self.connections if name in pair}

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    f = Friends(({"nikola", "sophia"}, {"stephen", "robot"}, {"sophia", "pilot"}))
    assert f.connected("sophia") == {"nikola","pilot"}
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
