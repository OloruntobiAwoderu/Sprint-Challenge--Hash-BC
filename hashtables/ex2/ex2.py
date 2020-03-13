#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    ticket = hash_table_retrieve(hashtable, "NONE")
    route[0] = ticket
    i = 1
    while (ticket != "NONE"):
        ticket = hash_table_retrieve(hashtable, ticket)
        route[i] = ticket
        i += 1

    return route[:-1]
