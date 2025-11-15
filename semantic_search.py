# 2025/11/15
# zhangzhong
# semantic search

# Semantic search is a type of AI-powered search that enables you to use natural language in your queries.
# It returns results that match the meaning of a query, as opposed to literal keyword matches.

## Create a vector database
# The way that you store vectors has a significant impact on the performance and accuracy of search results. 
# They must be stored in specialized data structures designed to ensure efficient similarity search and speedy vector distance calculations
# This guide uses the [[semantic text]] field type, which provides sensible defaults and automation.

# 1. Create an index with Semantic Search

from elasticsearch import Elasticsearch, helpers

client = Elasticsearch(
    "http://localhost:9200",
    api_key="ekxIeWdwb0JJVzV6NlV4YmV1eWc6cHVfU0x3S0xyeTlEc0lsQUNhdmxGQQ=="
)

index_name = "search-0ixx"

# 2. Create a semantic_text field mapping
# Each index has mappings that define how data is stored and indexed, like a schema in a relational database.
# When you use semantic_text fields, the type of vector is determined by the vector embedding model. 
# In this case, the default ELSER model will be used to create sparse vectors.
mappings = {
    "properties": {
        "text": {
            "type": "semantic_text"
        }
    }
}
mapping_response = client.indices.put_mapping(index=index_name, body=mappings)
print(mapping_response)

# 3. Add documents
# You can use the Elasticsearch bulk API to ingest an array of documents:
# First, the content is divided into smaller, manageable chunks 
# to ensure that meaningful segments can be more effectively processed and searched. 
# Each chunk of text is then transformed into a sparse vector by using the ELSER model's text expansion techniques.
# 所以还是简单的文本分块
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

# # Timeout to allow machine learning model loading and semantic ingestion to complete
# ingestion_timeout=300

# bulk_response = helpers.bulk(
#     client.options(request_timeout=ingestion_timeout),
#     docs,
#     index=index_name
# )
# print(bulk_response)

# 4. Perform a semantic search
# When you run a semantic search, the text in your query must be turned into vectors that use the same embedding model as your vector database
# This step is performed automatically when you use semantic_text fields. 
# https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/semantic-text

# Here is an example semantic search query:
search_query = {
    "query": {
        "semantic": {
            "field": "text",
            "query": "Which national park has the largest concentration of wildlife?"
        }
    }
}
search_response = client.search(index=index_name, body=search_query)
for hit in search_response["hits"]["hits"]:
    print(f"Score: {hit['_score']}, Text: {hit['_source']['text']}")