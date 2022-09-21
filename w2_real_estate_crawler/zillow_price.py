import os

from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults


zillow_key = os.environ['ZILLOW_KEY']
zillow_data = ZillowWrapper(zillow_key)

deep_search_response = zillow_data.get_deep_search_results('2114 Bigelow Ave', '98109', True)
result = GetDeepSearchResults(deep_search_response)

print(result.bathrooms)
# except BaseException as e:
#     print(e)

