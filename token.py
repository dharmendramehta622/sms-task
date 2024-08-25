
"""
Problem Statement

In our system, we rely on a third-party authentication service to 
handle user authentication. This service is external, and we 
frequently interact with it by calling its API endpoints to 
authenticate users and obtain tokens. However, since this 
authentication service is a managed solution hosted by a third 
party, it introduces some latency whenever we make a request to 
authenticate. Over time, this latency has become a bottleneck for
our APIs, leading to performance issues.

To address this growing concern, we've decided to implement a local 
caching mechanism to store authentication tokens. By maintaining these
tokens in a local cache, we can minimize the need to repeatedly hit the
 third-party authentication service, reducing latency and improving 
 overall API performance.

This local cache will be an in-memory data structure designed to hold 
the tokens for quick access. To implement this, you'll create a class 
named AuthTokenCache. This class will provide two key methods:

1.getToken(): This method will be responsible for fetching a token from 
  the cache when needed.
2.setToken(): This method will allow new tokens to be added to the cache.

Additionally, the cache will have a limited size, holding up to a 
maximum of N tokens at a time. Once the cache reaches its capacity, 
it should follow a First-In-First-Out (FIFO) eviction strategy. 
This means that when a new token is added and the cache is full, 
the oldest token (the one added first) will be removed to make space 
for the new one.

"""

"""
 * @author [kode-mafia008]
 * @email [dharmendramehta622@mail.com]
 * @create date 2024-08-25 09:33:06
 * @modify date 2024-08-25 09:33:06
 * @desc Local Token Cache Implementation
"""
 

from collections import deque

class AuthTokenCache:
    def __init__(self, max_size=10):
        # The cache holds tuples of (user_id, token) for quick access
        self.cache = deque(maxlen=max_size)
        self.cache_map = {}  # To track tokens for quick retrieval

    def get_token(self, user_id):
        """
        Retrieve a token from the cache based on the user ID.
        """
        return self.cache_map.get(user_id)

    def set_token(self, user_id, token):
        """
        Add a new token to the cache. If the cache is full, the oldest token is evicted.
        """
        if user_id in self.cache_map:
            # Remove the existing token before adding the new one
            self.cache.remove((user_id, self.cache_map[user_id]))
        
        # Add the new token to the cache
        self.cache.append((user_id, token))
        self.cache_map[user_id] = token

        # Handle the eviction in case the cache is full
        if len(self.cache) > self.cache.maxlen:
            oldest_user, _ = self.cache.popleft()
            del self.cache_map[oldest_user]

# Example usage:
auth_cache = AuthTokenCache(max_size=5)
auth_cache.set_token('user_1', 'token_abc')
print(auth_cache.get_token('user_1'))  # Output: 'token_abc'
