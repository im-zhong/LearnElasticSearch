# 2025/11/14
# zhangzhong
# https://www.elastic.co/docs/solutions/search/get-started/keyword-search-python
# Build your first search query with Python

from elasticsearch import Elasticsearch, helpers

# Connect to the Elasticsearch cluster
# You must replace the project URL, API key, and index name with the appropriate values.
client = Elasticsearch(
    "http://localhost:9200",
    api_key="ekxIeWdwb0JJVzV6NlV4YmV1eWc6cHVfU0x3S0xyeTlEc0lsQUNhdmxGQQ=="
)
index_name = "search-6s4e"

# Define the filed mappings
# An index has mappings that define how data is stored and indexed
# Create mappings for your index, including a single text field named text:
mappings = {
    "properties": {
        "text": {
            "type": "text"
        }
    }
}

# A successful response will acknowledge the creation of the mappings:z
# {'acknowledged': True}
# mapping_response = client.indices.put_mapping(index=index_name, body=mappings)
# print(mapping_response)

# # Ingest documents
# # use a bulk helper function to add three documents to your index. 
# # Bulk requests are the preferred method for indexing large volumes of data, from hundreds to billions of documents.
# docs = [
#     {
#         "text": "Yellowstone National Park is one of the largest national parks in the United States. It ranges from the Wyoming to Montana and Idaho, and contains an area of 2,219,791 acress across three different states. Its most famous for hosting the geyser Old Faithful and is centered on the Yellowstone Caldera, the largest super volcano on the American continent. Yellowstone is host to hundreds of species of animal, many of which are endangered or threatened. Most notably, it contains free-ranging herds of bison and elk, alongside bears, cougars and wolves. The national park receives over 4.5 million visitors annually and is a UNESCO World Heritage Site."
#     },
#     {
#         "text": "Yosemite National Park is a United States National Park, covering over 750,000 acres of land in California. A UNESCO World Heritage Site, the park is best known for its granite cliffs, waterfalls and giant sequoia trees. Yosemite hosts over four million visitors in most years, with a peak of five million visitors in 2016. The park is home to a diverse range of wildlife, including mule deer, black bears, and the endangered Sierra Nevada bighorn sheep. The park has 1,200 square miles of wilderness, and is a popular destination for rock climbers, with over 3,000 feet of vertical granite to climb. Its most famous and cliff is the El Capitan, a 3,000 feet monolith along its tallest face."
#     },
#     {
#         "text": "Rocky Mountain National Park  is one of the most popular national parks in the United States. It receives over 4.5 million visitors annually, and is known for its mountainous terrain, including Longs Peak, which is the highest peak in the park. The park is home to a variety of wildlife, including elk, mule deer, moose, and bighorn sheep. The park is also home to a variety of ecosystems, including montane, subalpine, and alpine tundra. The park is a popular destination for hiking, camping, and wildlife viewing, and is a UNESCO World Heritage Site."
#     }
# ]

# bulk_response = helpers.bulk(client, docs, index=index_name)
# # (3, [])
# print(bulk_response)

# Explore the data
# A keyword search, also known as lexical search or full-text search finds relevant documents in your indices using exact matches, patterns, or similarity scoring.
# 1. Query DSL. 
# 2. ES|QL https://www.elastic.co/docs/reference/query-languages/esql 有点像sql
response = client.esql.query(
	query="""
    	FROM *
        	| WHERE MATCH(text, "yosemite")
        	| LIMIT 5
    	""",
	format="csv"
)

print(response)


## delete index
client.indices.delete(index=index_name)
