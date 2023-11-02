from openai import OpenAI

client = OpenAI(api_key="none", base_url="http://localhost:8000/v1")


# create a request not activating streaming response
input_text = 'Please extract the noun entities from the sentences (Named Entity Recognition) below and print out in the following format: \
            "A woman walks in front of a building" => "woman", "building". \
            "A man walks in an office" => "man", "office". \
            "A boy in red shirt walks in a corridor" \
            "A person lies in the bed"'

response = client.chat.completions.create(model="Qwen",
                                          messages=[
                                              {"role": "user", "content": input_text}
                                          ],
                                          stream=False,
                                          stop=[])
print(response.choices[0].message.content)
