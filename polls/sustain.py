from django.core.cache import cache
import pickle

model_cache_key = 'model_cache'
# this key is used to `set` and `get` your trained model from the cache

tokenizer = cache.get(model_cache_key) # get tokenizer from cache

if tokenizer is None:
    # your model isn't in the cache
    # so `set` it
    # load the tokenizer
    tokenizer = pickle.load(open('polls/tokenizer.pkl', 'rb'))
    cache.set(model_cache_key, tokenizer, None)
