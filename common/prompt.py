import pathway as pw

from datetime import datetime
from common.geminiapi_helper import gemini_chat_completion


def prompt(index, embedded_query, user_query):

    @pw.udf
    def build_prompt(local_indexed_data, query):
        f = open ("./data/data.jsonl","r")
        docs_str=f.read()
        print("STRING:",docs_str)
        prompt = f"You are MedAI. An AI assistant to help users with finding information about medicines. Here is the text from the webpage 1mg.com that is needed to answer the user's query: \n {docs_str} \n The user is asking: \n {query} \n Please provide an detailed answer to the user's question using the information provided in the webpage. If you cannot find a definitive answer, inform that the information cannot be found."

        print("PROMPT:\n\n",prompt,"\n\n")

        with open("./data/logquery.txt", "w") as file:
            file.write(prompt)
        return prompt
    
    query_context = embedded_query + index.get_nearest_items(
        embedded_query.vector, k=3, collapse_rows=True
    ).select(local_indexed_data_list=pw.this.doc).promise_universe_is_equal_to(embedded_query)

    prompt = query_context.select(
        prompt=build_prompt(pw.this.local_indexed_data_list, user_query)
    )

    return prompt.select(
        query_id=pw.this.id,
        result=gemini_chat_completion(pw.this.prompt),
    )
