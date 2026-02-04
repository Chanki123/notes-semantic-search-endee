"""
This script performs semantic search on stored study notes
using vector similarity from Endee.
"""

def generate_query_embedding(query):
    return [0.0] * 768


def search_endee(query_embedding):
    # TODO: Replace with Endee similarity search
    return ["Sample relevant study note"]


if __name__ == "__main__":
    query = input("Enter your search query: ")
    query_embedding = generate_query_embedding(query)
    results = search_endee(query_embedding)

    print("\nSearch Results:")
    for result in results:
        print("-", result)
