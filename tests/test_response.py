# from response_generator import ResponseGenerator

# generator = ResponseGenerator()

# ticket = """
# I forgot my password and cannot login.
# """

# result = generator.generate_response(ticket)

# print("\nGenerated Response:\n")

# print(result["response"])

# print("\nRetrieved Documents:\n")

# for i, doc in enumerate(result["documents"], start=1):

#     print("=" * 60)

#     print(f"Document {i}")

#     print()

#     print(doc.metadata)

#     print()

#     print(doc.page_content)


from response_generator import ResponseGenerator

generator = ResponseGenerator()

ticket = """
I forgot my password and cannot login.
"""

result = generator.generate_response(ticket)

print("\nGenerated Response:\n")
print(result["response"])

print("\nSource References:\n")

for i, source in enumerate(result["sources"], start=1):

    print("=" * 60)
    print(f"Source {i}")
    print()
    print(f"Document : {source['source']}")
    print(f"Page     : {source['page']}")