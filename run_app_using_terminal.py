from graph import app


def main():
    question = input("Enter Your Question: ")

    # Kept your exact input dictionary structure
    inputs = {
        "question": question,
        "search_query": "",
        "search_results": [],
        "report": "",
        "feedback": "",
        "needs_more_research": False,
        "iteration_count": 0,
    }

    print("\n" + "=" * 50)
    print("FINAL REPORT")
    print("=" * 50)

    # Stream messages token-by-token in real time
    for msg, metadata in app.stream(inputs, stream_mode="messages"):
        if metadata.get("langgraph_node") == "writer" and msg.content:
            print(msg.content, end="", flush=True)

    # Fetch the final consolidated state dictionary for your sources
    result = app.get_state(config=None).values or inputs

    print("\n" + "-" * 40)
    print("\nSources")
    print("-" * 40)

    for i, source in enumerate(result["search_results"], start=1):
        print(f"{i}. {source['title']}")
        print(f"   {source['url']}\n")


if __name__ == "__main__":
    main()
