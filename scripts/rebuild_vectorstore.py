from portfolio_app.rag import rebuild_vectorstore


if __name__ == "__main__":
    count = rebuild_vectorstore()
    print(f"Vector store rebuilt: {count} chunks")
